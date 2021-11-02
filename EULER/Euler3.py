"""
Простые делители числа 13195 - это 5, 7, 13 и 29.

Каков самый большой делитель числа 600851475143, являющийся простым числом?

"""
import math

n = int(input('enter number: '))
col = 0
w = n
for i in range(2, int(math.sqrt(n))):
    while w % i == 0:
        print(i, end=' ')
        w /= i
        col = i

print()
print(col)

# num = n
# count = 1
#
# while num != 1:
#     count += 1
#     if num % count == 0:
#         num /= count
#         if num == 1:
#             print(count)





