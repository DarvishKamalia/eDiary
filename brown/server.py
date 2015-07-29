from bottle import route, run, request, static_file
import random, math

@route('/brownian.css')
def css():
	return static_file('brownian.css', '.')

@route('/brownian.html')
def html():
	return static_file('brownian.html', '.')

@route('/brownian.html', method='POST')
def simulate():
	steps = int(request.forms.steps)
	x, y = 0, 0
	html = ''

	i = 0
	while i < steps:
		rand = random.random()

		if rand < 0.25: x = x + 1
		elif rand < 0.5: x = x - 1
		elif rand < 0.75: y = y + 1
		else: y = y - 1

		html = html + '<p>(' + str(x) + ', ' + str(y) + ')</p>'

		i = i + 1

	dist = math.sqrt(x*x + y*y)
	html = html + '<hr>' + '<p>distance from beginning = ' + str(dist) + '</p>'

	html = html + '<a href="brownian.html">Try another simulation</a>'
	return html

run(reloader=True, debug=True)
