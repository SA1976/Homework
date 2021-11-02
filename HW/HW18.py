# При помощи вложенных циклов(можно
# while , можно for ) и оператора IF нарисовать фигуры представленные ниже.
# Пользователь вводит, с клавиатуры, высоту фигуры в символах.
#
# 0             *
# 1           * * *
# 2         * * * * *
# 3       * * * * * * *
# 4     * * * * * * * * *
# 5   * * * * * * * * * * *
# 6 * * * * * * * * * * * * *
# 7   *                   *
# 8     *               *
# 9       *           *
# 10        *       *
# 11          *   *
# 12            *

h = int(input('rhombus height?:'))
i = 1

while i <= h // 2 + 1:
    for j in range(h):
        if j <= h // 2 - i or j >= h // 2 + i:
            print(' ', end=' ')
        else:
            print('*', end=' ')
    print()
    i += 1
while i <= h:
    for j in range(h):
        if j == i - h // 2 - 1 or j == h - (i - h // 2):
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
    i += 1


