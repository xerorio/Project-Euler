# The first two consecutive numbers to have two distinct prime factors are:
# 14 = 2 × 7
# 15 = 3 × 5
# The first three consecutive numbers to have three distinct prime factors are:
# 644 = 2^2 × 7 × 23
# 645 = 3 × 5 × 43
# 646 = 2 × 17 × 19.
# Find the first four consecutive integers to have four distinct prime factors each.
# What is the first of these numbers?

from time import time
start = time()

def npf(n):
    """
    Number of unique prime factors of a number
    """
    i = 2
    factors = set()
    while i < n**0.5 or n == 1:
        if n % i == 0:
            n /= i
            factors.add(i)
            i -= 1
        i += 1
    return (len(factors) + 1)

# first possible number
i = 2*3*5*7

# while loop
while True:
    if npf(i) == 4:
        i += 1
        if npf(i) == 4:
            i += 1
            if npf(i) == 4:
                i += 1
                if npf(i) == 4:
                    print(i - 3)
                    break
    i += 1

print(time() - start)

# Answer: 134043
