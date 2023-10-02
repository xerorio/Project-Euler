# A googol (10^100) is a massive number: one followed by one-hundred zeros;
# 100^100 is almost unimaginably large: one followed by two-hundred zeros.
# Despite their size, the sum of the digits in each number is only 1.
# Considering natural numbers of the form, ab, where a, b < 100, what is the maximum digital sum?

from time import time
start = time()

max_digit_sum = 0
for a in range(1, 100):
    for b in range(1, 100):
        digit_sum = 0
        for i in str(int(a ** b)):
            digit_sum += int(i)
        if digit_sum > max_digit_sum:
            max_digit_sum = digit_sum
print(max_digit_sum)

print(time() - start)

# Answer: 972
