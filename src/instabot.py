#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from .userinfo import UserInfo
import datetime
import json
import logging
import time
import requests
from requests_toolbelt import MultipartEncoder
import uuid
import re
from .commentGen import commentGen
from .filesCount import filesCount
from random import *
import random
import os
from fake_useragent import UserAgent

class InstaBot:
    """
    Instagram bot v 1.2.0

    https://github.com/LevPasha/instabot.py
    """
    #database_name = "follows_db.db"

    url = 'https://www.instagram.com/'
    url_tag = 'https://www.instagram.com/explore/tags/%s/?__a=1'
    url_likes = 'https://www.instagram.com/web/likes/%s/like/'
    url_unlike = 'https://www.instagram.com/web/likes/%s/unlike/'
    url_comment = 'https://www.instagram.com/web/comments/%s/add/'
    url_follow = 'https://www.instagram.com/web/friendships/%s/follow/'
    url_unfollow = 'https://www.instagram.com/web/friendships/%s/unfollow/'
    url_login = 'https://www.instagram.com/accounts/login/ajax/'
    url_signup = 'https://www.instagram.com/accounts/web_create_ajax/'
    url_logout = 'https://www.instagram.com/accounts/logout/'
    url_media_detail = 'https://www.instagram.com/p/%s/?__a=1'
    url_user_detail = 'https://www.instagram.com/%s/?__a=1'
    api_user_detail = 'https://i.instagram.com/api/v1/users/%s/info/'
    url_upload = 'https://www.instagram.com/create/upload/photo/'
    url_upload_configure = 'https://www.instagram.com/create/configure/'
    url_delete_media = 'https://www.instagram.com/create/%s/delete/'
    url_change_profile_pix = 'https://www.instagram.com/accounts/web_change_profile_picture/'
    ####### Url Strings ########
    url_user = 'https://instagram.com/%s/'
    url_query = 'https://www.instagram.com/graphql/query/?query_hash=%s&variables=%s'
    url_ping_server = 'https://www.shopbraid.com/instapybot_log.php'
    url_bot_av_acct = 'https://www.shopbraid.com/bot_av_acct.php'
    url_bot_av_acct_update = 'https://www.shopbraid.com/bot_av_acct_update.php'

    ######### General Data #########
    bot_life_span = 360
    bot_age = 0
    server_off_threshold = 500000

    ######## Upload Data ###########
    uuid = ''

    ######### Signup Form Data #########
    email = ''
    username = ''
    first_name = ''
    signup_password = ''
    seamless_login_enabled = 1
    ######### Login Form Data #########
    user_login = ''
    user_password = ''
    ######### Followers Page Data #########
    has_next_page = False
    end_cursor = ""
    query_first = 300
    query_hash = ""
    query_hash_test_id = "11830955"
    query_hash_scripts = ["/static/bundles/Consumer.js/", "/static/bundles/ProfilePageContainer.js/", "/static/bundles/ConsumerCommons.js/", "/static/bundles/Consumer.js/", "/static/bundles/Vendor.js/", "/static/bundles/en_US.js/"]
    query_hash_regexes = ['l="([a-f0-9]{32})"', '"([a-f0-9]{32})"', '"([a-f0-9]{32})"', '"([a-f0-9]{32})"', '"([a-f0-9]{32})"', '"([a-f0-9]{32})"']
	
    ######### Actions Data ############
    keep_following = True
    accounts_for_followers = []
    account_for_followers = ''
    blacklist_account_for_followers = True
    account_for_followers_id = ''
    account_for_followers_key = -1
    accounts_to_follow = []
    blacklisted_accounts = ['payporte', 'damselbim', 'jijinigeria']
    account_followings = []
    follows_today = 0
    unfollows_today = 0
    likes_today = 0
    comments_today = 0
    comments_per_day = 300
    start_unfollowing_threshold = 1500
    follows_per_day = 300
    unfollows_per_day = 300
    action_sleep = 60
    min_media_count = 1
    min_followers_count = 1
    min_followings_count = 1
    min_followings_to_followes_ratio = 10
    user_agent = "" ""
    accept_language = 'en-US,en;q=0.5'

    # If instagram ban you - query return 400 error.
    error_400 = 0
    # If you have 3 400 error in row - looks like you banned.
    error_400_to_ban = 3
    # If InstaBot think you are banned - going to sleep.
    ban_sleep_time = 2 * 60 * 60
    log_mod = 0

    # All counter.
    bot_follow_list = []
    user_info_list = []
    user_list = []
    ex_user_list = []
    is_checked = False
    is_selebgram = False
    is_fake_account = False
    is_active_user = False
    is_following = False
    is_follower = False
    is_rejected = False
    is_self_checking = False
    is_by_tag = False
    is_follower_number = 0
    like_counter = 0
    follow_counter = 0
    unfollow_counter = 0
    comments_counter = 0

    self_following = 0
    self_follower = 0

    # Log setting.
    logging.basicConfig(filename='errors.log', level=logging.INFO)
    log_file_path = ''
    log_file = 0

    # Other.
    user_id = 0
    media_by_tag = 0
    media_on_profile = []
    login_status = False
    csrftoken = ''
    default_content_type = 'application/x-www-form-urlencoded'

    # Running Times
    start_at_h = 0
    start_at_m = 0
    end_at_h = 23
    end_at_m = 59

    # For new_auto_mod
    next_iteration = {"Like": 0, "Follow": 0, "Unfollow": 0, "Comments": 0}

    def __init__(self):
        fake_ua = UserAgent()
        self.user_agent = str(fake_ua.random)
        self.s = requests.Session()

    def clean_vars(self):
        self.user_login = self.user_login.lower()
        self.email = self.email.lower()
        self.username = self.username.lower()
        self.bot_mode = 0
        now_time = datetime.datetime.now()
        log_string = 'Instabot v1.2.0 started at %s:\n' % \
                     (now_time.strftime("%d.%m.%Y %H:%M"))
        self.write_log(log_string)
        #self.login()
        #self.populate_user_blacklist()
        #signal.signal(signal.SIGTERM, self.cleanup)
        #atexit.register(self.cleanup)

    def generate_uuid(self, uuid_type):
            generated_uuid = str(uuid.uuid4())
            if uuid_type:
                return generated_uuid
            else:
                return generated_uuid.replace('-', '')

    def change_profile_pix(self, input_name, filename, file_address):
        self.uuid = self.generate_uuid(False)
        url_change_profile_pix = self.url_change_profile_pix
        data = {input_name: (filename + '.jpg', open(file_address, 'rb'), 'image/jpeg')}
        m = MultipartEncoder(data, boundary=self.uuid)
        self.s.headers.update({'Content-Type': 'multipart/form-data; boundary=' + self.uuid})
        r = self.s.post(url_change_profile_pix, data=m.to_string())
        all_data = json.loads(r.text)
        changed = False
        if "changed_profile" in all_data:
            if all_data["changed_profile"]:
                changed = True
        if changed:
            log_text = "Profile Pix Successfully Changed"
            returnValue = True
        else:
            log_text = "Profile Pix Upload Failed!"
            returnValue = False
        print(log_text)
        self.s.headers.update({'Content-Type': self.default_content_type})
        return returnValue


    def upload_media(self, input_name, filename, mention, media_comment):
        self.uuid = self.generate_uuid(False)
        url_upload = self.url_upload
        upload_id = str(int(time.time() * 1000))
        data = {
            "upload_id": upload_id,
            input_name: (input_name+'.jpg', open(filename, 'rb'), 'image/jpeg')
        }
        m = MultipartEncoder(data, boundary=self.uuid)
        self.s.headers.update({'Content-Type': 'multipart/form-data; boundary='+self.uuid})
        self.s.headers.update({'Referer': 'https://www.instagram.com/create/style/'})
        r = self.s.post(url_upload, data=m.to_string())
        all_data = json.loads(r.text)
        trueAggregate = 0
        if "upload_id" in all_data:
            upload_id = all_data["upload_id"]
            print('UPLOAD ID: '+str(upload_id))
            trueAggregate += 1
            all_data = self.add_caption(upload_id, mention)
            print(all_data)
            if len(all_data) > 0:
                user_id = all_data["media"]["caption"]["user_id"]
                media_id_user_id = all_data["media"]["id"]
                media_id = str(media_id_user_id).replace("_"+str(user_id), "")
                if(len(media_id) > 0):
                    trueAggregate += 1
                self.like(media_id)
                do_comment = self.comment(media_id, media_comment)
                print(do_comment)
                self.default_headers()
                if trueAggregate == 2:
                    return True
                else:
                    return False
            else:
                self.keep_following = False
                print('Media caption configuration failed. So media was deleted')
                print('Logging out in 5 seconds....')
                time.sleep(5)
                self.logout()
                print('Logging back in 10 seconds')
                self.login()
                self.keep_following = True
                self.log_bot()

    def add_caption(self, upload_id, mention):
        caption = commentGen(1, 'caption', mention)
        configure_body = {
            "upload_id": upload_id,
            "caption": caption
        }
        print(caption)
        url_upload_configure = self.url_upload_configure
        self.s.headers.update({'Content-Type': 'application/x-www-form-urlencoded'})
        self.s.headers.update({'Referer': 'https://www.instagram.com/create/details/'})
        r = self.s.post(url_upload_configure, data=configure_body, allow_redirects=True)
        all_data = json.loads(r.text)
        if all_data["media"]["caption"] is None:
            ui = UserInfo()
            user_id = ui.get_user_id_by_login(self.user_login)
            media_id_user_id = all_data["media"]["id"]
            media_id = str(media_id_user_id).replace("_" + str(user_id), "")
            self.delete_media(media_id)
            all_data = []
        return all_data

    def delete_media(self, media_id):
        """ Send http request to delete media """
        all_data = []
        if self.login_status:
            url_delete_media = self.url_delete_media % media_id
            try:
                delete_media = self.s.post(url_delete_media)
                all_data = json.loads(delete_media.text)
                if all_data["status"] == "ok":
                    log_string = "Media deleted: %s" % media_id
                    self.write_log(log_string)
            except:
                logging.exception("Except on delete_media!")
        print('DELETE!!!')
        return all_data


    def default_headers(self):
        self.s.headers.update({'Content-Type': 'application/x-www-form-urlencoded'})
        self.s.headers.update({'Referer': 'https://www.instagram.com/'})


    def signup(self):
        log_string = 'Trying to signup ...\n'
        self.write_log(log_string)
        self.signup_post = {
            'email': self.email,
            'first_name': self.first_name,
            'password': self.signup_password,
            'seamless_login_enabled': self.seamless_login_enabled,
            'username': self.username
        }

        self.s.headers.update({
            'Accept': '*/*',
            'Accept-Language': self.accept_language,
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Content-Length': '0',
            'Host': 'www.instagram.com',
            'Origin': 'https://www.instagram.com',
            'Referer': 'https://www.instagram.com/',
            'User-Agent': self.user_agent,
            'X-Instagram-AJAX': '1',
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-Requested-With': 'XMLHttpRequest'
        })
		
        r = self.s.get(self.url)
        self.s.headers.update({'X-CSRFToken': r.cookies['csrftoken']})
        self.csrftoken = r.cookies['csrftoken']
        time.sleep(5 * random.random())
        signup = self.s.post(
            self.url_signup, data=self.signup_post, allow_redirects=True)
        self.s.headers.update({'X-CSRFToken': signup.cookies['csrftoken']})
        self.csrftoken = signup.cookies['csrftoken']
        #ig_vw=1536; ig_pr=1.25; ig_vh=772;  ig_or=landscape-primary;
        self.s.cookies['ig_vw'] = '1536'
        self.s.cookies['ig_pr'] = '1.25'
        self.s.cookies['ig_vh'] = '772'
        self.s.cookies['ig_or'] = 'landscape-primary'
        time.sleep(5 * random.random())

        if signup.status_code == 200:
            r = self.s.get('https://www.instagram.com/')
            finder = r.text.find(self.username)
            if finder != -1:
                self.bot_start = datetime.datetime.now()
                ui = UserInfo()
                self.user_id = ui.get_user_id_by_login(self.username)
                self.login_status = True
                self.ping_server_and_log_file(1)
                log_string = '%s signup successfull. You are loggedin!' % (self.username)
                self.write_log(log_string)
            else:
                self.login_status = False
                self.write_log('Signup error! Check your login data!')
        else:
            self.write_log('Signup! Connection error!')

    def ping_server_and_log_file(self, test):
        url_ping_server = self.url_ping_server
        ping_body = {
            "username": self.username,
            "email": self.email,
            "first_name": self.first_name,
            "test": test
        }
        r = self.s.post(url_ping_server, data=ping_body, allow_redirects=True)
        all_data = json.loads(r.text)
        if "Inserted" in all_data:
            if all_data["Inserted"]:
                print('{'+self.username+', '+self.email+', '+self.first_name+'} Logged at '+url_ping_server)
            else:
                print(
                    '{' + self.username + ', ' + self.email +
                    ', ' + self.first_name + ' ' + test + ' } Log at ' + url_ping_server+' failed!')
        with open('username.txt', 'wt') as f:
            f.write(self.username)


    def login(self):
        log_string = 'Trying to login as %s...\n' % (self.user_login)
        self.write_log(log_string)
        self.login_post = {
            'username': self.user_login,
            'password': self.user_password
        }

        self.s.headers.update({
            'Accept': '*/*',
            'Accept-Language': self.accept_language,
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Content-Length': '0',
            'Host': 'www.instagram.com',
            'Origin': 'https://www.instagram.com',
            'Referer': 'https://www.instagram.com/',
            'User-Agent': self.user_agent,
            'X-Instagram-AJAX': '1',
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-Requested-With': 'XMLHttpRequest'
        })

        r = self.s.get(self.url)
        self.s.headers.update({'X-CSRFToken': r.cookies['csrftoken']})
        self.csrftoken = r.cookies['csrftoken']
        time.sleep(5 * random.random())
        login = self.s.post(
            self.url_login, data=self.login_post, allow_redirects=True)
        self.s.headers.update({'X-CSRFToken': login.cookies['csrftoken']})
        self.csrftoken = login.cookies['csrftoken']
        #ig_vw=1536; ig_pr=1.25; ig_vh=772;  ig_or=landscape-primary;
        self.s.cookies['ig_vw'] = '1536'
        self.s.cookies['ig_pr'] = '1.25'
        self.s.cookies['ig_vh'] = '772'
        self.s.cookies['ig_or'] = 'landscape-primary'
        time.sleep(5 * random.random())

        if login.status_code == 200:
            r = self.s.get('https://www.instagram.com/')
            finder = r.text.find(self.user_login)
            if finder != -1:
                self.bot_start = datetime.datetime.now()
                ui = UserInfo()
                self.user_id = ui.get_user_id_by_login(self.user_login)
                self.login_status = True
                log_string = '%s login success!' % (self.user_login)
                self.write_log(log_string)
            else:
                self.login_status = False
                self.write_log('Login error! Check your login data!')
        else:
            self.write_log('Login error! Connection error!')

    def logout(self):
        now_time = datetime.datetime.now()
        log_string = 'Logout: likes - %i, follow - %i, unfollow - %i, comments - %i.' % \
                     (self.like_counter, self.follow_counter,
                      self.unfollow_counter, self.comments_counter)
        self.write_log(log_string)
        work_time = datetime.datetime.now() - self.bot_start
        log_string = 'Bot work time: %s' % (work_time)
        self.write_log(log_string)

        try:
            logout_post = {'csrfmiddlewaretoken': self.csrftoken}
            logout = self.s.post(self.url_logout, data=logout_post)
            self.write_log("Logout success!")
            self.login_status = False
        except:
            logging.exception("Logout error!")
			
    def like(self, media_id):
        """ Send http request to like media by ID """
        all_data = []
        if self.login_status:
            url_likes = self.url_likes % (media_id)
            try:
                like = self.s.post(url_likes)
                all_data = json.loads(like.text)
                if all_data["status"] == "ok":
                    self.like_counter += 1
                    self.likes_today += 1
                    all_data["status_code"] = like.status_code
            except:
                logging.exception("Except on like!")
        print('Like!!!')
        return all_data

    def unlike(self, media_id):
        """ Send http request to unlike media by ID """
        if self.login_status:
            url_unlike = self.url_unlike % (media_id)
            try:
                unlike = self.s.post(url_unlike)
            except:
                logging.exception("Except on unlike!")
                unlike = 0
            return unlike

    def comment(self, media_id, comment_text):
        """ Send http request to comment """
        all_data = []
        if self.login_status:
            comment_post = {'comment_text': comment_text}
            url_comment = self.url_comment % media_id
            try:
                comment = self.s.post(url_comment, data=comment_post)
                all_data = json.loads(comment.text)
                if all_data["status"] == "ok":
                    self.comments_counter += 1
                    self.comments_today += 1
                    log_string = 'Write: "%s". #%i.' % (comment_text,
                                                        self.comments_counter)
                    self.write_log(log_string)
            except:
                logging.exception("Except on comment!")
        print('Comment!!!')
        return all_data

    def follow(self, user_id):
        """ Send http request to follow """
        all_data = []
        if self.login_status:
            url_follow = self.url_follow % (user_id)
            try:
                follow = self.s.post(url_follow)
                all_data = json.loads(follow.text)
                if all_data["status"] == "ok":
                    self.follow_counter += 1
                    self.follows_today += 1
                    log_string = "Followed: %s #%i." % (user_id,
                                                        self.follow_counter)
                    self.write_log(log_string)
            except:
                logging.exception("Except on follow!")
        print('Follow!!!')
        return all_data

    def unfollow(self, user_id):
        """ Send http request to unfollow """
        all_data = []
        if self.login_status:
            url_unfollow = self.url_unfollow % user_id
            try:
                unfollow = self.s.post(url_unfollow)
                all_data = json.loads(unfollow.text)
                if all_data["status"] == "ok":
                    self.unfollow_counter += 1
                    self.unfollows_today += 1
                    log_string = "Unfollowed: %s #%i." % (user_id,
                                                          self.unfollow_counter)
                    self.write_log(log_string)
            except:
                logging.exception("Exept on unfollow!")
        return all_data

    def log_bot(self):
        print(self.username)
        media_uploads = []
        min_post = 4
        input_name = "photo"
        media_folder = 'media/'
        ext = '.jpg'
        mention = "@shopbraid"
        media = ''
        if os.path.exists('media.txt'):
            with open('media.txt') as f:
                user_posts = f.readline()
                try:
                    user_posts = int(user_posts)
                except:
                    user_posts = 0
        else:
            user_posts = 0
        if user_posts < min_post:
            min_post = min_post - user_posts
            while len(media_uploads) < min_post:
                while media in media_uploads or media == '':
                    media = media_folder + 'image' + str(randint(1, filesCount(media_folder, ext))) + ext
                media_comment = commentGen(randint(25, 30), 'hashtags', '')
                print(media + '\n')
                if self.upload_media(input_name, media, mention, media_comment):
                    media_uploads.append(media)
                    time.sleep(60)
            if self.change_profile_pix(input_name="profile_pic", filename="profilepic", file_address=media):
                with open('profile_pic.txt', 'wt') as f:
                    f.write('updated')
            with open('media.txt', 'wt') as f:
                f.write(str(len(media_uploads) + user_posts))
        line = ''
        try:
            with open('profile_pic.txt') as f:
                line = f.readline()
        except:
            if len(line) == 0 or line != "updated":
                media = media_folder + 'image' + str(randint(1, filesCount(media_folder, ext))) + ext
                if self.change_profile_pix(input_name="profile_pic", filename="profilepic", file_address=media):
                    with open('profile_pic.txt', 'wt') as f:
                        f.write('updated')

        sleep_before_actions = 20
        time.sleep(sleep_before_actions)
        print('Starting bot actions in ' + str(sleep_before_actions) + 'seconds')
        while self.keep_following:
            now = datetime.datetime.now()
            if (
                    datetime.time(self.start_at_h, self.start_at_m) <= now.time()
                    and now.time() <= datetime.time(self.end_at_h, self.end_at_m)
            ):
                # ------------------- Set Variables -------------------
                self.set_account_for_followers()
                self.set_accounts_to_follow()
				
                if(self.follows_today < self.follows_per_day and self.unfollows_today < self.unfollows_per_day):
                    # ------------------- FollowLike and Unfollow-------------------
                    self.auto_follow_like()
                    self.auto_unfollow()
                    time.sleep(self.action_sleep)
                elif(self.follows_today < self.follows_per_day):
                    # ------------------- Follow -------------------
                    self.auto_follow_like()
                    time.sleep(self.action_sleep)
                elif(self.unfollows_today < self.unfollows_per_day):
                    # ------------------- Unfollow -------------------
                    self.auto_unfollow()
                    time.sleep(self.action_sleep)
                else:
                    now_time_string = str(datetime.datetime.now().time())
                    now_time_string_format = "%H:%M:%S.%f"
                    now_time_obj = datetime.datetime.strptime(now_time_string, now_time_string_format)

                    end_time_string = str(datetime.time(self.end_at_h, self.end_at_m))
                    end_time_string_format = "%H:%M:%S"
                    end_time_obj = datetime.datetime.strptime(end_time_string, end_time_string_format)
                    pause_time = round((end_time_obj - now_time_obj).total_seconds())
                    time.sleep(pause_time)
                    self.follows_today = 0
                    self.unfollows_today = 0
                    self.likes_today = 0
                    self.comments_today = 0
            else:
                print("sleeping until {hour}:{min}".format(hour=self.start_at_h,
                                                           min=self.start_at_m), end="\r")
                self.bot_age += 1
                if self.bot_age == self.bot_life_span:
                    self.keep_following = False
                time.sleep(100)
                self.follows_today = 0
                self.unfollows_today = 0
                self.likes_today = 0
                self.comments_today = 0
            print("Follows Today: " + str(self.follows_today))
            print("Likes Today: " + str(self.likes_today))
            print("Unfollows Today: " + str(self.unfollows_today))
            print("Comments Today: " + str(self.comments_today))

    def auto_follow_like(self):
         account_to_follow = self.accounts_to_follow[0]
         self.follow_like(account_to_follow)
	
    def auto_unfollow(self):
         if len(self.account_followings) >= self.start_unfollowing_threshold:
             account_to_unfollow = self.account_followings[0]
             self.unfollow_like(account_to_unfollow)

    def set_account_for_followers(self):
        if self.account_for_followers == '' or len(self.accounts_to_follow) == 0:
            url_bot_av_acct = self.url_bot_av_acct
            try:
                r = self.s.get(url_bot_av_acct)
                all_data = json.loads(r.text)
                self.account_for_followers = all_data["account"]
                if self.blacklist_account_for_followers:
                    self.blacklisted_accounts.append(self.account_for_followers)
                print('Account_for_followers: '+self.account_for_followers)
                if self.account_for_followers != "":
                    self.end_cursor = all_data["last_cursor"]
                    try:
                        self.ping_next_cursor()
                    except:
                        print('self.ping_next_cursor() exception')
                else:
                    self.keep_following = False
                    print("@m - set_account_for_followers: No account found from server at address: "+self.url_bot_av_acct)
                    print(all_data["message"])
                return True
            except:
                print('Looks like the server is down or the network is bad!')
                server_down_times = 1
                server_alive = False
                while server_down_times < self.server_off_threshold and not server_alive:
                    pos_string = str(server_down_times + 1)
                    if pos_string[len(pos_string) - 1] == "1":
                        pos = pos_string+'st'
                    elif pos_string[len(pos_string) - 1] == "2":
                        pos = pos_string+'nd'
                    elif pos_string[len(pos_string) - 1] == "3":
                        pos = pos_string+'rd'
                    else:
                        pos = pos_string+'th'
                    server_alive = self.set_account_for_followers()
                    server_down_times += 1
                    print('Recalling the method "set_account_for_followers" the ' + pos + ' time in a minute')
                    time.sleep(60)
                if server_down_times >= self.server_off_threshold and not server_alive:
                    self.keep_following = False


    def ping_next_cursor(self):
        life_time_followings = 30 * self.follows_per_day
        chunk_size = 1000
        total_loops = round(life_time_followings / chunk_size)
        i = 0
        last_cursor = self.end_cursor
        ui = UserInfo()
        account_id = ui.get_user_id_by_login(self.account_for_followers)
        print('Total loops: '+str(total_loops))
        print(account_id)
        has_next_page = True
        while i < total_loops and has_next_page:
            juice = self.get_followers(self.account_for_followers, account_id, chunk_size, last_cursor)
            if 'message' in juice:
                print("Sleeping for rate limit(3 mins)...")
                time.sleep(180)
            else:
                followers = juice['data']['user']['edge_followed_by']['edges']
                for follower in followers:
                    username = follower['node']['username']
                    self.accounts_to_follow.append(username)
                has_next_page = juice['data']['user']['edge_followed_by']['page_info']['has_next_page']
                if has_next_page:
                    last_cursor = juice['data']['user']['edge_followed_by']['page_info']['end_cursor']
                else:
                    last_cursor = 'none'
                print(str(i)+'. Loop last cursor: '+last_cursor)
                i += 1
                time.sleep(5)
        print('Loops last cursor: ' + last_cursor)
        url_bot_av_acct_update = self.url_bot_av_acct_update
        payload = {
            "ut": "lc",
            "account": self.account_for_followers,
            "last_cursor": last_cursor,
        }
        r = self.s.get(url_bot_av_acct_update, params=payload)
        juice = r.text
        print(juice)
        #print('ACCOUNTS TO FOLLOW!!!')
        #print(self.accounts_to_follow)


    def get_followers(self, account, account_id, chunk_size, last_cursor):
        q_vars = self.query_vars2(account_id, chunk_size)
        if last_cursor != "" and last_cursor != "none" and last_cursor is not None:
            q_vars["after"] = last_cursor
        query_hash = self.get_query_hash(account)
        url_query = self.url_query % (query_hash, json.dumps(q_vars))
        r = self.s.get(url_query)
        all_data = json.loads(r.text)
        return all_data

    def set_accounts_to_follow(self):
         if(len(self.accounts_to_follow) == 0):
             account_for_followers = self.account_for_followers
             ui = UserInfo()
             user_id = ui.get_user_id_by_login(account_for_followers)
             query_hash = self.get_query_hash(account_for_followers)
             variables = self.query_vars2(user_id, self.query_first)
             if self.has_next_page and len(self.end_cursor) > 0:
                 variables["after"] = self.end_cursor
             if self.login_status:
                 url_query = self.url_query % (query_hash, json.dumps(variables))
                 try:
                     r = self.s.get(url_query)
                     all_data = json.loads(r.text)
                     self.has_next_page = all_data['data']['user']['edge_followed_by']['page_info']['has_next_page']
                     self.end_cursor = all_data['data']['user']['edge_followed_by']['page_info']['end_cursor']
                     followers = all_data['data']['user']['edge_followed_by']['edges']
                     for follower in followers:
                         username = follower['node']['username']
                         self.accounts_to_follow.append(username)
                 except:
                     logging.exception("Except on set_accounts_to_follow")
                     return False

			
    def get_query_hash(self, account):
         if not self.check_query_hash(self.query_hash):
             if self.login_status:
                 try:
                     i = 0
                     valid_hash = False
                     while (i < len(self.query_hash_scripts) and not valid_hash):
                         js_file_regex = self.query_hash_scripts[i]+'[a-z0-9]+\.js'
                         query_hash_regex = self.query_hash_regexes[i]
                         url_user = self.url_user % (account)
                         r = self.s.get(url_user)
                         mark_up = r.text
                         matches = re.findall(js_file_regex, mark_up)
                         script_addr = 'https://instagram.com'+matches[0]
                         script = self.s.get(script_addr)
                         script_src_code = script.text
                         hashes = re.findall(query_hash_regex, script_src_code)
                         #print(script_addr)
                         #print(query_hash_regex)
                         #print(hashes)
                         #print('\n-----')
                         if(len(hashes) == 0):
                             write_log('No hash Found in '+script_addr)
                             self.query_hash = ''
                         else:
                             for hash in hashes:
                                #print('hash - '+hash)
                                is_the_hash = self.check_query_hash(hash)
                                #print('Is the hash')
                                #print(is_the_hash)
                                if is_the_hash:
                                    self.query_hash = hash
                                    #print('HASH FOUND - '+hash)
                                    valid_hash = True
                                else:
                                    self.query_hash = ''
                                    #print('HASH NOT FOUND! - '+hash)
                         i += 1
                 except:
                     logging.exception('Exception on get_query_hash')

         return self.query_hash

    def check_query_hash(self, query_hash):
         id = self.query_hash_test_id
         first = 3
         query_vars = self.query_vars2(id, first)
         url_query = self.url_query % (query_hash, json.dumps(query_vars))
         r = self.s.get(url_query)
         #print(r.url)
         all_data = json.loads(r.text)
         #print('CHECK QUERY HASH ALL_DATA:')
         #print(all_data)
         if self.login_status:
             try:
                 #print(all_data)
                 if 'message' in all_data:
                     print(all_data['message'])
                     return False
                 else:
                     return True
             except:
                 logging.exception('Exception in check_query_hash')
                 return False

    def query_vars2(self, id, first):
         query_vars = {"id": id, "first": first}
         return query_vars


    def follow_like(self, account):
         user_data = self.get_user_data(account)
         user_id = user_data["user_id"]
         media_id = user_data["media_id"]
         media_count = user_data["media_count"]
         if self.login_status:
             try:
                 can_follow_like = self.can_follow_like(user_data)#return if we can perform actions on account
                 if(user_id not in self.account_followings and account not in self.blacklisted_accounts and can_follow_like):
                     follow = self.follow(user_id)
                     print(follow)
                     if follow["status"] == 'ok':
                         self.account_followings.append(user_id)
                         self.accounts_to_follow.remove(account)
                         if len(media_id) > 0:
                             if self.comments_today < self.comments_per_day:
                                 comment_text = commentGen(media_count, 'post_comment', '')
                                 comment = self.comment(media_id, comment_text)
                                 print(comment)
                             like = self.like(media_id)
                             print(like)
                             if like["status"] == 'ok':
                                 if like["status_code"] == 200:
                                     # Like, all ok!
                                     self.error_400 = 0
                                     log_string = "Liked: %s. Like #%i." % \
                                                  (media_id,
                                                   self.like_counter)
                                     self.write_log(log_string)
                                 elif like["status_code"] == 400:
                                     log_string = "Not liked: %i" \
                                                  % (like["status_code"])
                                     self.write_log(log_string)
                                     # Some error. If repeated - can be ban!
                                     if self.error_400 >= self.error_400_to_ban:
                                         # Look like you banned!
                                         time.sleep(self.ban_sleep_time)
                                     else:
                                         self.error_400 += 1
                                 else:
                                     log_string = "Not liked: %i" \
                                                  % (like["status_code"])
                                     self.write_log(log_string)
                                     return False
                     #Reset resources if we've followed the last followers of the account_for_followings
                     if len(self.accounts_to_follow) == 0:
                         self.end_cursor = ''
                         self.has_next_page = False
                         self.account_for_followers = ''
                 else:
                     self.accounts_to_follow.remove(account)
             except:
                 logging.exception('Exception on follow_like - '+account)
	
    def unfollow_like(self, user_id):
         if user_id in self.account_followings:
             unfollow = self.unfollow(user_id)
             if unfollow['status'] == 'ok':
                 self.account_followings.remove(user_id)
				
    def get_user_data(self, account):
         url_user_detail = self.url_user_detail % account
         r = self.s.get(url_user_detail)
         all_data = json.loads(r.text)
         user_id = all_data['user']['id']
         is_private = all_data['user']['is_private']
         is_verified = all_data['user']['is_verified']
         has_blocked_viewer = all_data['user']['has_blocked_viewer']
         followed_by_viewer = all_data['user']['followed_by_viewer']
         biography = all_data['user']['biography']
         media_count = all_data['user']['media']['count']
         followers_count = all_data['user']['followed_by']['count']
         followings_count = all_data['user']['follows']['count']
         print(all_data)
         if media_count > 0 and len(all_data['user']['media']['nodes']) > 0:
             media_id = all_data['user']['media']['nodes'][0]['id']
             media_likes = all_data['user']['media']['nodes'][0]['edge_media_preview_like']['count']
         else:
             media_id = False
             media_likes = 0
         return_value = {
             'is_private': is_private,
             'has_blocked_viewer': has_blocked_viewer,
             'is_verified': is_verified,
             'followed_by_viewer': followed_by_viewer,
             'user_id': user_id,
             'followers_count': followers_count,
             'followings_count': followings_count,
             'biography': biography,
             'media_count': media_count,
             'media_likes': media_likes,
             'media_id': media_id
         }
         return return_value

    def can_follow_like(self, user_data):
        is_private = user_data['is_private']
        has_blocked_viewer = user_data['has_blocked_viewer']
        is_verified = user_data['is_verified']
        followers_count = user_data['followers_count']
        followings_count = user_data['followings_count']
        biography = user_data['biography']
        media_count = user_data['media_count']
        media_likes = user_data['media_likes']
        followed_by_viewer = user_data['followed_by_viewer']

        can_follow_like = True
        if is_private or has_blocked_viewer or followed_by_viewer:
            can_follow_like = False
        if media_count < self.min_media_count or followers_count < self.min_followers_count or followings_count < self.min_followings_count:
            can_follow_like = False
        if followings_count / followers_count > self.min_followings_to_followes_ratio:
            can_follow_like = False
        return can_follow_like

    def write_log(self, log_text):
        """ Write log by print() or logger """

        if self.log_mod == 0:
            try:
                now_time = datetime.datetime.now()
                print(now_time.strftime("%d.%m.%Y_%H:%M")  + " " + log_text)
            except UnicodeEncodeError:
                print("Your text has unicode problem!")
        elif self.log_mod == 1:
            # Create log_file if not exist.
            if self.log_file == 0:
                self.log_file = 1
                now_time = datetime.datetime.now()
                self.log_full_path = '%s%s_%s.log' % (
                    self.log_file_path, self.user_login,
                    now_time.strftime("%d.%m.%Y_%H:%M"))
                formatter = logging.Formatter('%(asctime)s - %(name)s '
                                              '- %(message)s')
                self.logger = logging.getLogger(self.user_login)
                self.hdrl = logging.FileHandler(self.log_full_path, mode='w')
                self.hdrl.setFormatter(formatter)
                self.logger.setLevel(level=logging.INFO)
                self.logger.addHandler(self.hdrl)
            # Log to log file.
            try:
                self.logger.info(log_text)
            except UnicodeEncodeError:
                print("Your text has unicode problem!")
