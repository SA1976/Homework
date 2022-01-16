"""
Surprisingly there are only three numbers that can be written as the
sum of fourth powers of their digits:

1634 = 1^4 + 6^4 + 3^4 + 4^4
8208 = 8^4 + 2^4 + 0^4 + 8^4
9474 = 9^4 + 4^4 + 7^4 + 4^4
As 1 = 14 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written
as the sum of fifth powers of their digits.

# digits5=[num**5 for num in range(0,10)] # готовые степени цифр до 1..9
# print(digits5)
# #
# # limit = 6*pow(9,5) # 6 цифр с макс значением 9**5 = 354294
# # combinations_with_replacement - дает 5005 уникальных набора 10 цифр в 6 разрядах
# # eybrf
# # print(limit)
# c = combinations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 6)
# c1 = combinations_with_replacement([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 6)
# p = permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 6)
# print(len(list(c)))
# print(len(list(c1)))
# print(len(list(p)))
[1, 4150, 4151, 54748, 92727, 93084, 194979]
"""


from itertools import combinations_with_replacement
from time import time


def mu_sol_mod():
    print([num for num in range(1, 500_000) if sum(pow(int(i),5) for i in str(num)) == num])
    return sum([num for num in range(1, 500_000) if sum(pow(int(i),5) for i in str(num)) == num])

def uniq_digits_set():

    tmp = list(combinations_with_replacement([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 6))
    for i in range(len(tmp)):
        yield int(str(tmp[i]).strip('()').replace(', ', ''))


def my_sol_2():

    powers = [num**5 for num in range(0,10)]
    limit_of_combinations = 5005 # 5005 макс кол-во уникальных комбинаций
    limit_of_digits = 6*(pow(9,5))
    gen = uniq_digits_set()
    rez_lst=[]
    for i in range(limit_of_combinations):
        base = next(gen)
        candidate = sum(powers[int(el)] for el in str(base))
        if candidate < limit_of_digits:
            if candidate == sum(powers[int(el)] for el in str(candidate)):
                rez_lst.append(candidate)
    print(rez_lst)
    return sum(rez_lst)


def main():

    start = time()
    print(mu_sol_mod())
    end = time()
    print('время: ', end - start)

    start = time()
    print(my_sol_2())
    end = time()
    print('время: ', end - start)


if __name__ == '__main__':
    main()




# def euler_sol():
# def digit_combos(n=6, start=0, stop=9):
#     if n == 1:
#         return [str(x) for x in range(start, stop + 1)]
#     else:
#         combos = []
#         for sub_combo in digit_combos(n-1, start, stop):
#             for i in range(start, int(sub_combo[0])+1):
#                 combos.append(str(i) + sub_combo)
#         return combos
#
# d = digit_combos()