#! /usr/bin/env python
# -*- coding:utf-8 -*-

from twitter import *
import time
import calendar

def YmdHMS(created_at):
    time_utc=time.strptime(created_at,'%a %b %d %H:%M:%S +0000 %Y')
    unix_time=calendar.timegm(time_utc)
    time_local=time.localtime(unix_time)
    return time.strftime("%Y:%m:%d:%H:%M:%S",time_local)

config={}
execfile("config.py",config)

twitter=Twitter(
    auth=OAuth(config["access_key"],config["access_secret"],config["consumer_key"],config["consumer_secret"]))

user = "mazeran56"

results=twitter.statuses.user_timeline(count=200,screen_name=user)
count_loop=0
for status in results :
    print "(%s)%s" % (status["created_at"],status["text"])
    count_loop+=1
    id_last=status["id"]

for i in range(0,10):
    results=twitter.statuses.user_timeline(count=200,screen_name=user,max_id=id_last)
    count_loop=0
    for status in results :
        print "(%s)%s" % (YmdHMS(status["created_at"]),status["text"])
        count_loop+=1
        id_last=status["id"]

