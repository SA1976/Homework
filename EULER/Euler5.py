"""
2520 - самое маленькое число, которое делится без остатка на все числа от 1 до 10.

Какое самое маленькое число делится нацело на все числа от 1 до 20?
232792560
"""
import math
from time import time
from math import sqrt, log, gcd, lcm
from functools import reduce

def nod(a, b):
    while a % b != 0:
        a, b = b, a % b

    return b

def my_sol():
    c = 1

    for i in range(2,21):
        if i > c:
            nok = (i * c) // nod(i, c)
        else:
            nok = (i * c) // nod(c, i)
        c = nok

    print(c)

def my_sol_mod(): # используется встроенное gcd
    c = 1
    for i in range(2,21):
        if i > c:
            nok = (i * c) // gcd(i, c)
        else:
            nok = (i * c) // gcd(c, i)
        c = nok

    print(c)

def eratosfen_new(n): # список простых нечетных чисел до n (в списке нет 1 и 2 )
        # решето с одним списком - медленное из-за убирания 0 в конце
    l_a = [i for i in range(1, n + 1, 2)] # наполняем последовательность числами до n

    i = 1
    fin = len(l_a)-1
    while i <= fin:
        if l_a[i] != 0: # проверяем существует ли еще такое число в списке
            for j in range(i+l_a[i], fin, l_a[i]):
                    l_a[j] = 0 # убираем кратные до конца списка
        i += 1
    l_a[0] = 2
    return list(filter(lambda x: x != 0, l_a)) # убираем 0 из списка

def quick_LCM_by_log(n):
    primes = eratosfen_new(n) #returns list of all primes <=N
    sqrtN = sqrt(n)
    rez = 1
    for p in primes:
        if p <= sqrtN:
            rez *= p**(int(log(n)/log(p)))
        else:
            rez *= p
    return rez

def main():

    start = time()
    my_sol()
    end = time()
    print(end - start)

    start = time()
    my_sol_mod()
    end = time()
    print(end - start)

    start = time()
    print(quick_LCM_by_log(20))
    end = time()
    print(end - start)

    start = time() # интересное применение *
    print(lcm(*range(1, 21)))
    end = time()
    print(end - start)
if __name__ == '__main__':
    main()