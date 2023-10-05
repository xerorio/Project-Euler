# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number.
# For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
# A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16,
# the smallest number that can be written as the sum of two abundant numbers is 24.
# By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers.
# However, this upper limit cannot be reduced any further by analysis even though
# it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.
# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

import sys
sys.path.append('C:\Code\project-euler')
from module import divisors_n

abundant_nums = []
for i in range(1, 28123):
    if sum(set(divisors_n(i))) > i:
        abundant_nums.append(i)

abundant_num_sums = [0]*28124
for x in range(0, len(abundant_nums)):
    for y in range(x, len(abundant_nums)):
        sum_2_abundant_nums = abundant_nums[x] + abundant_nums[y]
        if (sum_2_abundant_nums <= 28123 and abundant_num_sums[sum_2_abundant_nums] == 0):
            abundant_num_sums[sum_2_abundant_nums] = 1

total = 0
for i in range(len(abundant_num_sums)):
    if (abundant_num_sums[i] == 0):
        total += i

print(total)

# Answer: 4179871
