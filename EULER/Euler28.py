"""
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
"""
"""
                  73 74 75 76 77 78 79 80 81
                  72 43 44 45 46 47 48 49 50
                  71 42 21 22 23 24 25 26 51
                  70 41 20  7  8  9 10 27 52
                  69 40 19  6  1  2 11 28 53
                  68 39 18  5  4  3 12 29 54
                  67 38 17 16 15 14 13 30 55
                  66 37 36 35 34 33 32 31 56
                  65 64 63 62 61 60 59 58 57
"""

"""
    wolfram-alpha:
    1, 9, 25 = 4 n^2 - 4 n + 1 = (2 n - 1)^2
    1, 3, 13 = 4 n^2 - 10 n + 7 = 2 n (2 n - 5) + 7
    1, 5, 17 = 4 n^2 - 8 n + 5 = 4 (n - 2) n + 5 = n (4 n - 8) + 5 = 4 (n - 1)^2 + 1
    1, 7, 21 = 4 n^2 - 6 n + 3 = n (4 n - 6) + 3
    cумма по всем диагоналям,без учета центральной едницы = 16 n^2 - 28 n + 16
    ответ 669171001
"""

"""
первый круг  1влево - 1 вниз-  2 направо-  2 вверх - 2 влево = 3х3
второй круг  1влево - 3 вниз - 4 направо - 4 вверх - 4 влево = 5х5
третий круг  1влево - 5 вниз - 6 направо - 6 вверх - 6 влево = 7х7
4-й круг     1влево - 7 вниз - 8 направо - 8 вверх - 8 влево = 9х9

500-й круг   1влево- 999 вниз-1000 направо -1000 вверх -1000 влево=1001х1001

"""
from time import time
import numpy as np

def my_sol():
    collector = 0
    for n in range(2, 502):
        collector += 16*n*n - 28 * n + 16
    return collector+1

def my_sol2():
    return sum([16*n*n - 28 * n + 16 for n in range(2, 502)])+1

def make_spiral(n=5):

    def seq():
        i = 1
        while True:
            i += 1
            yield i

    arrr = np.zeros((n, n))
    gen = seq()
    # ставим 1 в середину
    idy, idx = n // 2, n // 2
    arrr[idy, idx] = 1

    # начиниаем с 3 так как отсчет идет от общей размерности массива
    # и это размер минимального круга
    for i in range(3, n + 1, 2):

        # move_left 1 step - шаг на 1 влево - это начало каждого круга
        idx += 1
        arrr[idy, idx] = next(gen)

        # move_down i-2 steps
        for _ in range(i - 2):
            idy += 1
            arrr[idy, idx] = next(gen)


        # move_right i - 1 steps:
        for _ in range(i - 1):
            idx -= 1
            arrr[idy, idx] = next(gen)

        # move_up i-1 steps:
        for _ in range(i - 1):
            idy -= 1
            arrr[idy, idx] = next(gen)

        # move_left i-1 steps:
        for _ in range(i - 1):
            idx += 1
            arrr[idy, idx] = next(gen)

    # np.diagonal(arrr) - главная диагональ
    # np.fliplr(arrr).diagonal() - побочная диагональ

    return sum(np.diagonal(arrr)) + sum(np.fliplr(arrr).diagonal()) - 1

def main():

    start = time()
    print(my_sol())
    end = time()
    print('время: ', end - start)

    start = time()
    print(my_sol2())
    end = time()
    print('время: ', end - start)

    start = time()
    print(make_spiral(1001))
    end = time()
    print('время: ', end - start)

if __name__ == '__main__':
    main()