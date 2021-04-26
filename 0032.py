# We shall say that an n-digit number is pandigital if it makes use of all the digits 1
# to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.
# The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand,
# multiplier, and product is 1 through 9 pandigital.
# Find the sum of all products whose multiplicand/multiplier/product identity can be written
# as a 1 through 9 pandigital.

# HINT: Some products can be obtained in more than one way so be sure to only include it once
# in your sum.

from itertools import permutations

perms = permutations('123456789')
permset = set()
pandigital_products = set()

for perm in perms:
    permset.add(''.join(perm))

first = range(1, 1000)
second = range(1, 10000)

for i in first:
    print(f'i = {i}')
    for j in second:
        if (f'{str(i*j)}{i}{j}' in permset):
            pandigital_products.add(i * j)

print(sum(pandigital_products))

# Answer: 45228