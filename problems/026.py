# A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:
#     1/2	= 	0.5
#     1/3	= 	0.(3)
#     1/4	= 	0.25
#     1/5	= 	0.2
#     1/6	= 	0.1(6)
#     1/7	= 	0.(142857)
#     1/8	= 	0.125
#     1/9	= 	0.(1)
#     1/10	= 	0.1
# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.
# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

def cycle_length(denominator):
    numerator = 1
    remainders = []
    while len(remainders) == len(set(remainders)):
        print(remainders)
        remainder = numerator % denominator
        remainders.append(remainder)
        numerator = remainder * 10
    return len(set(remainders))

# max_denominator = 0
# counter = 0
# for i in range(2, 1000):
#     if cycle_length(i) > counter:
#         counter = cycle_length(i)
#         max_denominator = i
# print(max_denominator)
cycle_length(982)

# Answer: 983
