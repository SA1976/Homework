"""
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
1990 - 1996 - 2001 - 2007 - 20018
"""

from HW.HW23 import is_year_leap
a = 0
cllctr = 0
mnth = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

for year in range(1900, 2001):
    for month in mnth:
        if month == 'Feb':
            if is_year_leap(year):
                days = 29
            else:
                days = 28
        elif month == 'Apr' or month == 'Jun' or month == 'Sep' or month == 'Nov':
            days = 30
        else:
            days = 31
        for i in range(1, days + 1):
            a += 1
            if year > 1900 and a == 7 and i == 1:
                cllctr +=1
                print(year, month, i , a)
            if a == 7:
                a = 0

print(cllctr)
