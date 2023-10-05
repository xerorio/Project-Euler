# The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify
# it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.
# We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
# There are exactly four non-trivial examples of this type of fraction, less than one in value, 
# and containing two digits in the n and d.
# If the product of these four fractions is given in its lowest common terms, find the value of the d.

from time import time
start = time()

import sys
sys.path.append('C:\Code\project-euler')
from module import gcd

fractions = []
for n in range(11, 100):
    for d in range(n + 1, 100):
        n_1 = str(n)[0]
        n_2 = str(n)[1]
        if '0' not in str(n) and '0' not in str(d):
            if n_1 in str(d):
                if ((int(str(n)[1]) / int(str(d).replace(n_1, '', 1))) == n / d):
                    fractions.append([n, d])
            elif n_2 in str(d):
                if ((int(str(n)[0]) / int(str(d).replace(n_2, '', 1))) == n / d):
                    fractions.append([n, d])

numerator = fractions[0][0] * fractions[1][0] * fractions[2][0] * fractions[3][0]
denominator = fractions[0][1] * fractions[1][1] * fractions[2][1] * fractions[3][1]

print(denominator / gcd(numerator, denominator))

print(time() - start)

# Answer: 100
