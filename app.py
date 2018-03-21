from bottle import *

'''
@route('/')
def index():
    if request.get_cookie('hello'):
        return "Hello again"
    else:
        response.set_cookie('hello', 'world')
        return 'Hello World'
'''

adminuser = 'admin'
adminpwd = 'password'

@route('/')
def index():
    return template('index')

@route('/login')
def login():
    return template('login')

@route('/login', method='post')
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    if username == adminuser and password == adminpwd:
        response.set_cookie('account', username)
        return redirect('/restricted')
    else:
        return "Login failed. <br> <a href='/login'>Login</a>'"

@route('/restricted')
def restricted():
    user = request.get_cookie('account')
    print(user)
    return "Restricted area"

run()