# If p is the perimeter of a right angle triangle with integral length sides, {a,b,c},
# there are exactly three solutions for p = 120.
# {20,48,52}, {24,45,51}, {30,40,50}
# For which value of p ≤ 1000, is the number of solutions maximised?

from time import time
start = time()

perimeters = []
for a in range(1, 500):
    for b in range(a, 500):
        c = ((a * a) + (b * b))**0.5
        if int(c) == c and a + b + c <= 1000:
            perimeters.append(a + b + c)

largest_perimeter = 0
most_perimeters = 0
for i in range(10, 1000):
    if perimeters.count(i) > most_perimeters:
        largest_perimeter = i
        most_perimeters = perimeters.count(i)
print([largest_perimeter, most_perimeters])

print(time() - start)

# Answer: 840
