# """
# Doc sting of module 'mod1'
# """
# # import
# import random
# import sys
# import sys as v
# import sys as w
# import lesson_03.ESCAPE as p1
#
# from sys import getsizeof
# from sys import getsizeof as gs
#
#
#
# f = 9.8
# b = True
# i = 45
# print('FLOAT', getsizeof(f))
# print('BOOL', gs(b))
# print('INT', gs(i))
#
#
# print(p1.s)
#
# d = 0
#
# print(v.float_info)
# print(w.getsizeof(int))
#
#
# def func1():
#     pass
#
#
# print(dir())
# print(__doc__)
# print(__file__)
# print(__name__)
# print(random.randint(10, 99))
# # print(sys.int_info)
#
# # 1. Current dir
# # 2. PYTHONPATH
# # 3. Installation dir of Python
# # 4. vevn
#

from sys import *
from os import *
import os

print(dir(os))


def func2():
    # from os import *
    import sys