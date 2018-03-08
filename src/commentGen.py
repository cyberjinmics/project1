#!/usr/bin/env python
# -*- coding: utf-8 -*-


from random import *
import random

min_tags = 3
emojis = [u'🚀', u'🚅', u'🌅', u'🎆', u'🎁', u'🎇', u'🌈', u'🚎']
comment_string = 'I %s your %s. This is... %s'
loves = ['love', 'like', 'admire']
post_names = ['photos', 'pictures', 'pics', 'shots', 'snapshots']
exclamations = [u'WOW! 😤', u'hmmmmmm 😒', u'Shaking my head 😡']

comment = ''
def commentGen(tags_count, caption, mention):
    media_count = tags_count
    if tags_count < min_tags:
        tags_count = min_tags

    adjectives = [
        "5_Speed", "Easy_Drive", "Highgility", "Scientific", "6_Speed", "Economical", "Hybrid", "Sleek",
        "Acclaimed", "Effective", "Innovative", "Fasthorse", "Advanced", "Electric", "Legendary", "Speedy",
        "Affordable", "Elegant", "Limitless", "Sporty", "Agile", "Engineered", "Low_emission", "Standard",
        "All_wheels", "Enhanced", "Luxurious", "Stylish", "Astonishing", "Luxury", "Top_dollar", "Automatic",
        "Ergonomic", "Low_dollar", "Top_level", "Automotive", "Cheapies", "Tuned", "Beyond_Compare", "Extreme",
        "Exotic", "Ultimate", "Classic", "Noteworthy", "Ultraspeed", "Crash_tested", "Fast_wheels", "Carformance",
        "Unparalled", "Custom_built", "Fastrack", "Drivepoint", "Custom_designed", "Four_wheels", "Powerful",
        "Versatile", "Customized", "Front_wheel", "Progressive", "Vintage", "Distinctive", "Fuel_efficient",
        "Quick_shifting", "Drivetrain", "Ready_to_cruise", "Drivel", "Functional", "Reinforced"
    ]

    hashtags = [
        '#cars ', '#love ', '#auto ', '#bmw ', '#instagood ', '#instacar ', '#luxury ', '#speed ', '#follow ',
        '#supercar ', '#race ', '#like4like ', '#drive ', '#racing ', '#carswithoutlimits ', '#followme ', '#audi ',
        '#sportscar ', '#mercedes ', '#ferrari ', '#road ', '#beautiful ', '#picoftheday ', '#photooftheday ',
        '#wheels ', '#street ', '#ford ', '#carsofinstagram ', '#jdm ', '#exotic ', '#turbo ', '#amazing ',
        '#lamborghini ', '#instacars ', '#like ', '#fast ', '#vehicle ', '#instalike ', '#ride ', '#engine ',
        '#porsche ', '#style ', '#happy ', '#classic ', '#exoticcars ', '#stance ', '#black ', '#cool ',
        '#jdm', '#bugatti ', '#speedsuspects ', '#evox ', '#evo ', '#misubishi ', '#subie ', '#wrc ', '#subaru ',
        '#wrx ', '#rally ', '#drift ', '#track', '#volkswagenbeetle ', '#vdubclub ', '#carstagram ', '#vwmafia ',
        '#vwbeetle ', '#beetle ', '#oldvwclub ', '#instabeetle ', '#oldschoolvw ', '#static ', '#vintage ',
        '#wolfsburg ', '#oldvw ', '#aircooled ', '#vwlifestyle ', '#vwstance ', '#germancars ', '#m4 ', '#gmg ',
        '#gmggarage ', '#opss ', '#araba ', '#sakarya ', '#woswogen ', '#golf ', '#istanbul ', '#kayseri ',
        '#konya', '#madwhips ', '#wheelsonfire ', '#thesupercarsquad ', '#s550mustang ', '#fordmustang ',
        '#mustanggt ', '#l4l ', '#f4f ', '#s4s ', '#red ', '#pony ', '#torque ', '#amazingcars ', '#fastcar ', '#pa ',
        '#aston ', '#chestercounty ', '#westchester ', '#trucks ', '#carsforsale ', '#buyherepayhere ', '#autos ',
        '#philly', '#instagram ', '#horsepower ', '#beastmode ', '#foxbody ', '#cobra ', '#svt ',
        '#racecar ', '#performance ', '#truth ', '#fordracing ', '#saleen ', '#roush ', '#shelby ', '#american ',
        '#americanmuscle ', '#fastback ', '#stanggang ', '#stang ', '#coyote ', '#mustang ', '#muscle ', '#terminator ',
        '#musclecars ', '#musclecar ', '#mustangcobra', '#gtr ', '#godzilla ', '#skyline ', '#r35 ', '#r34 ', '#r33 ',
        '#r32 ', '#gt ', '#ams ', '#alpha ', '#skylinegtr ', '#sky ', '#rb26 ', '#japan ', '#car ', '#nismo ',
        '#nissanin ', '#pagani ', '#huayra ', '#bc ', '#huayrabc ', '#purple ', '#carbon ', '#rare ', '#uk ',
        '#london ', '#photooftheday'
    ]

    if caption == 'hashtags':
        comment = " ".join(sample(hashtags, tags_count))
    elif caption == 'caption':
        comment = 'Shopbraid ' + random.choice(adjectives).replace('_', ' ') + ' cars ' + mention + ' '
        comment = comment + random.choice(emojis)
    elif caption == 'post_comment':
        post_name = random.choice(post_names)
        if media_count == 1:
            post_name = post_name[:len(post_name) - 1]
        comment = comment_string % (random.choice(loves), post_name, random.choice(exclamations))
    return comment
