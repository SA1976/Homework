"""
Эйлер опубликовал свою замечательную квадратичную формулу:

n**2+n+41

Оказалось, что согласно данной формуле можно получить 40 простых чисел,
последовательно подставляя значения 0≤n≤39. Однако, при n=40
40**2+40+41=40(40+1)+41 делится на 41 без остатка, и, очевидно,
при n=41,412+41+41 делится на 41 без остатка.

При помощи компьютеров была найдена невероятная формула n**2−79n+1601,
согласно которой можно получить 80 простых чисел для последовательных
значений n от 0 до 79. Произведение коэффициентов −79 и 1601 равно −126479.

Рассмотрим квадратичную формулу вида:
n**2+an+b, где |a|<1000 и |b|≤1000

где |n| является модулем (абсолютным значением) n.
К примеру, |11|=11 и |−4|=4

Найдите произведение коэффициентов a и b квадратичного выражения,
согласно которому можно получить максимальное количество простых
чисел для последовательных значений n начиная со значения n=0.

# for i, val in enumerate(range(100)):
#     print(i, sympy.divisors(val*val + val + 41))
# print('x'*50)
# for i, val in enumerate(range(200)):
#     print(i, sympy.divisors(val*val - 79 * val + 1601))

D=b**2−4ac те в терминах задания D=a**2-4b*1,

n**2+n+41      print(1-4*41)        # D = -163
n**2−79n+1601 print(79*79 - 4*1601) # D = -163
D = - 163
a**2-4*b = -163
b = (-163 - a**2)/-4 = (a**2 + 163)/4
a = sqrt(4b-163)

2*sqrt(2) <class 'sympy.core.mul.Mul'>
sqrt(163) <class 'sympy.core.power.Pow'>
12 <class 'sympy.core.numbers.Integer'>

{-61: 971, -59: 911, -57: 853, -55: 797, -53: 743, -51: 691, -49: 641, -47: 593, -45: 547, -43: 503, -41: 461, -39: 421, -37: 383, -35: 347, -33: 313, -31: 281, -29: 251, -27: 223, -25: 197, -23: 173, -21: 151, -19: 131, -17: 113, -15: 97, -13: 83, -11: 71, -9: 61, -7: 53, -5: 47, -3: 43, -1: 41, 1: 41, 3: 43, 5: 47, 7: 53, 9: 61, 11: 71, 13: 83, 15: 97, 17: 113, 19: 131, 21: 151, 23: 173, 25: 197, 27: 223, 29: 251, 31: 281, 33: 313, 35: 347, 37: 383, 39: 421, 41: 461, 43: 503, 45: 547, 47: 593, 49: 641, 51: 691, 53: 743, 55: 797, 57: 853, 59: 911, 61: 971}
len 62

"""
import sympy
from pprint import pprint
from time import time

def my_sol():
    # rez = {}
    max_a, max_b, max_len, lst = 0, 0, 0, []
    for a in range(-999, 1000):
        tmp = (a*a + 163)
        if (tmp // 4) <= 1000 and tmp % 4 == 0:
            b = tmp // 4
            # rez[a] = b
            # print(f'n**2 {a}*n +{b}')

            for n in range(100):
                candidate = (n*n)+(a*n)+(b)
                if sympy.isprime(candidate):
                    # pprint(candidate)
                    lst.append(candidate)
                else:
                    break

            # print(len(lst), lst)
            if len(lst) > max_len:
                max_a = a
                max_b = b
                max_len = len(lst)
            lst = []

    print(f'max_a={max_a}, max_b={max_b}, max_len = {max_len}')
    # for n in range(100):
    #     candidate = (n * n) + (max_a * n) + (max_b)
    #     if sympy.isprime(candidate):
    #         lst.append(candidate)
    #     else:
    #         break
    # print(lst)
    print(max_a*max_b)

    # print(rez)
    # print(len(rez))

def main():
    start = time()
    my_sol()
    end = time()
    print('время: ', end - start)


if __name__ == '__main__':
    main()