# The ordered set of three 4-digit numbers: 8128, 2882, 8281 has three interesting properties.

# The set is cyclic, in that the last two digits of each number is the first two digits of the next number (including the last number with the first).
# Each polygonal type: triangle (P_3,127 = 8128), square (P_4,91 = 8281) and pentagonal (P_5,44 = 2882) 
# is represented by a different number in the set.
# This is the only set of 4-digit numbers with this property.

# Find the sum of the only ordered set of six cyclic 
# 4-digit numbers for which each polygonal type: triangle, square, pentagonal, hexagonal, heptagonal, and octagonal,
# is represented by a different number in the set.

from time import time
start = time()

import sys
sys.path.append('C:\\Code\\project-euler')
from module import is_triangle, is_square, is_pentagonal, is_hexagonal, is_heptagonal, is_octagonal

# generate all 4 digit polygonal numbers
# find all four digit numbers that form a group of six cyclic numbers
# for each group, they need a polygonal of each type

polygonals = {
    3: [],
    4: [],
    5: [],
    6: [],
    7: [],
    8: [],
}

cyclic_polygonals = {}

for n in range(1000, 10000):
    if is_triangle(n):
        polygonals[3].append(n)
        cyclic_polygonals[(3, n)] = []
    if is_square(n):
        polygonals[4].append(n)
    if is_pentagonal(n):
        polygonals[5].append(n)
    if is_hexagonal(n):
        polygonals[6].append(n)
    if is_heptagonal(n):
        polygonals[7].append(n)
    if is_octagonal(n):
        polygonals[8].append(n)

print(polygonals)
print(cyclic_polygonals)

print(time() - start)

# Answer: 
