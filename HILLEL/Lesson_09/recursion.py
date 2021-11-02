"""
2 ^ 5 = 2 * 2 * 2 * 2 * 2
2 ^ 5 = 2 * 2^4 => 2 * 2^3 => 2 * 2^2 => 2 * 2^1 => 2 * 2^0
  32 <= 2 * 16  <= 2 * 8  <=  2 * 4  <=  2 * 2  <=  2 * 1
"""


def ipow(num, ex):
    res = 1
    while ex > 0:
        res *= num
        ex -= 1
    return res


def rpow(num, ex):
    if ex == 0:
        return 1

    return num * rpow(num, ex-1)


print(ipow(2, 5))
print(rpow(2, 5))


def ifibb(num):
    x1 = 0
    x2 = 1
    while num > 0:
        y = x1 + x2
        x1 = x2
        x2 = y
        num -= 1
    return x1


def rfibb(num):
    # if num == 0 or num == 1:
    #     return num
    #
    # return rfibb(num-2) + rfibb(num-1)

    return num if num == 0 or num == 1 else rfibb(num-2) + rfibb(num-1)


print(ifibb(10))
print(rfibb(10))