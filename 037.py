# The number 3797 has an interesting property. Being prime itself,
# it is possible to continuously remove digits from left to right,
# and remain prime at each stage: 3797, 797, 97, and 7.
# Similarly we can work from right to left: 3797, 379, 37, and 3.
# Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

from time import time
start = time()

from module import sieve, is_prime
interesting_primes = []
for n in sieve(20, 750000):
    n1 = n
    n2 = n
    # left
    counter = 1
    if '0' not in str(n):
        for i in range(len(str(n1)) - 1):
            if is_prime(int(str(n1)[1:])):
                counter += 1
            n1 = int(str(n1)[1:])
        if counter == len(str(n)):
            # right
            counter = 1
            for i in range(len(str(n2)) - 1):
                if is_prime(int(str(n2)[:-1])):
                    counter += 1
                    n2 = int(str(n2)[:-1])
            if counter == len(str(n)):
                interesting_primes.append(n)

print(interesting_primes)
print(sum(interesting_primes))

print(time() - start)

# Answer: 748317
