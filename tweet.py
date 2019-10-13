import sys
import os
import django

from time import sleep
import random


sys.path.append('/var/www/server/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'server.settings'
django.setup()


from socialpost.models import *
from keys import cc_ifttt_key

import tweepy
from pprint import pprint as ppr

import csv

def renewCopies():
    all_db_copies = TweetCopy.objects.filter(tweeter__pk=t_user.id, link__published=True, published=True, running=False)
    for adc in all_db_copies:
        adc.running = True
        adc.save()


def getCopies():
    all_db_copies = TweetCopy.objects.filter(tweeter__pk=t_user.id, published=True, running=True, link__published=True)
    selected_db_copies = random.sample(set(all_db_copies), 1)
    return selected_db_copies


# Random number to decide if it runs
numnum = random.randint(0,12)
if numnum < 4:
    quit()


# print(sys.argv)
tname = sys.argv[1]
t_user = TweetUser.objects.filter(handle=tname)[0]
# print(t_user)

auth = tweepy.OAuthHandler(t_user.token, t_user.token_key)
auth.set_access_token(t_user.secret, t_user.secret_key)
api = tweepy.API(auth)

# Choose User
# Parameterize via CLI
tname = sys.argv[1]
t_user = TweetUser.objects.filter(handle=tname)[0]
# print(t_uuser.id)


# Choose TweetCopy
# Pick Random 3

try:
    selected_db_copies = getCopies()
except:
    renewCopies()
    selected_db_copies = getCopies()


# Delay Start time
start_time = random.randint(450,2100)
#start_time = random.randint(0,3)
print(start_time)
sleep(start_time)

# If list of at-handles is less than 3
# Renew the list



def renewList(tweetList):
    uhandles = tweetList.used_handles.split(',')
    handleList = tweetList.handle_list.split(',')
    compList = uhandles + handleList
    tweetList.handle_list = (', ').join(compList)
    tweetList.save()


# Get at-handle from the List

def checkList(tweetCopy):
    try:
        hList = TweetList.object.filter(id=tweetCopy.hList_id)
        handleList = hList.handle_list.split(',')
        if handleList > 2:
            handle = handleList.pop(random.randint(0,len(handleList - 1)))
            uhandles = hList.used_handles.split(',')
            uhandles.append(handle)
            uhandles = ', '.join(uhandles)
            hList.used_handles = uhandles
            hList.save()
            if handleList > 2:
                renewList(hList)
        else:
            renewList(hList)
            handle = checkList(tweetCopy)
    except:
        handle = None
    return handle

# Tweet Text

def tweetText(tweetCopy, listed):
    if listed == True:
        handle = checkList(tweetCopy)
        if handle != None:
            textCopy = copy.copy_text
            tweetText = textCopy.format(handle)
            print(tweetText)
            finalText = tweetText + ' ' + copy.link.link
    else:
        finalText = tweetCopy.copy_text + ' ' + tweetCopy.link.link
    tweetCopy.running = False
    tweetCopy.save()
    return finalText


def tweetImage(tweetCopy):
    images = tweetCopy.link.tweet_pics__all
    img_ids = []
    for i in images:
        img_ids.append(i.twt_media_id)
  
def postToFb(tweetCopy):
    if t_copy.facebook == True:
        r = {}
        r['value1'] = complete_text
        if 'CultureClap' in tweetCopy.facebook:
            ifttt_url = "https://maker.ifttt.com/trigger/facebook_base/with/key/" + cc_ifttt_key
        # if 'idioke' in tweetCopy.facebook:
        #     ifttt_url = "https://maker.ifttt.com/trigger/facebook_base/with/key/" + ifttt_key



for copy in selected_db_copies:
    pause = random.randint(244,2044)
    sleep(pause)
    if copy.hList == None:
        complete_text = tweetText(copy, False)
    elif copy.hlist != None:
        complete_text = tweetText(copy, True)
    else:
        complete_text = tweetText(copy, False)
    # Twitter
    try:
        ppr(complete_text)
        tweet = api.update_status(complete_text)
    except Exception as e:
        copy.copy_text = copy.copy_text + ' DOES NOT WORK ' + e
        copy.published = False
        copy.save()


    # if copy.rt_id != None:
    #     try:
    #         api.retweet(copy.rt_id)
    #     except:
    #         try:
    #             complete_text = copy.copy_text + ' ' + copy.link.link
    #             tweet = api.update_status(complete_text)
    #             copy.rt_id = None
    #             copy.save()
    #         except:
    #             copy.copy_text = copy.copy_text + ' DOES NOT WORK'
    #             copy.published = False
    #             copy.save()  
    # else:


	

# THIS FEATURE ENDS MARCH 1ST
# if t_copy.linkedin == True:
# 	ifttt_url = "https://maker.ifttt.com/trigger/linkedin_update/with/key/" + ifttt_key
# 	r = {}
# 	r['value1'] = complete_text
# 	r['value2'] = t_copy.link.link
