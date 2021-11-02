# При помощи вложенных циклов (можно while, можно for) и оператора IF
# нарисовать фигуры представленные ниже. Пользователь вводит, с клавиатуры,
# высоту фигуры в символах.
#
#   A         *
#           *   *
#         *       *
#       *           *
#     *               *
#   *                   *
# * * * * * * * * * * * * *

h = int(input('triangle height?:'))

for i in range(h):
    for j in range(h * 2-1):
        if j == h - i - 1 or j == h + i - 1 or i == h - 1:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
