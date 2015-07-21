alll = ['h1', 'h2', 'h3', 'v1', 'v2', 'v3', 'v4']

zero = ['h1', 'h3', 'v1', 'v2', 'v3', 'v4']
one = ['v3', 'v4']
two = ['h1', 'h2', 'h3', 'v2', 'v3']
three = ['h1', 'h2', 'h3', 'v1', 'v2', 'v3', 'v4']
four = ['h1', 'h2', 'h3', 'v1', 'v2', 'v3', 'v4']
five = ['h1', 'h2', 'h3', 'v1', 'v2', 'v3', 'v4']
six = ['h1', 'h2', 'h3', 'v1', 'v2', 'v3', 'v4']
seven = ['h1', 'h2', 'h3', 'v1', 'v2', 'v3', 'v4']
eight = ['h1', 'h2', 'h3', 'v1', 'v2', 'v3', 'v4']

###

grid = {
	'h1' : False,
	'h2' : False,
	'h3' : False,
	'v1' : False,
	'v2' : False,
	'v3' : False,
	'v4' : False
}

def printNum():
	from sys import stdout
	stdout.write(' ')
	if grid['h1']: stdout.write('---')
	else: stdout.write('   ')
	stdout.write(' \n')
	if grid['v1']: stdout.write('|')
	else: stdout.write(' ')
	stdout.write('   ')
	if grid['v3']: stdout.write('|')
	else: stdout.write(' ')
	stdout.write('\n ')
	if grid['h2']: stdout.write('---')
	else: stdout.write('   ')
	stdout.write(' \n')
	if grid['v2']: stdout.write('|')
	else: stdout.write(' ')
	stdout.write('   ')
	if grid['v4']: stdout.write('|')
	else: stdout.write(' ')
	stdout.write('\n ')
	if grid['h3']: stdout.write('---')
	else: stdout.write('   ')
	stdout.write(' \n')

def addline(line):
	grid[line] = True

###

addline('h1')
addline('v3')
addline('v4')

printNum()

