"""
A nice long script with loads of useful functions and variables
"""

# functions

def remove_punctuation(input_string: str) -> str:
    """
    Removes punctuation from input string
    """
    from string import punctuation
    input_string = input_string.replace(' ', '')
    translator = str.maketrans('', '', punctuation)
    return input_string.translate(translator)

def is_prime(n: int) -> bool:
    """
    Calculates whether the given number is prime (True) or not (False)
    """
    if n in (2, 3):
        return True

    if n == 0 or n == 1 or n % 2 == 0 or n % 3 == 0:
        return False

    for i in range(5, int(abs(n)**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def fibonacci(n: int) -> list:
    """
    Calculates the fibonacci sequence while its length is less than n
    """
    fibonacci_seq = [1, 1, 2]
    while len(fibonacci_seq) < n:
        next_num = fibonacci_seq[len(fibonacci_seq)-1] + fibonacci_seq[len(fibonacci_seq)-2]
        fibonacci_seq.append(next_num)
    return fibonacci_seq

def sieve(m: int, n: int) -> list:
    """
    Uses the Sieve of Eratosthenes to calculate prime numbers from m up to n (non-inclusive)
    """
    sieve_primes = [True] * n
    for p in range(2, n):
        if sieve_primes[p]:
            for i in range(p * p, n, p):
                sieve_primes[i] = False
    primes = []
    for i in range(m, n):
        if sieve_primes[i]:
            primes.append(i)

    return primes

def reverse_sieve(m: int, n: int) -> list:
    """
    Uses the Sieve of Eratosthenes to calculate composite numbers from m up to n (non-inclusive)
    """
    sieve_primes = [True] * n
    for p in range(2, n):
        if sieve_primes[p]:
            for i in range(p * p, n, p):
                sieve_primes[i] = False
    composites = []
    for i in range(m, n):
        if sieve_primes[i] is False:
            composites.append(i)

    return composites

def divisors_i(n: int) -> list:
    """
    Returns divisors in numerical order of the given integer (inclusive)
    Does not include duplicates
    """
    divs = [1, n]
    for i in range(2, int(n * 0.5) + 1):
        if (n % i == 0) and i not in divs and (n / i) not in divs:
            if int(i) == int(n / i):
                divs.append(int(i))
            else:
                divs.extend([int(i), int(n / i)])
    return sorted(divs)

def divisors_n(n: int) -> list:
    """
    Returns divisors in numerical order of the given integer (non-inclusive)
    Does not include duplicates
    """
    divs = [1]
    for i in range(2, int(n * 0.5) + 1):
        if (n % i == 0) and i not in divs and (n / i) not in divs:
            if int(i) == int(n / i):
                divs.append(int(i))
            else:
                divs.extend([int(i), int(n / i)])
    return sorted(divs)

def reverse_digits(num: int) -> int:
    """
    Reverse the digits of the input number
    """
    rev_num = 0
    while num > 0:
        rev_num = rev_num * 10 + num % 10
        num = num // 10
    return rev_num

def is_palindromic(input_num: int) -> bool:
    """
    Determine whether the input number is palindromic
    """
    return reverse_digits(input_num) == input_num

def bin_is_palindrome(num: int) -> bool:
    """
    Check if the binary equivalent base 10 integer is palindromic
    """
    binary = bin(num)
    binary = binary[2:]
    return binary == binary[::-1]

def gcd(a: int, b: int) -> int:
    """
    Returns greatest common divisor of two input numbers
    """
    while b != 0:
        t = b
        b = a % b
        a = t
    return a

def is_pandigital(n: int, s = 9) -> bool:
    """
    Takes an integer and a length and determines
    whether the number is pandigital, default length is 9
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
            if n > 1:
                factors.append(int(n))
            break
    return factors

def is_triangle(n: int) -> bool:
    """
    Determines if input number is triangular
    """
    a = (((8 * n + 1) ** 0.5) - 1) / 2
    return a == int(a)

def is_square(n: int) -> bool:
    """
    Determines if input number is square
    """
    a = n ** 0.5
    return a == int(a)

def is_pentagonal(n: int) -> bool:
    """
    Determines if input number is pentagonal
    """
    a = (1 + ((24 * n + 1) ** 0.5)) / 6
    return a == int(a)

def is_hexagonal(n: int) -> bool:
    """
    Determines if input number is hexagonal
    """
    a = (1 + ((8 * n + 1) ** 0.5)) / 4
    return a == int(a)

def is_heptagonal(n: int) -> bool:
    """
    Determines if input number is heptagonal
    """
    a = (3 + ((40 * n + 9) ** 0.5)) / 10
    return a == int(a)

def is_octagonal(n: int) -> bool:
    """
    Determines if input number is octagonal
    """
    a = (1 + ((3 * n + 1) ** 0.5)) / 3
    return a == int(a)

def factorial(n: int) -> int:
    """
    Returns the factorial of input number without math module
    """
    f = 1
    while n > 1:
        f *= n
        n -= 1
    return f

def choose(n: int, r: int) -> int:
    """
    Applies the choose function to input numbers, assuming n >= r
    """
    if n < r:
        return 0
    return int(factorial(n) / (factorial(r) * factorial(n - r)))

def split_string(input_iterable: str, n: int) -> list:
    """
    Takes a string and returns the same iterable split into size 'n' sections
    """
    if n <= 1:
        raise ValueError('Invalid size input')
    if not isinstance(input_iterable, str):
        raise ValueError('Invalid iterable input')
    return ' '.join([input_iterable[i:i + n] for i in range(0, len(input_iterable), n)])

# variables
alphabet = {
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
