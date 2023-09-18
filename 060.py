# The primes 3, 7, 109, and 673, are quite remarkable.
# By taking any two primes and concatenating them in any order the result will always be prime. 
# For example, taking 7 and 109, both 7109 and 1097 are prime.
# The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.

# Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.

from time import time
from module import sieve, is_prime
import math
start = time()

# exceptions
# 2 will never work, because if placed at the end of a number, makes it even
# after finding 5 prime numbers, there are 20 combinations to check are prime

primes = sieve(2, 10000)

def comb(a, b):
    """
    Check two numbers when concatenated both ways is prime
    """
    len_a = math.floor(math.log10(a))+1
    len_b = math.floor(math.log10(b))+1
    if is_prime(int(a * (10 ** len_b) + b)) and is_prime(int(b * (10 ** len_a) + a)):
        return True
    return False

def solve():
    for a in primes:
        for b in primes:
            if b < a:
                continue
            if comb(a, b):
                for c in primes:
                    if c < b:
                        continue
                    if comb(a, c) and comb(b, c):
                        for d in primes:
                            if d < c:
                                continue
                            if comb(a, d) and comb(b, d) and comb(c, d):
                                for e in primes:
                                    if e < d:
                                        continue
                                    if comb(a, e) and comb(b, e) and comb(c, e) and comb(d, e):
                                        return(a + b + c + d + e)

print(solve())

print(time() - start)

# Answer: 26033
