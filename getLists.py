import sys
import os
import django

from time import sleep
import random


sys.path.append('/var/www/server/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'server.settings'
django.setup()


from socialpost.models import *
#from keys import ifttt_key

import tweepy
from pprint import pprint as ppr

import csv

print(sys.argv)
tname = sys.argv[1]
t_user = TweetUser.objects.filter(handle=tname)[0]
print(t_user)

auth = tweepy.OAuthHandler(t_user.token, t_user.token_key)
auth.set_access_token(t_user.secret, t_user.secret_key)

api = tweepy.API(auth)


userLists = api.lists(tname)

for ul in userLists:
    members = api.list_members(tname, newList.id)
    memberList = []
    for member in members['users']:
        memberList.append(member.screen_name)
    tMemberList = ', '.join(memberList)
    TweetList.create(owner=t_user, name=ul.full_name, handle_list=tMemberList)

# Choose User

  

