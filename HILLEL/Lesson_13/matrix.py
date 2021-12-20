from random import randint

m = int(input('Введите высоту матрицы: '))
n = int(input('Введите ширину матрицы: '))

matrix = []
for i in range(m):
    matrix.append([])
    for _ in range(n):
        matrix[i].append(randint(10, 99))

for i in range(m):
    for j in range(n):
        print(matrix[i][j], end=' ')
    print()
print()

matrix1 = [[randint(10, 99) for _ in range(n)] for _ in range(m)]
for i in range(m):
    for j in range(n):
        print(matrix1[i][j], end=' ')
    print()
print()

for i in range(m):
    tmp = 0
    for j in range(n):
        if i % 2 == 0:
            if matrix[i][j] % 2 == 0:
                tmp += matrix[i][j]
        else:
            if matrix[i][j] % 2 != 0:
                tmp += matrix[i][j]

        print(matrix[i][j], end=' ')
    print('\t\t', tmp)
print()