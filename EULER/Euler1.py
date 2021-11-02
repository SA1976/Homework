col_list = []
col = 0
for i in range(999, 0, -1):
    if i % 3 == 0 or i % 5 == 0:
        col += i
        col_list.append(i)

print(col)
print(col_list)

# ниже, простое, но неправильное решение
# a = (list(range(0, 1000, 3)))[::-1]
# b = (list (range(0, 1000, 5)))[::-1]
#
#
#
# #a = a + b
# c1 = sorted(a+b, reverse=True)
# # for el in c1:
# #     if el not in col_list:
# #       print(el)
#
# print(c1)