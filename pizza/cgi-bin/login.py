#! /Users/yuta/.pyenv/versions/3.4.1/bin/python3.4
# coding: utf-8

import sqlite3
import cgi
from http.cookies import SimpleCookie
#from os import path
#from simplemapper import BaseMapper
#from simpletemplate import SimpleTemplate
from model import UserMapper, PizzaMapper, OrderMapper, OrderPizzaMapper
import uuid
import datetime
import os



def login():
    conn = sqlite3.connect('cgi-bin/pizza.db')
    UserMapper.setconnection(conn)
    print(UserMapper);

    form = cgi.FieldStorage()
    userid=form.getvalue('user','')
    password=form.getvalue('pass','')

    username=None
    cookie=None
    error_message=None

    u=list(UserMapper.select(username=userid,password=password))
    if len(u)==1:
        username=u[0].username
        u[0].session=str(uuid.uuid4())
        u[0].session_expire=datetime.datetime.utnow()+datetime.timedelta(days=15)
        u[0].update()
        cookie=SimpleCookie()
        cookie['session']=u[0].session
        cookie['session']['path']='/'
        cookie['session']['expires']=u[0].session_expire.strftime('%a, %d-%b-%Y %H:%M:%S GMT')
    if not username:
        if userid or password:
            self.login_error='ユーザ名またはパスワードが違います。'
        else:
            c=SimpleCookie()
            c.load(os.environ.get('HTTP_COOKIE',''))
            if 'session' in c:
                u=list(UserMapper.select(session=c['session'].value))
                if len(u)==1:
                    username=u[0].username
    return (username,cookie,error_message)


"""
    #Users = list(UserMapper.select())
    #print(Users);


    form=cgi.FieldStorage()
    print ("Content-type: text/html")
    userid = form.getvalue('user','')
    password = form.getvalue('pass','')

    c=SimpleCookie()

    return (None,None,None)
"""



