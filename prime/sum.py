from prime import isPrime

summ = 0

i = 1
while i <= 100:
	if isPrime(i): summ = summ + i
	i = i + 1

print 'Sum of primes from 1 to 100 :', summ
