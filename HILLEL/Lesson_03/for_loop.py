"""for (variable) in (iterable_object):
    operator1
    operator2


    for _ in (iterable_object): #тут нет переменной
    operator1
    operator2

"""

# range(start,stop,step) stop являеется обязательным параметром и не входит в перебираемый диапазон
# range (start, stop) step = 1
# range (stop) start = 0, step = 1

# range это тоже своеобразный список и можно обратится к его отдельному элементу
# print(range(3)[1])
# print(range(3)[2])

# for i in range (1, 16):
#     print(i, end=' ')
#
# print()
#
# s = "Hellow World"
# for el in s:
#     print(el, end=' ')
#
# print()

for _ in range(10):
    print('*', end=' ')
print()
# else - будет использоваться только если цикл закончится,
# если for закончится по brake, то else выполнен не будет