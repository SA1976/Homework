"""
Число-палиндром с обеих сторон (справа налево и слева направо) читается одинаково.
Самое большое число-палиндром, полученное умножением двух двузначных чисел – 9009 = 91 × 99.
Найдите самый большой палиндром, полученный умножением двух трехзначных чисел.

"""
import pprint
from time import time
start = time()


dict = {}
lst = []
counter = 0
for i in range(330,999):
    for j in range(303,999):
        n = i * j
        if str(n) == str(n)[::-1]:
           dict[n] = str(i) + ' x ' + str(j)
           #lst.append(n)
           if n > counter:
               counter = n

print(counter)
print(len(dict))
print(dict)
# print()
# print(set(lst))
#print(lst)

end = time()

print(end - start)













# num1 = 999
# num2 = 999
# polist = list()
# i = 0
#
# while num2 > 316:
#     pol = num1 * num2
#     pol1 = pol // 1000
#     pol2 = pol % 1000
#     revpol2 = int(str(pol2)[::-1])
#     if pol1 == revpol2 and pol > 100000:
#         polist.insert(i, pol)
#         i += 1
#     num1 -= 1
#     if num1 < 316:
#         num1 = 999
#         num2 -= 1
#
# polist.sort(reverse=True)
# print(len(polist))


