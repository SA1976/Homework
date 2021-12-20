"""
Starting in the top left corner of a 2×2 grid, and only
being able to move to the right and down, there are
exactly 6 routes to the bottom right corner.


How many such routes are there through a 20×20 grid?
137846528820 = 40!/20!(40-20)! - формула сочетания комбинаторики
m-элементного подмножества из n-элементного множества.
С = n! / m!(n-m)!, n > m
или треугольники Паскаля: число в треугольнике Паскаля обозначает количество путей ведущих к нему от вершины
(1-я строка является нулевой, 20-й элемент 40-й строки даст нужное число)
"""

def paskal_triangels_by_string_addition(n):

    triang = [[0] * (n+1) for i in range(n+1)]
    triang[0][0] = 1
    for row in range(n+1): # строка = предидущая строка + предидущая строка сдвинутая влево на 1 столбец
        triang[row][0] = 1
        for col in range(1, n+1):
            triang[row][col] = triang[row-1][col] + triang[row-1][col-1]

    return triang


def grid(row, col): #  круто и очень быстро - не моё
    if col == 0 or row == 0: # это левый верхний угол
        return 1
    elif row == 1:
        return col + 1
    elif col == 1:
        return row + 1
    else:
        return grid(row, col - 1) + grid(row - 1, col)


def main():

    # n = 40
    # lst = paskal_triangels_by_string_addition(n)
    # print(lst[n][n//2])
    # for i in range(n+1): #  печать самого треугольника Паскаля
    #     for el in lst[i]:
    #         if el != 0:
    #             print(el, end=' ')
    #     print(f'Строка = {i}\n')

    i = 0 # крутая чужая реккурсия
    dim = 20
    total = 0
    while i <= dim:
        total = total + grid(i, dim - i) ** 2
        i += 1
    print(total)

if __name__ == '__main__':
    main()

