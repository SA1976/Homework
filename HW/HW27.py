"""
Написать функцию для перевода десятичного числа в другую систему исчисления (2-36).
Небольшая подсказка. В этой задаче вам понадобится:
- список
- метод `revers()` (или срез [::-1]). Если не хотите переворачивать список остатков, тогда воспользуйтесь функцией
`insert()` и добавляйте остатки в начало списка
-`join()` для склейки элементов списка остатков в строку
- строка `ascii_uppercase` из модуля `string` (её можно получить если сделать импорт
from string import ascii_uppercase`), она содержит все буквы латинского алфавита.

Алгоритм преобразования десятичного числа в другую систему счисления можно найти в интернете. Например вот здесь.
"""
from string import ascii_uppercase


def dvn(x, dig_str, n=2):
    a = ''
    # print(bin(x))
    while x > 0:
        a += dig_str[x % n]
        x //= n
    a = a[::-1]

    return a


def main():

    while True:  # проверка конвертируемого числа на корректность
        try:
            flag = False
            while not flag:
                x = int(input('Please enter positive int value: '))
                if x < 0:
                    print('Not positive value')
                    flag = False
                else:
                    flag = True
        except ValueError as ve:
            print('Not int value: ', ve)
        else:
            break

    while True:  # проверка базы исчисления на корректность
        try:
            flag = False
            while not flag:
                n = int(input('Please enter base for numeral system - int value from 2 to 36: '))
                if n < 2 or n > 36:
                    print('Base not between 2 and 36, try again')
                    flag = False
                else:
                    flag = True
        except ValueError as ve:
            print('Incorrect int value: ', ve)
        else:
            print()
            break

    dig_str = ''  # создаем строку откуда будем брать "цифры"
    for i in range(10):
        dig_str += str(i)
    dig_str += ascii_uppercase

    dv = dvn(x, dig_str, n)
    print(f' {x} in {n}-base numeral system = {dv}')

    # for n in range(2, 37): # тут можно вывести вообще все варианты
    #     dv = dvn(x, dig_str, n)
    #     print(f' {x} in {n}-base numeral system = {dv}')


if __name__ == '__main__':
    main()
