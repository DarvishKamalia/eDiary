from bottle import route, run, template, static_file, request, redirect
from entry import Entry

entries = [Entry('parth'), Entry('mehta')]

def getEntries():
	return entries

def logEntry(text):
	entries.append(Entry(text))

def eraseEntry(id):
	i = 0
	while i < len(entries):
		if id == entries[i].id:
			del entries[i]
			return
		i += 1

# static files (like CSS, fonts, pictures)
@route('/static/<filepath:path>')
def static(filepath):
	return static_file(filepath, './static')

# homepage
@route('/home')
def home():
	data = {'entries' : getEntries()}
	return template('home', data) 

# log a new entry
@route('/log', method='POST')
def log():
	logEntry(request.forms['entry'])
	redirect('/home')

# erase an old entry
@route('/erase/<id>')
def erase(id):
	eraseEntry(id)
	redirect('/home')

run(reloader=True)
