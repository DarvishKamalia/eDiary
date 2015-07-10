from bottle import Bottle, run, template, static_file, request
from bottle import redirect
app = Bottle()

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
	return request.query.entry





run(app, reloader=True)
