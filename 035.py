# The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719,
# are themselves prime.
# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
# How many circular primes are there below one million?

from time import time
start = time()

def rotate(n: int) -> list:
    rotations = [n]
    for i in range(len(str(n)) - 1):
        rotations.append(int(f'{str(rotations[-1])[1:]}{str(rotations[-1])[0]}'))
    return rotations

print(rotate(197))

print(time() - start)

# Answer: 
