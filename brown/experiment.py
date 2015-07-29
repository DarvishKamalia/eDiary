import sys, random, math

steps = int(sys.argv[1])
trials = int(sys.argv[2])

total_sqrd_dist = 0.0

i = 0
while i < trials:
	x, y = 0, 0

	j = 0
	while j < steps:
		rand = random.random()

		if rand < 0.25: x = x + 1
		elif rand < 0.5: x = x - 1
		elif rand < 0.75: y = y + 1
		else: y = y - 1

		j = j + 1
		
	sqrd_dist = x*x + y*y
	total_sqrd_dist = total_sqrd_dist + sqrd_dist

	i = i + 1

mean_sqrd_dist = total_sqrd_dist / trials
mean_dist = math.sqrt(mean_sqrd_dist)
print 'mean distance from beginning = %f' % mean_dist
