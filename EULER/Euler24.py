"""
A permutation is an ordered arrangement of objects.
For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4.
If all of the permutations are listed numerically or alphabetically, we call it lexicographic order.
The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""
from itertools import product, combinations,permutations, islice
from time import time

def my_sol():
    return int(''.join(str(list(islice(permutations(range(10), 10), 999999, 1000000))).strip('()[]').split(', ')))

def main():

    start = time()
    print(my_sol())
    end = time()
    print('время ', end-start)


if __name__ == '__main__':
    main()