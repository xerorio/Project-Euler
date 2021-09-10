# The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.
# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
# (Please note that the palindromic number, in either base, may not include leading zeros.)

from module import is_palindromic, bin_is_palindrome

palindrome_sum = 0

for n in range(1, 1000000):
	if is_palindromic(n):
		if bin_is_palindrome(n):
			palindrome_sum += n

print(palindrome_sum)

# Answer: 872187