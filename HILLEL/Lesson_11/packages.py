
# import lesson_10.mod1
# import lesson_10.p1.p1_1.m1 as module1

# from lesson_10.p1.p1_1 import m1 as M1
# from lesson_10.p1.p1_1.m1 import PI

from lesson_10.p1.p1_1.m1 import *
from lesson_10.p1.p1_1 import *


# print(lesson_10.p1.p1_1.m1.PI)
# print(module1.PI)
# print(M1.PI)
# print(PI)
# print(test_line)
# from math import *
print(dir())


def square_circle(r):
    from math import pi
    return pi * (r ** 2)