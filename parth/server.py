from bottle import route, run, template, request, redirect, static_file
from db import load, store
from entry import make

# static files (like CSS, fonts, pictures)
@route('/static/<filepath:path>')
def static(filepath):
	return static_file(filepath, './static')

# homepage
@route('/home')
def home():
	data = {'entries' : load()[0:10]}
	return template('home', data) 

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

run(reloader=True, debug=True)
