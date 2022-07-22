# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.
# Find the sum of all the multiples of 3 or 5 below 1000.

ints_to_add = []

for i in range(0, 1001):
    if (i % 3 == 0):
        ints_to_add.append(i)
    elif (i % 5 == 0):
        ints_to_add.append(i)

result = 0
for i in ints_to_add:
    result += i

print(result - 1000)

# Answer: 233168
