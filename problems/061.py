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

from ..module import is_triangle, is_square, is_pentagonal, is_hexagonal, is_heptagonal, is_octagonal

print(time() - start)

# Answer: 
