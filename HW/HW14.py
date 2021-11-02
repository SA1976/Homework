# Дан список чисел. Определите, сколько в нем встречается различных (уникальных) чисел.
#   - Примечание. Эту задачу на Питоне можно решить в одну строчку.
# (Задача решается с применением множеств)

import random

spisok = [random.randint(0, 7) for _ in range(15)]
print(spisok)
print()

print('Unique numbers:', set(spisok), '\nAmount of unique numbers:', len(set(spisok)))
