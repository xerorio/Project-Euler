# We shall say that an n-digit number is pandigital if it makes use of all the digits
# 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.
# What is the largest n-digit pandigital prime that exists?

from time import time
start = time()

from module import is_pandigital, is_prime

# sum of digits from 9 down to 1 is divisble by 3
# sum of digits from 8 down to 1 is divisble by 3
# sum of digits from 7 down to 1 is not divisble by 3
n = 7654321
while not(is_pandigital(n, 7) and is_prime(n)):
    n -= 2
print(n)

print(time() - start)

# Answer: 7652413
