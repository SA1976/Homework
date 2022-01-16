"""
In the United Kingdom the currency is made up of pound (£) and pence (p).
There are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?
"""
from time import time
from pprint import pprint
from itertools import product, combinations_with_replacement

def my_sol_1(n=200): # strait and brute force
    result = set()

    limit_pence_1 = n+1
    limit_pence_2 = n//2 + 1
    limit_pence_5 = n//5 + 1
    limit_pence_10 = n // 10 + 1
    limit_pence_20 = n // 20 + 1
    limit_pence_50 = n // 50 + 1
    limit_pound_1 = n // 100 + 1

    for pound_1 in range(limit_pound_1):
        if pound_1 * 100 == n:
            result.add((0, 0, 0, 0, 0, 0, pound_1, 0))
            result.add((0, 0, 0, 0, 0, 0, 0, 1)) # добавляем 1 монету 2 фунта
            break
        for pence_50 in range(limit_pence_50):
            if pence_50 * 50 == n:
                result.add((0, 0, 0, 0, 0, pence_50, 0, 0))
                continue
            for pence_20 in range(limit_pence_20):
                if pence_20 * 20 == n:
                    result.add((0, 0, 0, 0, pence_20, 0, 0, 0))
                    continue
                for pence_10 in range(limit_pence_10):
                    if pence_10 * 10 == n:
                        result.add((0, 0, 0, pence_10, 0, 0, 0, 0))
                        continue
                    for pence_5 in range(limit_pence_5):
                        if pence_5 * 5 == n:
                            result.add((0, 0, pence_5, 0, 0, 0, 0, 0))
                            continue
                        for pence_2 in range(limit_pence_2):
                            if pence_2 * 2 == n:
                                result.add((0, pence_2, 0, 0, 0, 0, 0, 0))
                                continue
                            for pence_1 in range(limit_pence_1):
                                if pence_1 + pence_2 * 2 + pence_5 * 5 + pence_10 * 10 + pence_20 * 20 + pence_50 * 50 == n:  # + pound_1 * 100
                                    result.add((pence_1, pence_2, pence_5, pence_10, pence_20, pence_50))  # , pound_1



    print(len(result))

def my_sol_2(n=200):
    pass





def main():
    # 4562 - 1 фунт только пенсами - время с сетом: 5.515249252319336
    # 69118 - 2 фунта только пенсами - время с сетом: 384.0923330783844
    # 73680 - 2 фунта пенсами + монета 1 фунт
    # 73682 - то же + 2 монеты по 1 фунту + монета 2 фунта время: 668.5302169322968



    start = time()
    my_sol_1(200)
    end = time()
    print('время: ', end - start)


    # start = time()
    # print(my_sol_2())
    # end = time()
    # print('время: ', end - start)


if __name__ == '__main__':
    main()