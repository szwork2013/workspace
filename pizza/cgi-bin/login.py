#! /Users/yuta/.pyenv/shims/python3
# coding: utf-8

import sqlite3
import cgi
from http.cookies import SimpleCookie
#from os import path
#from simplemapper import BaseMapper
#from simpletemplate import SimpleTemplate
from model import UserMapper, PizzaMapper, OrderMapper, OrderPizzaMapper
import uuid


def login():
    conn = sqlite3.connect('cgi-bin/pizza.db')
    UserMapper.setconnection(conn)
    print(UserMapper);

    #Users = list(UserMapper.select())
    #print(Users);


    form=cgi.FieldStorage()
    print ("Content-type: text/html")
    userid = form.getvalue('user','')
    password = form.getvalue('pass','')

    c=SimpleCookie()

    return (None,None,None)



