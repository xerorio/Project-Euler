# Euler discovered the remarkable quadratic formula:
# (n^2 + n + 41)
# It turns out that the formula will produce 40 primes for the consecutive integer values 0 <= n <= 39.
# However, when n = 40, 40^2 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41
# The incredible formula (n^2 -79n + 1601) was discovered, which produces 80 primes for the consecutive values 0 <= n <= 79
# The product of the coefficients, −79 and 1601, is −126479.

# Find the product of the coefficients, a and b,
# for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n = 0.

from time import time
import sys
sys.path.append('C:\Code\project-euler')
from module import sieve, is_prime

start = time()

# find primes up to 1000 - these are possible values for b, since when n is 0, b must be prime
primes_up_to_one_thousand = sieve(2, 1000)
primes = primes_up_to_one_thousand.copy()

xy = 0
largest = 0

for x in primes_up_to_one_thousand:
    for y in primes_up_to_one_thousand:
        n = 0

        # positive 'a' and positive 'b'
        while True:
            quadratic = (n * (n + x)) + y
            if is_prime(quadratic) is False:
                if n - 1 > largest:
                    largest = (n - 1)
                    xy = x * y
                break
            n += 1

        n = 0

        # negative 'a' and positive 'b'
        while True:
            quadratic = (n * (n - x)) + y
            if is_prime(quadratic) is False or quadratic < 0:
                if n - 1 > largest:
                    largest = n - 1
                    xy = -1 * x * y
                break
            n += 1

print(xy)

print(time() - start)

# Answer: -59231
