from bottle import route, run, template, request, redirect, static_file
import db

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
		data = {'entries' : db.loadEntries()[0:10], 'feelings' : db.loadFeelings(), 'name' : name}
		return template('home', data)

# signin
@route('/signin')
def signin():
	data = {'quote' : db.getQuote()}
	return template('signin', data)

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
		i += 1
	db.storeEntries(entries)
	redirect('/home')

# search based on day, month, year
@route('/search')
def search():
	entries = db.loadEntries()

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
	
	data = {'entries' : result, 'query' : request.query, 'feelings' : db.loadFeelings()}
	return template('search', data)

run(reloader=True, debug=True)
