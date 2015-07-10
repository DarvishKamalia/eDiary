from bottle import Bottle, run, template, static_file

app = Bottle()

@app.route('/home')
def home():	
	return static_file('main.html', root='templates/')

@app.get('/<filename>')
def server_static(filename):
	return static_file(filename, root='templates/')



run(app, host='localhost', port=8080, debug=True)
