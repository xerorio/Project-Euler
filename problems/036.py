# The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.
# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
# (Please note that the palindromic number, in either base, may not include leading zeros.)

from time import time
start = time()

import sys
sys.path.append('C:\Code\project-euler')
from module import is_palindromic, bin_is_palindrome
nice_numbers = set()
for i in range(1, 1000000):
    if is_palindromic(i) and bin_is_palindrome(i):
        nice_numbers.add(i)
print(sum(nice_numbers))

print(time() - start)

# Answer: 872187
