from prime import isPrime
from sys import argv

maxx = int(argv[1])

count = 0

i = 1
while i <= maxx:
	if isPrime(i): count = count + 1
	i = i + 1

print 'Number of primes from 1 to', maxx, ':', count
