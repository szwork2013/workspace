#!/usr/bin/env python3.4
from os import path
from simplemapper import BaseMapper
from simpletemplate import SimpleTemplate
from model import UserMapper
from http.cookies import SimpleCookie
import auth
import html

import cgi
form = cgi.FieldStorage()
userid = form.getvalue('userid', '')
email = form.getvalue('mail', '')
password1 = form.getvalue('pass1', '')
password2 = form.getvalue('pass2', '')

print("Content-type: text/html")
print('')

confirm = False
formview = False
if userid and email and password1 and password2:
    confirm = True
else:
    formview = True

value_dic = {
    'nav_index': True,
    'nav_cart': False,
    'userid': html.escape(userid),
    'email': html.escape(email),
    'password1': password1,
    'password2': password2,
    'confirm': confirm,
    'formview': formview,
}
html = u''
filenames = ['head.html', 'signup.html', 'foot.html']
for fname in filenames:
    p = path.join(path.dirname(__file__), '../templates', fname)
    t = SimpleTemplate(file_path=p)
    html += t.render(value_dic)

print(html)
