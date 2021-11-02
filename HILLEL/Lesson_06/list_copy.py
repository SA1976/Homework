import random
import pprint
import copy

#
# spisok = [random.randint(0, 99) for _ in range(int(input('Enter list length: ')))]
# print(spisok)
# print()

lst = [83, 97, 97, 11, 88, 72, 25, 71, 15, 36, 92, 7, 46, 17, 73]

print(lst)

a= 8
b= a

lst1 = lst

print(id(lst), id(lst1))
print(lst)
print(lst1)
lst[4] = 888
print (lst)
print(lst1)

lst2 = []

for i in range(len(lst)):
    lst2.append(lst[i])

print(lst2, id(lst2))
lst[8] = 999
print(lst, id(lst))
print(lst2, id(lst2))

lst3 = lst[:] + [0]
print(lst, id(lst))
print(lst3, id(lst3))

lst4 = lst.copy()
print(lst4, id(lst4))

matrix = []
for _ in range(5):
    matrix.append([random.randint(10,99) for _ in range(6)])
print(matrix)

pprint.pprint(matrix)

print(matrix[0])
print(matrix[0][4])



for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j], end= ' ')
    print()


lst6 = [
    [47, 98, 19, 80, 27, 76],
    [16, 22, 46, 84, 45, 77],
    [78, 63, 67, 30, 91, 26],
    [40, 60, 48, 14, 22, 98],
    [34, 36, 49, 44, 23, 11]
]

print(id(lst[6]))
pprint.pprint(lst6)
lst7 = lst6.copy()
print(id(lst7))
pprint.pprint(lst7)

lst6[3][5] = 555
pprint.pprint(lst7)
print()

lst8 = copy.deepcopy(lst6)
pprint.pprint(lst8)
print()
lst6[2][3] = 11111
pprint.pprint(lst6)
print()
pprint.pprint(lst8)