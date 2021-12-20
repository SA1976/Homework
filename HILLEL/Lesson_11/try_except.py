"""
try:
    operator_1
    operator_2
    operator_3
    operator_4
    .
    .
    .
    operator_N
except TypeError_1 as ex:
    # logging issues
except TypeError_2 as ex:
    # logging issues
except TypeError_3 as ex:
    # logging issues
     Перехват ошибки позволяет продолжить выполнение оставшегося кода
      и не приведет к аварийному сбою в программе
Эксепты применяются по очереди, начианя с первого - выстраивание очередности очен важно
Потому что ошибки являются классами и если родительский класс будет стоять до младшего, он все ошибки заберёт на себя

Кроме эксепшенов в блоке ошибок существуют ворнинги
"""


z = 0
while True:
    try:
        x = int(input('Please enter first value: '))
        y = int(input('Please enter second value: '))
        z = x / y
        # break
    except ZeroDivisionError as ex: #  в блоке except указывается тот тип ошибки который мы хотим поймать
        print('Error:', ex)         # некоторый код который должен выполяться в случае перхвата ошибки
    except ValueError as ex:
        print('Error:', ex)
    else:                               # необязательный оператор
        print('No errors')
        break
    finally:                            # необязательный оператор
        print('Finally block')

print('Result:', z)


"""
находится на python.org
FloatingPointError
        |
  OverflowError
        |
ZeroDivisionError
        |
  ArithmeticError
        |
    Exception
"""
print(dir())
print(__file__)
