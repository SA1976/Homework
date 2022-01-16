"""
Выписав первые шесть простых чисел, получим
2, 3, 5, 7, 11 и 13. Очевидно, что 6-е простое число - 13.

Какое число является 10001-м простым числом? 104743
"""

from time import time
from math import sqrt, log, floor


def my_sol(n): # формирует список простых чисел до n
    prime_list = list(0 for _ in range(n))
    prime_list[0] = 2
    candidate = 3
    idx = 1
    while prime_list[-1] == 0:
        check = True
        fin = int(sqrt(candidate))+1
        for i in range(3, fin, 2):
            if candidate % i == 0:
                check = False
                break
        if check:
            prime_list[idx] = candidate
            idx += 1
        candidate += 2
    print(prime_list[-1])

def my_sol_mod(n): # убран список - выдает только последнее значение

    candidate = 3
    idx = 1
    while True:
        check = True
        fin = int(sqrt(candidate))+1
        for i in range(3, fin, 2):
            if candidate % i == 0:
                check = False
                break
        if check:
            idx += 1
            if idx == n:
                break
        candidate += 2
    print(candidate)

def euler_sol(m): # решето с булевым списком
    def eratosthene(n):
        isPrime = [True] * (n + 1)
        primes = []
        for i in range(2, n + 1):
            if isPrime[i]:
                for j in range(i, n + 1, i):
                    isPrime[j] = False
                primes.append(i)
        print(isPrime)
        return primes

    def primeNumb(n):
        limit = n * (log(n) + log(log(n)) - 0.5)
        primes = eratosthene(floor(limit))
        print(primes)
        return primes[n - 1]

    print(primeNumb(m))


def main():
    n = 10001
    # start = time()
    # my_sol(n)
    # end = time()
    # print(end - start)
    #
    # start = time()
    # my_sol_mod(n)
    # end = time()
    # print(end - start)

    start = time()
    euler_sol(n)
    end = time()
    print(end - start)

if __name__ == '__main__':
    main()