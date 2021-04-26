# The following iterative sequence is defined for the set of positive integers:

# n → n/2 (n is even)
# n → 3n + 1 (n is odd)

# Using the rule above and starting with 13, we generate the following sequence:
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
# Although it has not been proved yet (Collatz Problem),
# it is thought that all starting numbers finish at 1.
# Which starting number, under one million, produces the longest chain?
# NOTE: Once the chain starts the terms are allowed to go above one million.

def collatz_sequence(start_number: int) -> list:
    sequence = [start_number]
    next_number = start_number

    while sequence[len(sequence) - 1] != 1:
        if (next_number % 2 == 0):
            sequence.append(int(next_number / 2))
            next_number = int(next_number / 2)
        else:
            sequence.append((next_number * 3) + 1)
            next_number = (next_number * 3) + 1

    return sequence

most_terms = 0
start_number = 0

for i in range(1000000, 50000, -1):
    if (len(collatz_sequence(i)) > most_terms):
        most_terms = len(collatz_sequence(i))
        start_number = i

print(most_terms)
print(start_number)

# Answer: 837799