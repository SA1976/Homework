"""
Написать функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения:
периметр квадрата, площадь квадрата и диагональ квадрата.
"""
import math

def square(side):

    area = side**2
    perimetr = side * 4
    diagonal = math.sqrt(2 * side**2)

    return area, perimetr, diagonal

a1 = float(input('Square side? '))

if a1 <= 0:
    print('Incorrect number')
else:
    a, p, d = square(a1)
    print('Square area:', a, '\nSquare perimetr:', p, '\nSquare diagonal:', round(d, 2))
