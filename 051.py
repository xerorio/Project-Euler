# By replacing the 1st digit of the 2-digit number *3,
# it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.
# By replacing the 3rd and 4th digits of 56**3 with the same digit,
# this 5-digit number is the first example having seven primes among the ten generated numbers,
# yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993.
# Consequently 56003, being the first member of this family, is the smallest prime with this property.
# Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits)
# with the same digit, is part of an eight prime value family.

from time import time
start = time()

from module import sieve
primes = sieve(3, 1_000_000)

wildcards = []
searched = set()
def generate_wildcards(s, index):
    if index > 0 and s not in searched:
        wildcards.append(s)
        searched.add(s)
    for x in range(index, len(s)):
        generate_wildcards(substitute_asterisk(s, x), x+1)

def substitute_asterisk(s, index):
    return s[0:index] + '*' + s[index+1:]

def binary_search(prime):
    start = 0
    end = len(primes)
    middle = int((end + start) / 2)
    
    while(start < end and primes[middle] != prime and middle < len(primes)):
        if primes[middle] < prime:
            start = middle + 1
        else:
            end = middle - 1
        middle = int((end + start) / 2)
    
    if middle < len(primes) and primes[middle] == prime:
        return middle
    else:
        return -1

for x in range(0, len(primes)):
    wildcards = []
    generate_wildcards(str(primes[x]), 0)
    for y in range(1, len(wildcards)):
        count = 0
        for z in range(0, 10):
            num = int(wildcards[y].replace('*', str(z)))
            if len(str(num)) < len(wildcards[y]):
                continue
            if binary_search(num) >= 0:
                count += 1
        if count >= 8:
            answer = ''
            for c in wildcards[y]:
                if c == '*':
                    answer += '1'
                else:
                    answer += c
            print(answer)
            exit(0)

print(time() - start)

# Answer: 121313
