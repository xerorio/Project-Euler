# The fraction 49/98 is a curious fraction, as an inexperienced mathematician
# in attempting to simplify it may incorrectly believe that 49/98 = 4/8,
# which is correct, is obtained by cancelling the 9s.
# We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
# There are exactly four non-trivial examples of this type of fraction,
# less than one in value, and containing two digits in the numerator and denominator.
# If the product of these four fractions is given in its lowest common terms,
# find the value of the denominator.

from fractions import Fraction

product_p = 1
product_q = 1

for p in range(10, 100):
    for q in range(10, 100):
        reduced = float(p) / q
        if reduced >= 1.0:
            continue
        reduced = Fraction(p, q)

        pstr = str(p)
        qstr = str(q)

        for l in pstr:
            if l == '0':
                continue
            if l in qstr:
                rpstr = pstr.replace(l, '')
                rqstr = qstr.replace(l, '')
                if len(rpstr) == 0 or len(rqstr) == 0 or int(rqstr) == 0:
                    continue
                frac = Fraction(int(rpstr), int(rqstr))
                if frac == reduced:
                    print(f'{rpstr}/{rqstr} == {str(p)}/{str(q)}')
                    product_p *= int(rpstr)
                    product_q *= int(rqstr)

product = Fraction(product_p, product_q)

print(product)

# Answer: 100