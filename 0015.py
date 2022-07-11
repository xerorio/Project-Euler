# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down,
# there are exactly 6 routes to the bottom right corner.
# How many such routes are there through a 20×20 grid?

# overall you have to go 2 down and 2 across for a 2x2 grid, therefore for a 20x20 grid
# in total, you have to go 20 down and 20 across

from math import ceil

def routes(n):
    result = 1
    for i in range(1, n + 1):
        result *= ((n + i) / i)
    return result

# floating point error, so round up
print(ceil(routes(20)))

# Answer: 137846528820