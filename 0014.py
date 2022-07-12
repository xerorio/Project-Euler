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

def generate_sequence(x):
    sequence = [x]

    while x != 1:
        if x % 2 == 0:
            x /= 2
        else:
            x *= 3
            x += 1
        sequence.append(int(x))
    
    return sequence

longest_chain = 0
chain_got_longer = []
for i in range(70000, 1000000):
    if len(generate_sequence(i)) > longest_chain:
        longest_chain = len(generate_sequence(i))
        print(i)

# It's a bit slow and not too sure how to optimise
# Answer: 837799
