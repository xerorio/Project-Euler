# The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719,
# are themselves prime.
# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
# How many circular primes are there below one million?

from time import time
start = time()

from module import sieve, is_prime

def rotate(n: int) -> list:
    r = set()
    for i in range(len(str(n))):
        r.add(int(f'{str(n)[i:]}{str(n)[:i]}'))
    return r

circular_primes = []
for n in sieve(2, 1000000):
    counter = 0
    if '0' not in str(n):
        rotations = rotate(n)
        for r in rotations:
            if is_prime(r):
                counter += 1
        if counter == len(rotations):
            circular_primes.append(n)

print(len(circular_primes))

print(time() - start)

# Answer: 55
