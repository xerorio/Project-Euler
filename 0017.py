# If the numbers 1 to 5 are written out in words: one, two, three, four, five,
# then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words,
# how many letters would be used?

# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains
# 23 letters and 115 (one hundred and fifteen) contains 20 letters.
# The use of "and" when writing out numbers is in compliance with British usage.

dictionary = {
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine',
    '10': 'ten',
    '11': 'eleven',
    '12': 'twelve',
    '13': 'thirteen',
    '14': 'fourteen',
    '15': 'fifteen',
    '16': 'sixteen',
    '17': 'seventeen',
    '18': 'eighteen',
    '19': 'nineteen',
    '20': 'twenty',
    '30': 'thirty',
    '40': 'forty',
    '50': 'fifty',
    '60': 'sixty',
    '70': 'seventy',
    '80': 'eighty',
    '90': 'ninety'
}

def split(word: str) -> list:
    return [c for c in word]

def calculate_length(n: str) -> int:
    if len(n) == 1:
        length = len(dictionary[n])
    elif len(n) == 2:
        if int(n) < 20:
            length = len(dictionary[n])
        else:
            tens_num = f'{split(n)[0]}0'
            if split(n)[1] != '0':
                ones_num = split(n)[1]
                length = len(f'{dictionary[tens_num]}{dictionary[ones_num]}')
            else:
                length = len(f'{dictionary[tens_num]}')
    elif len(n) == 3:
        if n[-2:] != '00':
            if int(n[-2:]) < 20:
                length = len(dictionary[str(int(n[-2:]))])
            else:
                tens_num = f'{split(n)[1]}0'
                if split(n)[2] != '0':
                    ones_num = split(n)[2]
                    length = len(f'{dictionary[tens_num]}{dictionary[ones_num]}')
                else:
                    length = len(f'{dictionary[tens_num]}')
            length += len(dictionary[n[0]])
            length += 10 # hundred and
        else:
            length = len(dictionary[n[0]])
            length += 7 # hundred
    return length

total_length = 0
for i in range(1, 1000):
    total_length += calculate_length(str(i))
total_length += 11 # adding one thousand
print(total_length)

# Answer: 21124