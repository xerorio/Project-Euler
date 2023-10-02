# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a
# and b are called amicable numbers.
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110;
# therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
# Evaluate the sum of all the amicable numbers under 10000.

from ..module import divisors_n, sieve

prime_nums = sieve(2, 10000)

amicables = []
checked_nums = []

for i in range(2, 10000):
    if (i not in prime_nums and i not in checked_nums):
        da = sum(divisors_n(i))
        db = sum(divisors_n(da))
        checked_nums.extend([da, db])
        if (i == db and da != db):
            amicables.extend([i, da])

print(int(sum(amicables)))

# Answer: 31626
