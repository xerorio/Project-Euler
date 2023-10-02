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

largest_p = 0
most_p = 0
for p in perimeters:
    if perimeters.count(p) > most_p:
        largest_p = p
        most_p = perimeters.count(p)
print([int(largest_p), most_p])

print(time() - start)

# Answer: 840
