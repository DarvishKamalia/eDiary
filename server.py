from bottle import route, run, template, request, redirect, static_file
import db

# static files (like CSS, fonts, pictures)
@route('/static/<filepath:path>')
def static(filepath):
	return static_file(filepath, './static')

# homepage
@route('/home')
def home():
	data = {'entries' : db.getEntries()}
	return template('home', data) 

# log a new entry
@route('/log', method='POST')
def log():
	entry = db.makeEntry(request.forms['entry'])
	db.logEntry(entry)
	redirect('/home')

# erase an old entry
@route('/erase/<id>')
def erase(id):
	db.eraseEntry(id)
	redirect('/home')

run(reloader=True)
