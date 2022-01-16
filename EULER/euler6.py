"""
Найдите разность между суммой квадратов и квадратом суммы первых ста натуральных чисел.
25164150
# # s2 = n * (n+1) * (2 * n + 1) // 6 # сумма квадратов
# # s = ((1 + n) * n // 2) ** 2 # квадрат суммы
"""
from time import time

def my_sol(n):
    s=0
    s2 = 0
    for i in range(1, n+1):
        s2 += pow(i, 2)
        s += i

    print(pow(s, 2) - s2)

def my_sol_mod(n):
    s = pow(((1 + n) * n // 2), 2)
    s2 = n * (n+1) * (2 * n + 1) // 6
    print (s - s2)

def main():
    start = time()
    my_sol_mod(100)
    end = time()
    print(end - start)

    start = time()
    my_sol(100)
    end = time()
    print(end - start)

    start = time()
    print(pow(sum([x for x in range(101)]), 2) - sum([pow(x, 2) for x in range(101)]))
    end = time()
    print(end - start)

    start = time()
    print((100 * (pow(100, 2) - 1) * (3 * 100 + 2) / 12))
    end = time()
    print(end - start)

if __name__ == '__main__':
    main()