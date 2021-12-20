
# import HILLEL.Lesson_10.mod1
#import HILLEL.Lesson_10.P1.P1_1.m1 as module1

from HILLEL.Lesson_10.P1.P1_1 import m1 as M1
# from HILLEL.Lesson_10.P1.P1_1.m1 import PI

from HILLEL.Lesson_10.P1.P1_1.m1 import * # импорт содержимого модуля. В пространство имен добавится всё из m1
# from HILLEL.Lesson_10.P1.P1_1 import *  #  импорт содержимого пакета.
# Автоматом всё не добавится. Добавление происходит через __all_ = ['m1', 'm3'] в файле __init__.py
# Такая же перменная  __all__ может быть использована внутри модуля и будет управляять тем,
# какие функции будт импортироваться в случае import *

# print(HILLEL.Lesson_10.p1.p1_1.m1.PI)
# print(module1.PI)
# print(M1.PI)
# print(PI)
# print(test_line)
# from math import *
print(dir())



def square_circle(r):
    from math import pi #  импорт будет существовать только внутри этой функции,
    # по ее завершению все будет удалено из пространства имен модуля
    return pi * (r ** 2)