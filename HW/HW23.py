"""
Написать функцию is_year_leap, принимающую 1 аргумент — номер года, и возвращающую True, если год високосный,
и False иначе.
Отсюда следует распределение високосных годов:

- год, номер которого кратен 400, — високосный;
- остальные годы, номер которых кратен 100, — невисокосные (например, годы 1700, 1800, 1900, 2100, 2200, 2300);
- остальные годы, номер которых кратен 4, — високосные[5].
- все остальные годы — невисокосные.

"""


def is_year_leap(year):

    if year % 400 == 0:
        leap_year = True

    elif year % 100 == 0:
        leap_year = False

    elif year % 4 == 0:
        leap_year = True

    else:
        leap_year = False

    return leap_year

def main():
    year_number = int(input('Enter year: '))

    result = is_year_leap(year_number)

    if result:
        print('Year', year_number, 'is a leap year')
    else:
        print('Year', year_number, 'is not a leap year')

if __name__ == '__main__':
    main()