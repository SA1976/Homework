"""
Написать функцию season, принимающую 1 аргумент — номер месяца (от 1 до 12),
и возвращающую время года (в виде строки), которому этот месяц принадлежит (зима, весна, лето или осень).

"""


def season(month_number):
    s = ''
    if month_number == 12 or month_number == 1 or month_number == 2:
        s = 'winter'
    elif 3 <= month_number <= 5:
        s = 'spring'
    elif 6 <= month_number <= 8:
        s = 'summer'
    elif 9 <= month_number <= 11:
        s = 'autumn'
    return s


a = int(input('Enter month: '))
if a < 1 or a > 12:
    print('Incorrect number')
else:
    print('Season is', season(a))
