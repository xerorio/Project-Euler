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

from math import floor

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
        cyclic_polygonals[(4, n)] = []
    if is_pentagonal(n):
        polygonals[5].append(n)
        cyclic_polygonals[(5, n)] = []
    if is_hexagonal(n):
        polygonals[6].append(n)
        cyclic_polygonals[(6, n)] = []
    if is_heptagonal(n):
        polygonals[7].append(n)
        cyclic_polygonals[(7, n)] = []
    if is_octagonal(n):
        polygonals[8].append(n)
        cyclic_polygonals[(8, n)] = []

# print(cyclic_polygonals)

for k in cyclic_polygonals:
    for triangle in polygonals[3]:
        if k[0] != 3 and int(str(k[1])[2:]) == floor(triangle / 100):
            cyclic_polygonals[k].append((3, triangle))

    for square in polygonals[4]:
        if k[0] != 4 and int(str(k[1])[2:]) == floor(square / 100):
            cyclic_polygonals[k].append((4, square))

    for pentagonal in polygonals[5]:
        if k[0] != 5 and int(str(k[1])[2:]) == floor(pentagonal / 100):
            cyclic_polygonals[k].append((5, pentagonal))

    for hexagonal in polygonals[6]:
        if k[0] != 6 and int(str(k[1])[2:]) == floor(hexagonal / 100):
            cyclic_polygonals[k].append((6, hexagonal))

    for heptagonal in polygonals[7]:
        if k[0] != 7 and int(str(k[1])[2:]) == floor(heptagonal / 100):
            cyclic_polygonals[k].append((7, heptagonal))

    for octagonal in polygonals[8]:
        if k[0] != 8 and int(str(k[1])[2:]) == floor(octagonal / 100):
            cyclic_polygonals[k].append((8, octagonal))

print(len(cyclic_polygonals))
with open('061.txt', 'w') as f:
    for x in cyclic_polygonals:
        f.writelines(f'{x}: {cyclic_polygonals[x]}\n')

print(time() - start)

#### THIS DOESN'T WORK YET #####

# Answer: 




# def fn(n):
#     return (3, n * (n + 1) / 2), (4, n * n), (5, n * (3 * n - 1) / 2), (6, n * (2 * n - 1)), (7, n * (5 * n - 3) / 2), (8, n * (3 * n - 2))
 
# def next(types, data):
#     if len(types) == 6 and data[0] // 100 == data[-1] % 100:
#         print(data, sum(data))
#     else:
#         for t, n in ds.get((types[-1], data[-1]), []):
#             if t not in types:
#                 next(types + [t], data + [n])
 
# p = []          # build a list of polygonal numbers with their type (type, pnum)
# n = 19          # first n for octogonal number > 999
 
# while n < 141:  # last n for triangle numbers < 10000
#     for type, data in fn(n):
#         if 1000 <= data <= 9999 and data % 100 > 9:
#             p.append((type, data)) 
#     n+=1
 
# ds = {}         # build a dictionary of tuples
# for t1, d1 in p:
#     for t2, d2 in p:
#         if t1 != t2 and d1 % 100 == d2 // 100:
#             ds[t1, d1] = ds.get((t1, d1),[]) + [(t2, d2)] 
 
# print("Project Euler 61 Solution Set")
# for type, data in ds: next([type], [data])