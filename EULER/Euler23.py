"""
A perfect number is a number for which the sum of its proper divisors is exactly
 equal to the number. For example, the sum of the proper divisors of 28 would
  be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n
 and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest
number that can be written as the sum of two abundant numbers is 24.
By mathematical analysis, it can be shown that all integers greater than 28123
can be written as the sum of two abundant numbers. However, this upper limit
cannot be reduced any further by analysis even though it is known that the
greatest number that cannot be expressed as the sum of two abundant numbers
is less than this limit.

Find the sum of all the positive integers which cannot be written as the
sum of two abundant numbers.
28122 - крайнее избыточное число, следующее 28128, 28134
пропустил 945 - оно не является суммой предидущих значений, хотя является избыточным числом
4179871
"""

from sympy import proper_divisors
from time import time

def my_sol(n):

    lst = [i for i in range(1, n + 1) if sum(proper_divisors(i)) > i]

    full_set = set([lst[i]+lst[j] for i in range(len(lst)) for j in range(i+1) if lst[i]+lst[j] < n])

    return sum(num for num in range(1, n) if num not in full_set)

def my_sol2(n):
    pass
    lst = [i for i in range(1, n + 1) if sum(proper_divisors(i)) > i]


    full_set = set()

    for i in range(len(lst)):
        for j in range(i+1):
            if lst[i]+lst[j] < n:
                full_set.add(lst[i]+lst[j])


    return sum(num for num in range(1, n) if num not in full_set)


def main():

    n = 28123
    start = time()
    print(my_sol(n))
    end = time()
    print('время ', end-start)

    start = time()
    print(my_sol2(n))
    end = time()
    print('время ', end-start)
if __name__ == '__main__':
    main()
