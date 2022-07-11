# Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.

numbers = []
with open('0013.txt', 'r') as f:
    for line in f.readlines():
        numbers.append(int(line.strip()))

total = sum(numbers)
print(total)
print(str(total)[:10])

# Sum: 5537376230390876637302048746832985971773659831892672
# Answer: 5537376230