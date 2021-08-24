# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number.
# For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28,
# which means that 28 is a perfect number.

# A number n is called deficient if the sum of its proper divisors is less than n
# and it is called abundant if this sum exceeds n.
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16,
# the smallest number that can be written as the sum of two abundant numbers is 24.
# By mathematical analysis, it can be shown that all integers greater than
# 28123 can be written as the sum of two abundant numbers.

# However, this upper limit cannot be reduced any further by analysis even
# though it is known that the greatest number that cannot be expressed as the
# sum of two abundant numbers is less than this limit.

# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

from module import divisors

abundant_nums = []

# calculate abundant numbers up to 28123 inclusive
for i in range(1, 28124):
    divisors = divisors(i)
    divisor_sum = 0
    for divisor in divisors:
        divisor_sum += divisor
    if (divisor_sum > i):
        abundant_nums.append(i)

largest_abundant_num = max(abundant_nums)
not_a_sum_of_abundant_nums = []

for i in range(1, largest_abundant_num * 2):
    not_a_sum_of_abundant_nums.append(i)

sums = [0]*28124
for x in range(0, len(abundant_nums)):
    for y in range(x, len(abundant_nums)):
            sumOf2AbundantNums = abundant_nums[x] + abundant_nums[y]
            if (sumOf2AbundantNums <= 28123):
                if (sums[sumOf2AbundantNums] == 0):
                    sums[sumOf2AbundantNums] = sumOf2AbundantNums

total = 0
for i in range(1, len(sums)):
    if (sums[i] == 0):
        total += i

print(total)

# Answer: 4179871