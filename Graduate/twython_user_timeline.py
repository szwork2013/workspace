#! /usr/bin/env python
# -*- coding:utf-8 -*-

from twitter import *
from twython import Twython,TwythonError

config={}
execfile("config.py",config)

api = twython.setup(authtype="Basic", username="ykmilab", password="crfyk1988")
twitter = Twython(app_key="consumer_key",                      # ここらにそれぞれ
                  app_secret="consumer_secret",                # developer でメモった
                  oauth_token="access_key",                  # key を入力すると
                  oauth_token_secret="access_secret")    # 認証されるっぽい。

try:
    user_timeline = twitter.get_user_timeline(screen_name='BarackObama', count=30) # オバマ大統領のアカウントを30tweet取得する。
except TwythonError as e:
    print e

for tweet in user_timeline:
    print tweet['text'] + "\n"