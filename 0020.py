# n! means n × (n − 1) × ... × 3 × 2 × 1
# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

# Find the sum of the digits in the number 100!

from module import split_word

product = 1
for i in range(2, 100):
    product *= i

total = 0
for x in list(filter(lambda n: int(n) != 0, split_word(str(product)))):
    total += int(x)

print(total)

# Answer: 648
