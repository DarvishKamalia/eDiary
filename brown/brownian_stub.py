# RANDOM is a function that takes in no arguments and returns a random decimal
# number (with many digits after the decimal point) between 0.0 and 1.0
from random import random

# SQRT is a function which takes in a decimal number (or a positive integer)
# and returns its square root
from math import sqrt

# x and y coordinates of the particle, both are 0 at the start, so initialize them
x = 
y = 

# loop for 100 steps
i = 0
while i < 100:
	
	# generate random number between 0.0 and 1.0
	rand = 

	# go North/South/East/West with equal probability
	# (and change x and y accordingly)
	# HINT : use the random number just generated
	if:
	elif:
	elif:
	else:

	# print the position of the particle after this step
	print 

	# incrmeent loop counter to go to next step
	i = i + 1

# simulation over, calculate the distance from beginning
# HINT : simple use of Pythagoras theorom
dist = 

# print the distance just calculated
print 
