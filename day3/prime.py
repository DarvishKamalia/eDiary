from math import sqrt
from itertools import count, islice

def isPrime(n):
	if n < 2: return False
	else: return all(n % i for i in islice(count(2), int(sqrt(n)-1)))
