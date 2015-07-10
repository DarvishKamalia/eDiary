from bottle import Bottle, run, template, static_file, request, redirect
import datetime # Get the current timestamp
import swag as swag  



app = Bottle()
JSONmodule = swag.JSONmodule("test")
@app.route('/home')
def home():	
	return static_file('main.html', root='static/')

# static files (like CSS, fonts, pictures)
@app.get('/<filename:path>')
def server_static(filename):
	return static_file(filename, 'static/')

# get the text from the textarea
@app.get('/new')
def note():
	if request.query.entry == "": 
		return redirect('/home')
	entryTuple = ()
	print float(datetime.datetime.now().strftime('%s'))
	entryTuple += (float(datetime.datetime.now().strftime('%s')), request.query.entry,)
	print entryTuple
	JSONmodule.addEntry(entryTuple)	
	return request.query.entry

run(app, reloader=True)
