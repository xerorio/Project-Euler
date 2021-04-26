# For quadratics in the form n^2 + an + b, where
# modulus(a) < 1000 and modulus(b) < 1000

# Find the product of the coefficients, a and b,
# for the quadratic expression that produces the maximum number of
# primes for consecutive values of n, starting with n = 0.

from module import sieve, is_prime

# find primes up to 1000 - these are possible values for b, since when n is 0, b must be prime
primes_up_to_one_thousand = sieve(1000)
primes = primes_up_to_one_thousand.copy()

y_times_x = 0
largest = 0

for x in primes_up_to_one_thousand:
    for y in primes_up_to_one_thousand:
        n = 0

        # positive 'a' and positive 'b'
        while True:
            quadratic = (n**2) + (y * n) + x
            if quadratic not in primes:
                if is_prime(quadratic):
                    primes.append(quadratic)
                else:
                    if n - 1 > largest:
                    	largest = (n - 1)
                    	y_times_x = y * x 
                    break
            n += 1

        n = 0

        # negative 'a' and positive 'b'
        while True:
            quadratic = (n**2) - (y * n) + x
            if quadratic not in primes:
                if is_prime(quadratic) and quadratic > 0:
                    primes.append(quadratic)
                else:
                    if n - 1 > largest:
                        largest = n - 1
                        y_times_x = -1 * y * x 
                    break
            n += 1

print(y_times_x)

# Answer: 