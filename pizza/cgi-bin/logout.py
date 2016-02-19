#!/usr/bin/env python3.4
from os import path
from simplemapper import BaseMapper
from simpletemplate import SimpleTemplate
from model import UserMapper, PizzaMapper, OrderMapper, OrderPizzaMapper
from http.cookies import SimpleCookie
import auth

cookie = auth.logout()

print("Content-type: text/html")
if cookie:
    print(cookie.output())
print('')  # HTTPヘッダ終了

html = u'''<html>
<head><meta http-equiv="refresh" content="0;URL=/cgi-bin/index.py"></head>
<body>Logout! <a href="/cgi-bin/index.py">Go to top page...</a></body>
</html>
'''

print(html)
