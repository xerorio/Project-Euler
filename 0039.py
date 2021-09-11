# If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.
# {20,48,52}, {24,45,51}, {30,40,50}
# For which value of p ≤ 1000, is the number of solutions maximised?

from math import sqrt

pythagorean_triples = []
perimeters = {}

# generate_pythagorean_triples
for i in range(1, 100):
    denominator = i + i + 1
    numerator = (denominator * i) + i
    hypotenuse = sqrt( (denominator*denominator) + (numerator*numerator) )

    triple = [denominator, numerator, int(hypotenuse)]
    pythagorean_triples.append(triple)

for triple in pythagorean_triples:
    if sum(triple) in perimeters:
        perimeters[sum(triple)].append(triple)
    else:
        perimeters[sum(triple)] = [triple,]

print(perimeters)

# Answer: 