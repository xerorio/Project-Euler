# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143?

prime_nums = []
num = 600851475143
prime_factors = []

for i in range(2, 10086):
    remainder = True
    for j in range(2, (i-1)):
        if (i <= j):
            break
        if (i % j == 0):
            remainder = False
            break
    if (remainder == True):
        prime_nums.append(i)

for prime_num in prime_nums:
    while num % prime_num == 0:
        num /= prime_num
        prime_factors.append(prime_num)

print(prime_factors)

# Answer: 6857