from prime import isPrime

count = 0
i = 1
while i <= 200:
  if isPrime(i):
    count = count + 1
  i = i + 1

print count