# The number 3797 has an interesting property. Being prime itself,
# it is possible to continuously remove digits from left to right,
# and remain prime at each stage: 3797, 797, 97, and 7.
# Similarly we can work from right to left: 3797, 379, 37, and 3.
# Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

from module import sieve, is_prime

primes = sieve(11, 1000000)
primes_truncated_left = []
primes_truncated_right = []

truncatable_primes = []

def truncate_left(prime: int) -> bool:
    prime = str(prime)
    truncated_primes = [prime]
    while len(prime) > 1:
        prime = prime[1:]
        truncated_primes.append(int(prime))
    
    check = []

    for truncated_prime in truncated_primes:
        if is_prime(int(truncated_prime)):
            check.append(truncated_prime)
    
    if len(truncated_primes) == len(check):
        return True

    return False

def truncate_right(prime: int) -> bool:
    prime = str(prime)
    truncated_primes = [prime]
    while len(prime) > 1:
        prime = prime[:-1]
        truncated_primes.append(int(prime))
    
    check = []

    for truncated_prime in truncated_primes:
        if is_prime(int(truncated_prime)):
            check.append(truncated_prime)
    
    if len(truncated_primes) == len(check):
        return True

    return False

for prime in primes:
    if truncate_left(prime) and truncate_right(prime):
        truncatable_primes.append(prime)

print(sum(truncatable_primes))

# Answer: 748317