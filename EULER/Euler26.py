"""
A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators
2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle.
It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
"""

from decimal import *
from time import time

def check(tst, n):
    flag = False
    lst = []
    if len(tst) == n:
        for i in range(len(tst)):
            lst += tst[i]
            if lst[0] == tst[i] and i != 0 and i % 2 == 0:
                tmp = len(lst) // 2
                if lst[tmp:-1] == lst[:tmp]:
                    lst = ''.join(lst[:tmp])
                    flag = True
                    return flag, lst
    return flag, lst

def my_sol(precis):
    getcontext().prec = precis
    max_id, max_len = 0, 0
    for i in range(2, 1000):
        num = str(1 / Decimal(i)).strip('0.')
        # print(i, num)
        flag, seq_num = check(num, precis)
        if flag:
            l = len(seq_num)
            # print(f' {i} длина {l}: {seq_num}')
            if l > max_len:
                max_len = l
                max_id = i
    print(f'макс i: {max_id}, макс длина {max_len}')
        # else:
        #     print('нет последовательности')

def main():
    precis = 2000
    start = time()
    my_sol(precis)
    end = time()
    print('время: ', end - start)


if __name__ == '__main__':
    main()





