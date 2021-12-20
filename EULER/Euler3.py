"""
Простые делители числа 13195 - это 5, 7, 13 и 29.

Каков самый большой делитель числа 600851475143, являющийся простым числом?
6857 - 0.4267611503601074
"""

def my_sol_euler3(n): # includs simplification time 8 -5
    import math

    col = 0
    w = n
    for i in range(3, int(math.sqrt(n)), 2):
        while w % i == 0:
            #print(i, end=' ')
            w /= i
            col = i

    #print()
    return col


def not_my_sol_euler3(n): #0,0017
    f = 3
    while (n > 1):
        if n % f == 0:
            n /= f
        else:
            f += 2
    return f

def main():

    from time import time
    start = time()
    n = 600851475143
    #print(my_sol_euler3(n))
    print(not_my_sol_euler3(n))




    end = time()
    print(end - start)

if __name__ == '__main__':
    main()

