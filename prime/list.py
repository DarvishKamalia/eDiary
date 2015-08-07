from prime import isPrime

listt = []

i = 1
while i <= 100:
	if isPrime(i): listt = listt + [i]
	i = i + 1

print 'List of primes from 1 to 100 :', listt
