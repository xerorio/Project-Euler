# 2520 is the smallest number that can be divided by each of the numbers from
# 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# incrementing by 20 as that is the largest number that it must be divisble by
# between 100,000,000 and 999,999,999
for i in range(100000000, 1000000000, 20):
    if (i % 11 == 0):
        if (i % 13 == 0):
            if (i % 14 == 0):
                if (i % 15 == 0):
                    if (i % 16 == 0):
                        if (i % 17 == 0):
                            if (i % 18 == 0):
                                if (i % 19 == 0):
                                    print(i)
                                    break

# Answer: 232792560