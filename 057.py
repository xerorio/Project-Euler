# It is possible to show that the square root of two can be expressed as an infinite continued fraction.
# In the first one-thousand expansions, how many fractions contain
# a numerator with more digits than the denominator?

from time import time
start = time()

p = 1
q = 1
counter = 0
for i in range(1000):
    numerator = p + (2 * q)
    denominator = p + q
    if len(str(numerator)) > len(str(denominator)):
        counter += 1
    p = numerator
    q = denominator

print(counter)

print(time() - start)

# Answer: 153
