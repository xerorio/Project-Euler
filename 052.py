# It can be seen that the number, 125874, and its double, 251748,
# contain exactly the same digits, but in a different order.
# Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.

from time import time
start = time()

for i in range(2, 200000):
    digits = ''.join(sorted(str(i)))
    if (''.join(sorted(str(i * 2))) == digits and
        ''.join(sorted(str(i * 3))) == digits and
        ''.join(sorted(str(i * 4))) == digits and
        ''.join(sorted(str(i * 5))) == digits and
        ''.join(sorted(str(i * 6))) == digits):
        print(i)
        exit(0)

print(time() - start)

# Answer: 142857
