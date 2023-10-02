# The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.
# Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.

from time import time
start = time()

total = 0
for i in range(1, 1001):
    total += (i ** i)
print(int(str(total)[-10:]))

print(time() - start)

# Answer: 9110846700
