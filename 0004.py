# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

# takes the input number and takes the last digit (num % 10) and adds it to the reversed number after
# multiplying it by 10. 
def reverseDigits(num) -> int:
    rev_num = 0
    while (num > 0):
        rev_num = rev_num * 10 + num % 10
        num = num // 10
    return rev_num

def isPalindromic(input_num) -> bool:
    if (reverseDigits(input_num) == input_num):
        return True
    else:
        return False

three_digit_palindromes = []

for i in range(100, 1000):
    for j in range(100, 1000):
        number = i * j
        if (isPalindromic(number)):
            three_digit_palindromes.append(number)

largest_number = 0

for i in range(1, len(three_digit_palindromes) - 1):
    if (three_digit_palindromes[i] > three_digit_palindromes[i-1]):
        largest_number = three_digit_palindromes[i]

print(largest_number)

# Answer: 906609