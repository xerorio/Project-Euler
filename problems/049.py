# The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330,
# is unusual in two ways:
# (i) each of the three terms are prime
# (ii) each of the 4-digit numbers are permutations of one another.
# There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes,
# exhibiting this property, but there is one other 4-digit increasing sequence.
# What 12-digit number do you form by concatenating the three terms in this sequence?

from time import time
start = time()

from ..module import is_prime
for i in range(1488, 6671):
    j = i + 3330
    k = i + 6660
    if (is_prime(i) and is_prime(j) and is_prime(k) and
        sorted(str(i)) == sorted(str(j)) == sorted(str(k))):
        print(str(i) + str(j) + str(k))

print(time() - start)

# Answer: 296962999629
