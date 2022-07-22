def split_word(word: str) -> list:
    return [c for c in word]

def is_prime(n: int) -> bool:
    """
    Calculates whether the given number is prime (True) or not (False)
    """
    if n == 0 or n == 1:
        return False

    for i in range(2, int(abs(n)**0.5) + 1):
        if n % i == 0:
            return False
    return True

def fibonacci(n: int) -> list:
    """
    Calculates the fibonacci sequence while its length is less than n
    """
    fibonacci = [1, 1, 2]
    while len(fibonacci) < n:
        next_num = fibonacci[len(fibonacci)-1] + fibonacci[len(fibonacci)-2]
        fibonacci.append(next_num)
    return fibonacci

def sieve(m: int, n: int) -> list:
    """
    Uses the Sieve of Eratosthenes to calculate prime numbers from m up to n (non-inclusive)
    """
    sieve = [True] * n
    for p in range(2, n):
        if sieve[p]:
            for i in range(p * p, n, p):
                sieve[i] = False
    primes = []
    for i in range(m, n):
        if sieve[i]:
            primes.append(i)
    
    return primes

def reverse_sieve(m: int, n: int) -> list:
    """
    Uses the Sieve of Eratosthenes to calculate composite numbers from m up to n (non-inclusive)
    """
    sieve = [True] * n
    for p in range(2, n):
        if sieve[p]:
            for i in range(p * p, n, p):
                sieve[i] = False
    composites = []
    for i in range(m, n):
        if sieve[i] is False:
            composites.append(i)
    
    return composites

def divisors_i(n: int) -> list:
    """
    Returns all the divisors of a given integer (inclusive)
    """
    divs = [1, n]
    for i in range(2, int(n ** 0.5) + 1):
        if (n % i == 0) and i not in divs and (n / i) not in divs:
            divs.extend([int(i), int(n / i)])
    return divs

def divisors_n(n: int) -> list:
    """
    Returns all the divisors of a given integer (non-inclusive)
    """
    divs = [1]
    for i in range(2, int(n * 0.5) + 1):
        if (n % i == 0) and i not in divs and (n / i) not in divs:
            divs.extend([int(i), int(n / i)])
    return divs

def reverse_digits(num: int) -> int:
    """
    Reverse the digits of the input number
    """
    rev_num = 0
    while (num > 0):
        rev_num = rev_num * 10 + num % 10
        num = num // 10
    return rev_num

def is_palindromic(input_num: int) -> bool:
    """
    Determine whether the input number is palindromix
    """
    if (reverse_digits(input_num) == input_num):
        return True
    else:
        return False

def bin_is_palindrome(num: int) -> bool:
    """
    Check if the binary equivalent base 10 integer is palindromic
    """
    binary = bin(num)
    binary = binary[2:]
    return binary == binary[-1::-1]

def gcd(a: int, b: int) -> int:
    """
    Returns greatest common divisor of two input numbers
    """
    while b != 0:
        t = b
        b = a % b
        a = t
    return a

def factorial(n: int) -> int:
    """
    Applies factorial function to input number
    """
    if isinstance(n, int) is False:
        print('Error: number is not an integer')
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f

def is_pandigital(n: int, s = 9) -> bool:
    """
    Takes an integer and a length and determines whether the number is pandigital, default length is 9
    """
    n = str(n)
    return len(n) == s and not '1234567890'[:s].strip(n)

def prime_factors(n: int) -> list:
    """
    Returns all the prime factors of a input number
    """
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(int(d))
            n /= d
        d = d + 1
        if (d * d) > n:
            if n > 1: factors.append(int(n))
            break
    return factors

def is_pentagonal(n: int) -> bool:
    """
    Determines if input number is pentagonal
    """
    # Get positive root of equation P(n) = n.
    a = (1 + ((24 * n + 1) ** 0.5)) / 6
    return(a == int(a))

def is_hexagonal(n: int) -> bool:
    """
    Determines if input number is hexagonal
    """
    # Get positive root of equation H(n) = n.
    a = (1 + ((8 * n + 1) ** 0.5)) / 4
    return(a == int(a))

letters_to_numbers = {
    'A': 1,
    'B': 2,
    'C': 3,
    'D': 4,
    'E': 5,
    'F': 6,
    'G': 7,
    'H': 8,
    'I': 9,
    'J': 10,
    'K': 11,
    'L': 12,
    'M': 13,
    'N': 14,
    'O': 15,
    'P': 16,
    'Q': 17,
    'R': 18,
    'S': 19,
    'T': 20,
    'U': 21,
    'V': 22,
    'W': 23,
    'X': 24,
    'Y': 25,
    'Z': 26
}
