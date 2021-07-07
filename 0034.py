# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
# Find the sum of all numbers which are equal to the sum of the
# factorial of their digits.
# Note: As 1! = 1 and 2! = 2 are not sums they are not included.
from math import factorial

valid_nums = []

for n in range(1, 100000):
    sum = 0
    n = str(n)
    for digit in n:
        digit = int(digit)
        sum += factorial(digit)
    n = int(n)
    if (sum == n):
        valid_nums.append(n)
    
valid_nums.remove(1)
valid_nums.remove(2)

print(valid_nums)

sum = 0
for i in valid_nums:
    sum += i
print(sum)

# Answer: 40730