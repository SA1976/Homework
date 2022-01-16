# 'str' in type(param_1)
import typing


def func(param_1):
    # param_1.append(45)
    if isinstance(param_1, str):
        print('String')
    elif isinstance(param_1, bool):
        print('Boolean')
    elif isinstance(param_1, int):
        print('Integer')
    elif isinstance(param_1, float):
        print('Float')
    elif isinstance(param_1, typing.List):
        param_1.append(56)
        print('List')
    else:
        print('Unknown type of data')


func(23)
func(45.7)
func(True)
func('Hello')
lst = []
func(lst)

print(type(True))


def func2(p1: int, p2: str, p3: typing.List):
    pass


func2(34, 'Hello', [6, 7])
func2('Hello', [4, 6], 56)