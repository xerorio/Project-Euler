# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

sum, sieve = 0, [True] * 2000000
for p in range(2, 2000000):
    if sieve[p]:
        sum += p
        for i in range(p*p, 2000000, p):
            sieve[i] = False
print(sum)

# Answer: 142913828922