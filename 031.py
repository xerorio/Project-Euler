# In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins in general circulation:

#     1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).

# It is possible to make £2 in the following way:

#     1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

# How many different ways can £2 be made using any number of coins?

from time import time
start = time()

# 1: 200
# 2: 100
# 5: 40
# 10: 20
# 20: 10
# 50: 4
# 100: 2
# 200: 1

# 1 for £2 coins
count = 1

# 100p coins
for a in range(3):
    # 50p coins
    for b in range( int(1 + ((200 - (100 * a)) / 50)) ):
        # 20p coins
        for c in range( int(1 + ((200 - (100 * a) - 50 * b) / 20)) ):
            # 10p coins
            for d in range( int(1 + ((200 - (100 * a) - (50 * b) - (20 * c)) / 10)) ):
                # 5p coins
                for e in range( int(1 + ((200 - (100 * a) - (50 * b) - (20 * c) - (10 * d)) / 5)) ):
                    # 2p coins
                    for f in range( int(1 + ((200 - (100 * a) - (50 * b) - (20 * c) - (10 * d) - (5 * e)) / 2)) ):
                        count += 1

print(count)

print(time() - start)

# Answer: 73682
