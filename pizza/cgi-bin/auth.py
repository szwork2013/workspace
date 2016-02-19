import sqlite3, uuid, datetime, os, cgi
from http.cookies import SimpleCookie
from model import UserMapper

conn = sqlite3.connect('cgi-bin/pizza.db')
UserMapper.setconnection(conn)

def login(form):
    userid = form.getvalue('user', '')
    password = form.getvalue('pass', '')
    
    username = None
    cookie = None
    error_message = None
    
    u = list(UserMapper.select(username=userid, password=password))
    if len(u) == 1:
        username = u[0].username
        u[0].session = str(uuid.uuid4())    # 念のために重複チェックした方がいいかも
        u[0].session_expire = datetime.datetime.utcnow() + datetime.timedelta(days=15)
        u[0].update()
        cookie = SimpleCookie()
        cookie['session'] = u[0].session
        cookie['session']['path'] = '/'
        cookie['session']['expires'] = u[0].session_expire.strftime('%a, %d-%b-%Y %H:%M:%S GMT')
    if not username:
        if userid or password:
            error_message = 'ユーザ名またはパスワードが違います。'
        else:
            c = SimpleCookie()
            c.load(os.environ.get('HTTP_COOKIE', ''))
            if 'session' in c:
                u = list(UserMapper.select(session=c['session'].value))
                if len(u) == 1:
                    username = u[0].username
    return (username, cookie, error_message)

def logout():
    cookie = SimpleCookie()
    cookie.load(os.environ.get('HTTP_COOKIE', ''))
    if 'session' in cookie:
        u = list(UserMapper.select(session=cookie['session'].value))
        if len(u) == 1:
            u[0].session = None
            u[0].session_expire = None
            u[0].update()
            expire = datetime.datetime.utcnow() + datetime.timedelta(days=-1)
            cookie['session']['expires'] = expire.strftime('%a, %d-%b-%Y %H:%M:%S GMT')
            return cookie
    return None
