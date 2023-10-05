# It was proposed by Christian Goldbach that every odd composite number can be 
# written as the sum of a prime and twice a square.
# 9 = 7 + 2 × (1^2)
# 15 = 7 + 2 × (2^2)
# 21 = 3 + 2 × (3^2)
# 25 = 7 + 2 × (3^2)
# 27 = 19 + 2 × (2^2)
# 33 = 31 + 2 × (1^2)
# It turns out that the conjecture was false.
# What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?

from time import time
start = time()

from math import sqrt
import sys
sys.path.append('C:\Code\project-euler')
from module import is_prime
primes = []

done = False
n = 2
while done is False:
    if is_prime(n):
        primes.append(n)
    elif n % 2 == 1:
        it_can = False
        for p in primes:
            square = sqrt((n - p) / 2)
            if square == int(square):
                it_can = True
        if it_can is False:
            print(n)
            done = True
    n += 1

print(time() - start)

# Answer: 5777
