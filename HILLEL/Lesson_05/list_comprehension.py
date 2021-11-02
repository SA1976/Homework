import random

lst = []
print('тут заранее создается список, аппенд добавляет в конец случайное число и\n'
      'список распечатывается целиком')
for _ in range(25):
    lst.append(random.randint(10, 99))# тут заранее создается список и аппенд добавляет в конец случайное число
print(lst)
print()

print('распечатка списка по элементам 1-й вариант')
for i in range(len(lst)):
    print(lst[i], end=' ')
print()
print()

print('распечатка списка по элементам 2-й вариант')
for value in lst: # тут можно только читать!!!
    print(value, end=' ')
print()
print()

# variable = [expression1 expression2 expression3]
# expression2 - цикл
# expression1 - выражение которое выполняется
# expression3 - фильтр
# 2 - 1
# 2 - 3 - 1
print('Генератор списка одной строкой вариант без условия')
lst = [random.randint(10,99) for _ in range(15)]
#           1                       2
print(lst,type(lst))
print()


print('отбор четных элементов и пересоздание списка')
lst1 = [value for value in lst if value % 2 == 0]
print (lst1, type(lst1))
print()

print('объединение элементов списка в строку с выводом итоговой суммы')
s = ' + '.join([str(value) for value in lst]) + '=' + str(sum(lst))
print(s, type(s)) #суммировать можно только строки поэтому int-элементы списка
# необходимо перевести в строковые значения, также и сумму

matrix = [[x for x in range(1, 4)] for y in range(1, 4)] # создание 2-го списка [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
print(matrix)