# The prime 41, can be written as the sum of six consecutive primes:
# 41 = 2 + 3 + 5 + 7 + 11 + 13
# This is the longest sum of consecutive primes that adds to a prime below one-hundred.
# The longest sum of consecutive primes below one-thousand that adds to a prime,
# contains 21 terms, and is equal to 953.
# Which prime, below one-million, can be written as the sum of the most consecutive primes?

from time import time
start = time()

import sys
sys.path.append('C:\Code\project-euler')
from module import sieve, is_prime
primes = sieve(2, 10000)

fin_seq = []
l = len(primes)
j = l
while j != 0:
    i = 0
    while i + j < l + 1:
        seq = primes[i:i + j]
        if sum(seq) <= 1_000_000:
            if is_prime(sum(seq)):
                if len(seq) > len(fin_seq):
                    fin_seq = seq
        i += 1
    j -= 1
print(sum(fin_seq))

print(time() - start)

# Answer: 997651
