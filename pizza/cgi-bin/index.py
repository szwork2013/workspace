#! /Users/yuta/.pyenv/versions/3.4.1/bin/python3.4
# coding: utf-8

from os import path
from simplemapper import BaseMapper
from simpletemplate import SimpleTemplate
from model import UserMapper, PizzaMapper, OrderMapper, OrderPizzaMapper
# import sys
# reload(sys)
# sys.setdefaultencoding('utf8')
import login

(username,cookie,error_message)=login.login()

print("Content-type: text/html")
import cgi
form = cgi.FieldStorage()
userid = form.getvalue('userid', '')
password = form.getvalue('password', '')

import sqlite3

#login.login()

conn = sqlite3.connect('cgi-bin/pizza.db')
PizzaMapper.setconnection(conn)
print(PizzaMapper);
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
#     if pizza.id in self.msize_carts: pizza.cart_count_msize = self.msize_carts[pizza.id]
    pizza.cart_count_lsize = 0
#     if pizza.id in self.lsize_carts: pizza.cart_count_lsize = self.lsize_carts[pizza.id]

value_dic = {
    'nav_index': True,
    'nav_cart': False,
    'nav_history': False,
    'pizzas': pizzas,
    'login_error': False,
    'username': '',
    'login': False,
    'anonymous': True,
    'cart_count': 0,
}

html = u''
filenames = ['head.html','head.html', 'nav.html', 'index.html', 'foot.html']
for fname in filenames:
    p = path.join(path.dirname(__file__), '../templates', fname)
    t = SimpleTemplate(file_path=p)
    html += t.render(value_dic)

print(html)
