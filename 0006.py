# The sum of the squares of the first ten natural numbers is, 1^2 + 2^2 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is, (1 + 2 + ... + 10)^2 = 55^2 = 3025
# Find the difference between the sum of the squares of the first one
# hundred natural numbers and the square of the sum.

sum_of_natural_squares = 0
sum = 0
square_of_natural_sum = 0

for i in range(1, 101):
    sum_of_natural_squares += i**2

for i in range(1, 101):
    sum += i

square_of_natural_sum = sum**2

print(square_of_natural_sum - sum_of_natural_squares)

# Answer: 25164150
