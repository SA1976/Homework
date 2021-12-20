"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called
amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""
from razlojenie_na_prost_mnoj import eratosfen_sieve
from razlojenie_na_prost_mnoj import list_of_divisor

def full_set_of_divisor (n, prime_factorization):
    p = prime_factorization.keys
    rates_of_primes = prime_factorization.values
    number_of_divisors = sum(rates_of_primes)+len(rates_of_primes)+1

    for i in range(number_of_divisors):

