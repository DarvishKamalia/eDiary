from bottle import route, run, template, request, redirect, static_file
from db import load, store, getQuote
from entry import make

name = ""

# static files (like CSS, fonts, pictures)
@route('/static/<filepath:path>')
def static(filepath):
	return static_file(filepath, './static')

# homepage
@route('/home')
def home():
	global name
	if name == "":
		redirect('/signin')
	else:
		data = {'entries' : load()[0:10], 'name' : name}
		return template('home', data) 

# signin
@route('/signin')
def signin():
	quote = {'quote' : getQuote() }
	return template('signin', quote)

# signin POST
@route('/signin', method='POST')
def signin_post():
	global name
	if request.forms['name'] != "":
		name = request.forms['name']
		redirect('/home')
	else:
		redirect('/signin')

# signout
@route('/signout')
def signout():
	global name
	name = ""
	redirect('/signin')

# log a new entry
@route('/log', method='POST')
def log():
	text = request.forms['entry']
	if text == '':
		redirect('/home')
	else:
		entry = make(text)
		entries = load()
		entries.insert(0, entry)
		store(entries)
		redirect('/home')

# erase an old entry
@route('/erase/<id>')
def erase(id):
	entries = load()
	i = 0
	while i < len(entries):
		if id == entries[i]['id']:
			del entries[i]
			break
		i += 1
	store(entries)
	redirect('/home')

# search based on day, month, year
@route('/search')
def search():
	entries = load()

	# year
	temp1 = []
	year = request.query['year']
	if year != '':
		for entry in entries:
			if year == entry['year']:
				temp1.append(entry)
	else:
		temp1 = entries

	# mon
	temp2 = []
	mon = request.query['mon']
	if mon != '':
		for entry in temp1:
			if mon == entry['mon']:
				temp2.append(entry)
	else:
		temp2 = temp1

	# day
	result = []
	day = request.query['day']
	if day != '':
		for entry in temp2:
			if day == entry['day']:
				result.append(entry)
	else:
		result = temp2
	
	data = {'entries' : result}
	return template('search', data)

run(reloader=True,port=8000, debug=True)