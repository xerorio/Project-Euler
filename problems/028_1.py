# Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

# 73 74 75 76 77 78 79 80 81
# 72 43 44 45 46 47 48 49 50
# 71 42 21 22 23 24 25 26 51
# 70 41 20  7  8  9 10 27 52
# 69 40 19  6  1  2 11 28 53
# 68 39 18  5  4  3 12 29 54
# 67 38 17 16 15 14 13 30 55
# 66 37 36 35 34 33 32 31 56
# 65 64 63 62 61 60 59 58 57

# It can be verified that the sum of the numbers on the diagonals is 101.
# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

from time import time
start = time()

total = 1
for i in range(1, 501): 
    total += ((4 * i * i) + (4 * i) + 1) # top right diagonal, series starting on 9
    total += ((4 * i * i) + (2 * i) + 1) # top left diagonal, series starting on 7
    total += ((4 * i * i) + 1) # bottom left diagonal, series starting on 5
    total += ((4 * i * i) - (2 * i) + 1) # bottom right diagonal, series starting on 3

print(total)
print(time() - start)

# Answer: 669171001
