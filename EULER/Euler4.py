"""
Число-палиндром с обеих сторон (справа налево и слева направо) читается одинаково.
Самое большое число-палиндром, полученное умножением двух двузначных чисел – 9009 = 91 × 99.
Найдите самый большой палиндром, полученный умножением двух трехзначных чисел.

abccba
100000a + 10000b + 1000c + 100c + 10b + a
100001a + 10010b + 1100c
11(9091a + 910b + 100c) - поэтому одно из чисел произведения делится на 11 и находится в диапазоне 990 - 110

993 x 913 = 906609
0.0547940731048584

"""


import pprint
from time import time
from timeit import timeit
import math



# def my_first_sol():
#     # dict = {}
#     # lst = []
#     counter = 0
#     for i in range(330,999):
#         for j in range(303,999):
#             n = i * j
#             if str(n) == str(n)[::-1]:
#                # dict[n] = str(i) + ' x ' + str(j)
#                #lst.append(n)
#                if n > counter:
#                    counter = n
#
#     print(f'{i} x {j} = {counter}')
#
#     # print(len(dict))
#     # print(dict)
#     # print()
#     # print(set(lst))
#     #print(lst)

def my_sol():
    counter = 0
    flag = False
    for i in range(999, 100, -1):
        for j in range(990, 110, -11):
            n = i * j
            if n > counter:
                n_str = str(n)
                if n_str == n_str[::-1]:
                   counter = n
                   max_i, max_j = i, j
            else:
                break

    print(f'{max_i} x {max_j} = {counter}')


def mysol_while():
    counter = 0
    # max_i, max_j = 0, 0
    i = 999
    while i > 100:
        j = 990
        while j > 110:
            n = i * j
            if n > counter:
                n_str = str(n)
                if n_str == n_str[::-1]:
                   counter = n
                   max_i, max_j = i, j
            else:
                break
            j -= 11
        i -=1
    print(f'{max_i} x {max_j} = {counter}')


def pol_gen():
    for a in range(9, 0, -1):
        for b in range(9, -1, -1):
            for c in range(9, -1, -1):
                n = 100001 * a + 10010 * b + 1100 * c
                yield n

def my_sol_gen_usage():

    for i in range (990, 110, -11)
        gen = next(pol_gen())
        if gen % i == 0





def test(): # перебираеются 6-значные числа, ищутся палиндромы, а затем проверяются на делимость
    for i in range(999999,99999,-1):
        i_str = str(i)
        if i_str == i_str[::-1]:
            for j in range(999,99,-1):
                if (i % j == 0) and (i / j < 1000): # делится ли нацело и второй делитель является 3-х значным числом
                    return i

def test_2():
    for a in range(9, 0, -1):
        for b in range(9, -1, -1):
            for c in range(9, -1, -1):
                n = 100001 * a + 10010 * b + 1100 * c
                for k in range(999, math.floor(n ** (1 / 2)), -1):
                    if (n % k == 0):
                        return [n, k]

def main():

    start = time()
    #my_first_sol() # создает словарь всех палиндромов
    my_sol() # начинаем сверху вниз, второй цикл уменьшается на 11, убираем двойное использование str
    end = time()
    print(end - start)

    start = time() # циклы while  получаются медленне чем for
    mysol_while()
    end = time()
    print(end - start)

    start = time()
    print(max([x*y for x in range(999, 100, -1) for y in range(990, 110, -11) if str(x*y) == str(x*y)[::-1]]))
    end = time()
    print(end - start)


    start = time() # создаем сначала палиндромы, а затем проверяем их
    print(test())
    end = time()
    print(end - start)

    start = time() # создаем палиндромы по формуле и проверяем их
    print(test_2())
    end = time()
    print(end - start)


if __name__ == '__main__':
    main()














