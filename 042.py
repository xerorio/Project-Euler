# The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1);
# so the first ten triangle numbers are:
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
# By converting each letter in a word to a number corresponding to its
# alphabetical position and adding these values we form a word value.
# For example, the word value for SKY is 19 + 11 + 25 = 55 = t10.
# If the word value is a triangle number then we shall call the word a triangle word.
# How many in the text file are triangle words?

from time import time
start = time()

from module import letters_to_numbers

words = []
with open('042.txt', 'r') as f:
    for w in f.read().split(','):
        words.append(w[1:-1])

triangular_numbers = [1]
for i in range(2, 1000):
    triangular_numbers.append(triangular_numbers[-1] + i)

counter = 0
for word in words:
    word_sum = 0
    for l in word:
        word_sum += letters_to_numbers[l]
    if word_sum in triangular_numbers:
        counter += 1

print(counter)

print(time() - start)

# Answer: 162
