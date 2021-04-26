# Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

# 21 22 23 24 25
# 20  7  8  9 10
# 19  6  1  2 11
# 18  5  4  3 12
# 17 16 15 14 13

# It can be verified that the sum of the numbers on the diagonals is 101.
# 21 + 25 + 7 + 9 + 1 + 5 + 3 + 17 + 13 = 101

# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

# first identified that all the number are odd
# there are also specific gaps between each series of numbers
# for a 7x7 grid:
# (1), (3), (5), (7), 9, 11, (13), 15, (17), 19, (21), 23, (25),
# 27, 29, (31), 33, 35, (37), 39, 41, (43), 45, 47, (49)
# bracketed are numbers along the diagonals

largest_number = 1001 * 1001

odd_numbers = list(range(1, largest_number + 1, 2))

# iterator index
i = 0

# gap for every four iterations
gap = 1

solution = 1

while odd_numbers[i] != largest_number:
    for j in range(4):
        i += gap
        solution += odd_numbers[i]
    gap += 1

print(solution)

# Answer: 669171001