from sys import argv
from random import random
from math import sqrt

steps = int(argv[1])
x, y = 0, 0

i = 0
while i < steps:
	rand = random()

	if rand < 0.25: x = x + 1
	elif rand < 0.5: x = x - 1
	elif rand < 0.75: y = y + 1
	else: y = y - 1

	print '(%d, %d)' % (x, y)
	i = i + 1

dist = sqrt(x*x + y*y)
print 'distance from beginning = %f' % dist
