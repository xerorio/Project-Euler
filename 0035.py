# The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.
# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
# How many circular primes are there below one million?

def circularPrimes(n):
    primeList, sieve = [], [True] * n
    for p in range(2, n):
        if sieve[p]:
            for i in range(p*p, n, p):
                sieve[i] = False
    for p in range(2, n):
        if sieve[p]:
            circularPrime = True
            p_str = str(p)
            for i in range(0, len(p_str)):
                rotatedNumber = p_str[i:len(p_str)] + p_str[0:i]
                rotatedNumber1 = int(rotatedNumber)
                if not sieve[rotatedNumber1]:
                    circularPrime = False
            if circularPrime:
                primeList.append(p)
    return len(primeList)

print(circularPrimes(1000000))

# Answer: 55