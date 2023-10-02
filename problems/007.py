# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

prime_nums = []

for i in range(2, 1000000):
    remainder = True
    for j in range(2, (i-1)):
        if (i <= j):
            break
        if (i % j == 0):
            remainder = False
            break
    if (remainder == True):
        prime_nums.append(i)
    if (len(prime_nums) == 10001):
        break

print(prime_nums[10000])

# Answer: 104743
