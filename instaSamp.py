#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

from src import InstaBot
from src.usernameGen import usernameGen
from src.commentGen import commentGen
from src.filesCount import filesCount
from random import *
import random
import os

bot = InstaBot()

##### Set Variables #####
######### Signup Form Data #########
bot.username = usernameGen(5, True)
bot.email = bot.username+'@gmail.com'
bot.first_name = bot.username.replace("_", " ").title()
bot.signup_password = 'b@tinlo18'

bot.user_login = bot.username
bot.user_password = 'b@tinlo18'
##### clean Variables #####
bot.clean_vars()
#### Signup or Login####
#check if there is no signup already
if os.path.exists('username.txt'):
    with open('username.txt') as f:
        user_signed = f.readline()
        if len(user_signed) == 0:
            bot.signup()
        else:
            bot.user_login = user_signed
            bot.username = bot.user_login
            bot.login()
else:
    bot.signup()
bot.log_bot()