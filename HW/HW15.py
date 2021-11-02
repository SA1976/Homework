"""Даны два списка чисел. Посчитайте, сколько (уникальных) чисел содержится
одновременно как в первом списке, так и во втором.
  - Примечание. Эту задачу на Питоне можно решить в одну строчку.

(Задача решается с применением множеств)
"""
import random

spisok1 = [random.randint(0, 5) for _ in range(7)]
print('list1:=', spisok1)
print()
spisok2 = [random.randint(3, 12) for _ in range(15)]
print('list2:=', spisok2)
print()

print('Common Unique numbers:', set(spisok1) & set(spisok2),
      '\nAmount of common unique numbers:', len((set(spisok1) & set(spisok2)))
      )
