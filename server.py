# not important, this just tells Python to avoid generating .pyc files
import sys
sys.dont_write_bytecode = True

# imports, only necessary stuff from bottle
from bottle import route, run, template, request, redirect, static_file
import db

# logged in name
name = ""

# static files, like CSS, fonts, images
@route('/static/<filepath:path>')
def static(filepath):
	return static_file(filepath, 'static')

# homepage
@route('/home')
def home():
	return template('home', {})

# signin
@route('/signin')
def signin():
	return template('signin', {})

# signin POST
@route('/signin', method='POST')
def signin_post():
	redirect('/home')

# signout
@route('/signout')
def signout():
	redirect('/signin')

# log a new entry
@route('/log', method='POST')
def log():
	redirect('/home')

# erase an old entry
@route('/erase/<id>')
def erase(id):
	redirect('/home')

run(reloader=True, debug=True)
