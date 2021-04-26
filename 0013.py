# Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
# (in the txt file)

number_list = []
sum = 0

with open('0013.txt', 'r') as f:
    number_list = f.readlines()

for i in number_list:
    i = i.strip()
    sum += int(i)

print(sum)

# Sum: 5537376230390876637302048746832985971773659831892672
# Answer: 5537376230