"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19
letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115
(one hundred and fifteen) contains 20 letters.
The use of "and" when writing out numbers is in compliance with British usage.
one = 3
two = 3
three = 5
four = 4
five = 4
six = 3
seven = 5
eight = 5
nine = 4
ten = 3
eleven = 6
twelve = 6
thirteen = 8
fourteen = 8
fifteen = 7
sixteen = 7
seventeen = 9
eighteen = 8
nineteen = 8
twenty = 6
thirty = 6
forty = 5
fifty = 5
sixty = 5
seventy = 7
eighty = 6
ninety = 6
one hundred and = 3 + 7 + 3 = 13
two hundred and = 13
three hundred and = 15
four hundred and = 14
five hundred and = 14
six hundred and = 13
seven hundred and = 15
eight hundred and = 15
nine hundred and = 14
one thousand = 11
"""

units = {9: 4, 8: 5, 7: 5, 6: 3, 5: 4, 4: 4, 3: 5, 2: 3, 1: 3} # 1..9

dec = {9: 6, 8: 6, 7: 7, 6: 5, 5: 5, 4: 5, 3: 6, 2: 6,
       19: 8, 18: 8, 17: 9, 16: 7, 15: 7, 14: 8, 13: 8, 12: 6, 11: 6, 10: 3} #10.. 19, 20, 30

hundr = {9: 14, 8: 15, 7:15, 6:13, 5: 14, 4: 14, 3: 15, 2: 13, 1: 13} # 100, 200, ... 900


def brut_force (perimetr):
    c = 0
    # 21089 - 999, 21113 - 999, 21124 - 1000
    for n in range(1, perimetr + 1):

        if n // 100 == 10: # one thousand = 11
            c += 11
            n = 0

        if 9 >= n // 100 > 0 and n % 100 == 0: # только круглые сотни
            c += hundr.get(n//100) - 3 # вычитаем 'and'
            n = 0

        if 9 >= n // 100 > 0: # считаем сотни и уменьшаем n для дальнейшей обработки
            c += hundr.get(n//100)
            n %= 100

        if n // 10 == 1:  # 10 .. 19
            c += dec.get(n)
            n = 0

        elif 9 >= n // 10 > 1 and n % 10 != 0:  # число > 10 и есть остаток
            c += dec.get(n // 10)
            c += units.get(n % 10)
            n = 0

        elif 9 >= n // 10 > 1 and n % 10 == 0:  # круглые десятки
            c += dec.get(n//10)
            n = 0

        elif n > 0 and n // 10 == 0:  # число меньше 10
            c += units.get(n)

    return c

def main():
    limit = 1000
    print(brut_force(limit))


if __name__ == '__main__':
    main()













