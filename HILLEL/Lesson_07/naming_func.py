import random

"""
def function_name(param1, param2):
    operatior 1
    operator 2
Имя функции - это ссылка на код который находится в памяти, 
поэтому к ней можно обратится из любого места программы
Также можно имя функции передать как аргумент другой функции func1(func2(a))
"""


lst = [random.randint(10, 50) for _ in range(15)]
lst1 = [random.randint(10, 50) for _ in range(15)]

def print_list(param):
    for i in range(len(param)):
        print(lst[i], '<->', end=' ')
    print()

def sum_list(param):
    s = 0
    for i in range(len(param)):
        s+= param[i]
    print('Summa:', s)
    return s # return возвращает только ОДНО значение!
    # return выполняет 2 действия: 1. останавливает работу функции и предает
                                            # работу в точку откуда функция была вызвана,
                                            # например если у return нет параметра
                                         #  2. возвращает значение переменной


def multi_func(my_list):
    s = 0
    p = 1
    for element in my_list:
        s += element
        p += element
    return s, p # return возвращает только ОДНО значение! на выходе из фунции пременные упакованы в кортеж





# for i in range(len(lst)):
#     print(lst[i], '->', end = ' ')
# print()
print_list(lst)
"""
# вот так можно изменять элементы списка при выводе
"""
lst = [el+5 for el in lst]
print_list(lst)
# for i in range(len(lst)):
#     print(lst[i], '->', end = ' ')
# print()

lst= [el*2 for el in lst]
print_list(lst)
print_list(lst1)
# for i in range(len(lst)):
#     print(lst[i], '->', end = ' ')
# print()
print(sum_list(lst))
print(sum_list(lst1))

x = sum_list(lst)
y = sum_list(lst1)
res = sum_list(lst) + sum_list(lst1)
print(x, y, x+y, res)

z = multi_func(lst) #передача кортежа в переменную
print(z, z[0], z[1]) # распечатан кортеж и его элементы отдельно
b,c = z # распаковка элементов кортежа в переменные
print(b,c)
print()

a,b = multi_func(lst) # распаковка результатов функции из кортежа в переменные
print(a,b)

