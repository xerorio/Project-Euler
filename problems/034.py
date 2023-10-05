# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
# Find the sum of all numbers which are equal to the sum of the factorial of their digits.
# Note: As 1! = 1 and 2! = 2 are not sums they are not included.

from time import time
start = time()

import sys
sys.path.append('C:\Code\project-euler')
from module import factorial

curious_numbers = []
for n in range(10, 50000):
    sum_of_factorials = sum([factorial(int(i)) for i in str(n)])
    if n == sum_of_factorials:
        curious_numbers.append(n)

print(sum(curious_numbers))

print(time() - start)

# Answer: 40730
