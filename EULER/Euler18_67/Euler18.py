"""
Начиная в вершине треугольника (см. пример ниже) и перемещаясь вниз на смежные числа, максимальная сумма до основания
составляет 23.
3                       3
7 4                    7 4
2 4 6                 2 4 6
8 5 9 3              8 5 9 3

То есть, 3 + 7 + 4 + 9 = 23.

Найдите максимальную сумму пути от вершины до основания следующего треугольника:

Примечание: Так как в данном треугольнике всего 16384 возможных маршрута от вершины до основания, эту задачу
можно решить проверяя каждый из маршрутов. Однако похожая Задача 67 с треугольником, состоящим из сотни строк,
не решается перебором (brute force) и требует более умного подхода! ;o)
"""


def main():
    triangl = []

    name = 'p067_triangle.txt'
    with open(name, 'rt', encoding='utf-8') as src:
        lst = src.readlines()
        for el in lst:
            tmp = el.strip().split()
            triangl.append([int(x) for x in tmp])


    way_summary = [[0] * len(triangl) for _ in range(len(triangl))] # массив для накопления сумм
    way_tracing = [[0] * len(triangl[row]) for row in range(len(triangl))] # массив для отслеживания отуда были получены значения
    way_marked = [[0] * len(triangl[row]) for row in range(len(triangl))] # массив для наглядной демонстрации пути (1 среди 0)

    way_summary[0][0] = triangl[0][0] # передаем начальный элемент


    for row in range(len(triangl)-1):  # идем сверху вниз

        for col in range(len(triangl[row])):

            if triangl[row][col] + triangl[row+1][col] > triangl[row][col] + triangl[row+1][col+1]: #  текущее занчение + левое ниже > текущего + правое нижнее
                if way_summary[row+1][col] < triangl[row+1][col] + way_summary[row][col]: # суммарное значение слева внизу <  значение левой нижней позиции + суммарного значения текущей позиции
                    way_summary[row+1][col] = triangl[row+1][col] + way_summary[row][col] #  влево вниз записываем значение левой нижней позиции + суммарного значения текущей позиции
                    way_tracing[row+1][col] = col # записываем откуда получено значение
                if way_summary[row + 1][col+1] < triangl[row + 1][col+1] + way_summary[row][col]: # суммарное значение справа внизу < значения справа внизу + суммарное значение текущей
                    way_summary[row + 1][col+1] = triangl[row + 1][col+1] + way_summary[row][col] # вправо вниз записывааем заначение правой нижне + суммарного значения текущей
                    way_tracing[row + 1][col+1] = col # записываем откуда получено значение

            elif triangl[row][col] + triangl[row+1][col] <= triangl[row][col] + triangl[row+1][col+1]:
                if way_summary[row + 1][col+1] < triangl[row + 1][col+1] + way_summary[row][col]:
                    way_summary[row + 1][col+1] = triangl[row + 1][col+1] + way_summary[row][col]
                    way_tracing[row + 1][col + 1] = col # записываем откуда получено значение
                if way_summary[row + 1][col] < triangl[row + 1][col] + way_summary[row][col]:
                    way_summary[row + 1][col] = triangl[row + 1][col] + way_summary[row][col]
                    way_tracing[row + 1][col] = col # записываем откуда получено значение

    # with open('rez_Euler67.txt', 'wt') as dst: # загоняем результаты в файл
    #     for line in way_summary:
    #         dst.write(str(line))  # каждую строку записываем в файл
    #         dst.write('\n')  # записываем \n


    for el in way_tracing: # это массив с данными откуда были взяты значения для каждого э-та
        # (указаны только столбцы, так ка строка всегда предидущая)
        print(el)

    a = way_summary[-1].index(max(way_summary[-1])) # индекс максимального эл-та последней строки
    print(max(way_summary[-1]))
    path = [] # список чисел из которых состоит путь
    for row in range(len(triangl) - 1, 0, -1 ):
        for col in range(len(triangl[row])):
            if col == a:
                way_marked[row][col] = 1 # отмечаем маршрут 1 среди 0
                a = way_tracing [row][col] # меняем индекс на след значение
                path.append(triangl[row][col]) # добавляем числа в путь, начиная с конца

    path.reverse() # так как шли с конца, то впреди - послднее значение
    for el in way_marked:
        print(el)

    print()
    print(path) # путь без самого первого элемента
    print(sum(path)+triangl[0][0]) # добавляем вершину треугольника и считаем сумму


if __name__ == '__main__':
    main()

