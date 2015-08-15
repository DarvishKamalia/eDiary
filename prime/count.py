from prime import isPrime

count = 0

i = 1
while i <= 100:
	if isPrime(i):
		count = count + 1
	i = i + 1

print 'Number of primes from 1 to 100 :', count
