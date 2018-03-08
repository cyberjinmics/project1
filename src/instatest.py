#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from .unfollow_protocol import unfollow_protocol
from .userinfo import UserInfo
import atexit
import datetime
import itertools
import json
import logging
import random
import signal
import sys
import sqlite3
import time
import requests
from .sql_updates import check_and_update, check_already_liked, check_already_followed
from .sql_updates import insert_media, insert_username, insert_unfollow_count
from .sql_updates import get_usernames_first, get_usernames, get_username_random
from .sql_updates import check_and_insert_user_agent
from fake_useragent import UserAgent

class InstaTest:
    url_user = 'https://instagram.com/%s'
    url_query = 'https://www.instagram.com/graphql/query/?query_hash=%s&variables=%s'
    has_next_page = False
    end_cursor = None
	query_hash = None
    query_hash_test_id = 1183095
	query_hash_scripts = ["/static/bundles/Consumer.js/", "/static/bundles/ProfilePageContainer.js/", "/static/bundles/ConsumerCommons.js/", "/static/bundles/Vendor.js/", "/static/bundles/en_US.js/"]
	query_hash_regexes = ['l="([a-f0-9]{32})"', '"([a-f0-9]{32})"', '"([a-f0-9]{32})"', '"([a-f0-9]{32})"', '"([a-f0-9]{32})"']
	query_after = None
	query_vars = '{"id":"%s", "first": %i}'
	
	def __init__(self):

        #if proxy != "":
        #    proxies = {
        #        'http': 'http://' + proxy,
        #       'https': 'http://' + proxy,
        #    }
        #    self.s.proxies.update(proxies)
        # convert login to lower
        
	def clean_vars(self):
	    self.user_login = login.lower()
		self.email = self.email.lower()
	    self.username = self.username.lower()
        self.bot_mode = 0
        now_time = datetime.datetime.now()
        log_string = 'Instabot v1.2.0 started at %s:\n' % \
                     (now_time.strftime("%d.%m.%Y %H:%M"))
        self.write_log(log_string)
        #self.login()
        self.populate_user_blacklist()
        signal.signal(signal.SIGTERM, self.cleanup)
        atexit.register(self.cleanup)
	
	def get_query_hash(self, account):
	    js_file_regex = '/static/bundles/ProfilePageContainer.js/[a-z0-9]+\.js'
		url_user = self.url_user %(account)
		r = self.s.get(url_user)
        matches = re.findall(js_file_regex, r.text)
		js_file_addr = 'https://instagram.com/'+matches[0]
		
		if(self.check_query_hash(self.query_hash) == False):
		    valid_hash = False
		    i = 0
		    while(i < len(self.query_hash_scripts) and valid_hash == False):
			    js_file_regex = self.query_hash_scripts[i]+'[a-z0-9]+\.js'
				query_hash_regex = query_hash_regexes[i]
		        url_user = self.url_user %(account)
				r = self.s.get(url_user)
                mark_up = r.text
				matches = re.findall(js_file_regex, r.text)
				script_addr = 'https://instagram.com/'+matches[0]
				script = self.s.get(script_addr)
                script_src = script.text
				hashes = re.findall(query_hash_regex, script_src)
				if(len(hashes) == 0):
				    print('No hash Found in'+script_addr)
				else:
				    for hash in hashes:
					    print('checking the hash '+hash+' in '+script_addr+'....')
					    is_the_hash = valid_hash = self.check_query_hash(hash)
						if(is_the_hash == True):
						    self.query_hash = hash
						else:
						    self.query_hash = None
			
		else:
		    return self.query_hash
			
	def check_query_hash(self, query_hash):
	    id = self.query_hash_test_id
		first = 3
	    query_vars = self.query_vars%(id, first)
		url_query = self.query_url%(query_hash, query_vars)
		r = self.s.get(url_user)
		all_data = json.loads(r.text)
		user_id = all_data["data"]["user"]["id"]
		first_follower_username = all_data['data']['user']['edge_followed_by']['edges'][0]['node']['username']
		if(user_id == self.query_hash_test_id and len(first_follower_username) > 0):
		     return True
		else:
		    return False