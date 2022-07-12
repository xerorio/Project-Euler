# You are given the following information, but you may prefer to do some research for yourself.
# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century
# unless it is divisible by 400.
# How many Sundays fell on the first of the month during the twentieth century
# (1 Jan 1901 to 31 Dec 2000)?

counter = 0

class Date():
    def __init__(self, day, date, month, year):
        self.day = day
        self.date = date
        self.month = month
        self.year = year

current_day = Date(2, 1, 1, 1901)

while current_day.year < 2001:
    current_day.day += 1
    current_day.date += 1

    if current_day.day == 8:
        current_day.day = 1
    
    if (current_day.date == 31 and 
            (current_day.month == 4 or
            current_day.month == 6 or
            current_day.month == 9 or
            current_day.month == 11)):
                current_day.date = 1
                current_day.month += 1
    elif (current_day.date == 32 and
        (current_day.month == 1 or
        current_day.month == 3 or
        current_day.month == 5 or
        current_day.month == 7 or
        current_day.month == 8 or
        current_day.month == 10 or
        current_day.month == 12)):
            current_day.date = 1
            current_day.month += 1
    
    # a leap year
    if ((str(current_day.year)[-2:] == '00' and current_day.year % 400 == 0) or
        (str(current_day.year)[-2:] != '00' and current_day.year % 4 == 0)):
        if (current_day.date == 30 and current_day.month == 2):
            current_day.date = 1
            current_day.month = 3
    else:
        if (current_day.date == 29 and current_day.month == 2):
                current_day.date = 1
                current_day.month += 1
    
    if current_day.month == 13:
        current_day.month = 1
        current_day.year += 1
    
    if current_day.day == 7 and current_day.date == 1:
        counter += 1
    
    print(f'{current_day.day} {current_day.date} {current_day.month} {current_day.year}')

print(counter)

# Answer: 171
