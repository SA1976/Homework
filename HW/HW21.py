"""
Написать функцию arithmetic, принимающую 3 аргумента: первые 2 - числа, третий - операция, которая должна быть
произведена над ними. Функция должна вернуть результат вычислений зависящий от третьего аргумент:
+ сложить их;
- вычесть;
* умножить;
/ разделить (первое на второе).
В остальных случаях вернуть строку "Неизвестная операция".

"""


def arithmetic(first, second, math_op):
    if math_op == '+':
        result = first + second
    elif math_op == '-':
        result = first - second
    elif math_op == '*':
        result = first * second
    elif math_op == '/':
        if second == 0:
            result = 'Not possible to divide by 0'
        else:
            result = first / second
    else:
        result = 'Unknown operation'

    return result


a = float(input('Enter first number: '))
b = float(input('Enter second number: '))
c = input('Enter math operation +, -, *, /: ')
print()

print(arithmetic(a, b, c))
