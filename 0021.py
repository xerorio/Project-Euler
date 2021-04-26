# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a
# and b are called amicable numbers.
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110;
# therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
# Evaluate the sum of all the amicable numbers under 10000.

from math import sqrt

def sieve(n) -> list:
    sieve = [True] * n
    for p in range(2, n):
        if sieve[p]:
            for i in range(p*p, n, p):
                sieve[i] = False
    prime = []
    for i in range(1, n):
        if sieve[i] == True:
            prime.append(i)
    return prime

def divisors(n) -> list:
	divs = [1]
	for i in range(2, int(sqrt(n)) + 1):
		if (n % i == 0):
			divs.extend([i, n / i])
	return list(set(divs))

prime_nums = sieve(10000)
amicable_nums = []
checked_nums = []

for i in range(2, 10000):
    if (i not in prime_nums and i not in checked_nums):
        da = sum(divisors(i))
        db = sum(divisors(da))
        checked_nums.extend([da, db])
        if (i == db and db != da):
            amicable_nums.extend([i, da])

print(sum(amicable_nums))

# Answer: 31626