#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
"""

from pixivpy3 import *
import json
import pprint
import re

#def pp(obj):
#	json.dumps(obj,ensure_ascii=False,indent=2)

"""
関数名:pp()
概要:日本語をPrettyPrintする
引数:obj…配列
戻り値:
例外:
備考:http://www.nltk.org/book-jp/ch12.htmlよりコピペ
"""
def pp(obj):
    pp = pprint.PrettyPrinter(indent=4, width=160)
    str = pp.pformat(obj)
    return re.sub(r"\\u([0-9a-f]{4})", lambda x: unichr(int("0x"+x.group(1),
                                                            16)), str)

api = PixivAPI()
api.login("umai-koreippon", "crfyk1988")

print "-------------------------------"
print "works"
print "-------------------------------"
# 作品详细 PAPI.works
json_result = api.works(46363414)
print json.dumps(json_result,ensure_ascii=False,indent=2)
illust = json_result.response[0]
print( ">>> %s, origin url: %s" % (illust.caption, illust.image_urls['large']))


print "-------------------------------"
print "users"
print "-------------------------------"
# 用户资料 PAPI.users
json_result = api.users(1184799)
print pp(json_result)
user = json_result.response[0]
print(user.profile.introduction)

# 我的订阅 PAPI.me_feeds
#json_result = api.me_feeds(show_r18=0)
#print(json_result)
#ref_work = json_result.response[0].ref_work
#print(ref_work.title)
"""
print "-------------------------------"
print "users_works"
print "-------------------------------"
# 用户作品 PAPI.users_works
json_result = api.users_works(1184799)
print pp(json_result)
illust = json_result.response[0]
print(">>> %s, origin url: %s" % (illust.caption, illust.image_urls['large']))

print "-------------------------------"
print "users_favorite_works"
print "-------------------------------"
# 用户收藏 PAPI.users_favorite_works
json_result = api.users_favorite_works(1184799)
print pp(json_result)
illust = json_result.response[0].work
print(">>> %s origin url: %s" % (illust.caption, illust.image_urls['large']))

print "-------------------------------"
print "me_favorite_works"
print "-------------------------------"
# 获取收藏夹 PAPI.me_favorite_works
#json_result = api.me_favorite_works()
#print(json_result)
#ids = json_result.response[0].id
"""
"""
print "-------------------------------"
print "me_favorite_works_add"
print "-------------------------------"
# 添加收藏 PAPI.me_favorite_works_add
json_result = api.me_favorite_works_add(46363414)
print(json_result)

print "-------------------------------"
print "me_favorite_works_delete"
print "-------------------------------"
# 删除收藏 PAPI.me_favorite_works_delete
json_result = api.me_favorite_works_delete(ids)
print(json_result)

print "-------------------------------"
print "me_favorite_users_follow"
print "-------------------------------"
# 关注用户 PAPI.me_favorite_users_follow
json_result = api.me_favorite_users_follow(1184799)
print(json_result)

print "-------------------------------"
print "ranking_all weekly"
print "-------------------------------"
# 排行榜 PAPI.ranking_all
json_result = api.ranking_all('weekly', 1)
print(json_result)
illust = json_result.response[0].works[0].work
print(">>> %s origin url: %s" % (illust.title, illust.image_urls['large']))

print "-------------------------------"
print "ranking_all daily"
print "-------------------------------"
# 过去排行榜 PAPI.ranking_all(2015-05-01)
json_result = api.ranking_all(mode='daily', page=1, date='2015-05-01')
print(json_result)
illust = json_result.response[0].works[0].work
print(">>> %s origin url: %s" % (illust.title, illust.image_urls['large']))

"""

print "-------------------------------"
print "search_works"
print "-------------------------------"
# 标题(text)/标签(exact_tag)搜索 PAPI.search_works
#json_result = api.search_works("五航戦 姉妹", page=1, mode='text')
#mode exact_tag?
#数は自動で30抜き出されてる
json_result = api.search_works(u"ざくざくアクターズ", page=1, mode='tag',sort="date")
json_result2 = api.search_works(u"ざくざくアクターズ", page=2, mode='tag',sort="date")
print pp(json_result)
print "-------------------------------"
print "search_works2"
print "-------------------------------"
print pp(json_result2)
illust = json_result.response[0]
print(">>> %s origin url: %s" % (illust.title, illust.image_urls['large']))
