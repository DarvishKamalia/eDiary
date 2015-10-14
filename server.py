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
	global name
	if name == "":
		redirect('/signin')
	else:
		data = {'entries' : db.loadEntries(), 'feelings' : db.loadFeelings(), 'name' : name}
		return template('home', data)

# signin
@route('/signin')
def signin():
	return template('signin', {})

# signin POST
@route('/signin', method='POST')
def signin_post():
	global name
	if request.forms['name'] == "":
		redirect('/signin')
	else:
		name = request.forms['name']
		redirect('/home')

# signout
@route('/signout')
def signout():
	global name
	name = ""
	redirect('/signin')

# log a new entry
@route('/log', method='POST')
def log():
	text = request.forms['text']
	feel = request.forms['feel']
	if text == '':
		redirect('/home')
	else:
		entry = db.newEntry(text, feel)
		entries = db.loadEntries()
		entries.insert(0, entry)
		db.storeEntries(entries)
		redirect('/home')

# erase an old entry
@route('/erase/<id>')
def erase(id):
	entries = db.loadEntries()
	i = 0
	while i < len(entries):
		if id == entries[i]['id']:
			del entries[i]
			break
		i = i + 1
	db.storeEntries(entries)
	redirect('/home')

run(reloader=True, debug=True)
