# to demonstrate type conversions
# and to teach stdin stdout

from sys import stdin, stdout

stdout.write('Enter an integer: \n')
x = int(stdin.readline()) # x = '20' and not x = 20
print type(x)