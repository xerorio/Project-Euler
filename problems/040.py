# An irrational decimal fraction is created by concatenating the positive integers:
# 0.123456789101112131415161718192021...
# It can be seen that the 12th digit of the fractional part is 1.
# If d(n) represents the nth digit of the fractional part, find the value of the following expression.
# d(1) × d(10) × d(100) × d(1000) × d(10,000) × d(100,000) × d(1,000,000)

from time import time
start = time()

decimal = ''
for i in range(1, 200000):
    decimal += str(i)
product = 1
product *= int(decimal[9])
product *= int(decimal[99])
product *= int(decimal[999])
product *= int(decimal[9999])
product *= int(decimal[99999])
product *= int(decimal[999999])
print(product)

print(time() - start)

# Answer: 210
