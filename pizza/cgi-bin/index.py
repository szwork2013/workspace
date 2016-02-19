#!/usr/bin/env python3.4
from os import path
from simplemapper import BaseMapper
from simpletemplate import SimpleTemplate
from model import UserMapper, PizzaMapper, OrderMapper, OrderPizzaMapper
from http.cookies import SimpleCookie
import auth, cart_manager

import cgi
form = cgi.FieldStorage()
(username, cookie, error_message) = auth.login(form)

login_status = False
anonymous = True
if username:
    login_status = True
    anonymous = False

print("Content-type: text/html")
if cookie:
    print(cookie.output())

(cart_count, msize_carts, lsize_carts, cookie) = cart_manager.check_cart(form)

if cookie:
    print(cookie.output())

print()  # HTTPヘッダ終了

#userid = form.getvalue('user', '')
#password = form.getvalue('pass', '')

import sqlite3
conn = sqlite3.connect('cgi-bin/pizza.db')
PizzaMapper.setconnection(conn)

pizzas = list(PizzaMapper.select())
for i, pizza in enumerate(pizzas):
    pizza.clearfix_xs = False
    pizza.clearfix_sm = False
    pizza.clearfix_md = False
    if (i+1) % 2 == 0: pizza.clearfix_xs = True
    if (i+1) % 3 == 0: pizza.clearfix_sm = True
    if (i+1) % 4 == 0: pizza.clearfix_md = True
    if pizza.sauce == u'ホワイトソース':
        pizza.sauce_color = 'label-warning'
    elif pizza.sauce == u'黒コショウマヨネーズソース':
        pizza.sauce_color = 'label-default'
    elif pizza.sauce == u'特製バジルソース':
        pizza.sauce_color = 'label-success'
    elif pizza.sauce == u'南蛮ソース':
        pizza.sauce_color = 'label-info'
    else:
        pizza.sauce_color = 'label-danger'
    pizza.cart_count_msize = 0
    if pizza.id in msize_carts: pizza.cart_count_msize = msize_carts[pizza.id]
    pizza.cart_count_lsize = 0
    if pizza.id in lsize_carts: pizza.cart_count_lsize = lsize_carts[pizza.id]

value_dic = {
    'nav_index': True,
    'nav_cart': False,
    'nav_history': False,
    'pizzas': pizzas,
    'login_error': error_message,
    'username': username,
    'login': login_status,
    'anonymous': anonymous,
    'cart_count': cart_count,
}

html = u''
filenames = ['head.html', 'nav.html', 'index.html', 'foot.html']
for fname in filenames:
    p = path.join(path.dirname(__file__), '../templates', fname)
    t = SimpleTemplate(file_path=p)
    html += t.render(value_dic)

print(html)
