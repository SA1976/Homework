# list

# списки отличаются от строк если одному списку назначить
# 2 переменные и потом внести изменния то они коснуться и второй переменной
# lst = [5, 18, 42, 56.5678, 'волаптлокетм', True]
# lst1 = lst
# print(lst1, type(lst1), id(lst1))
# print(lst, type(lst), id(lst))
# lst.pop()
# print(lst, type(lst), id(lst))
# lst.append('Process finished with exit code 0')
# print(lst, type(lst), id(lst))
# del lst[3]
# print(lst, type(lst), id(lst))
# lst.clear()
# print(lst, type(lst), id(lst))
# print(lst1, type(lst1), id(lst1))
# # в строках в данном случае изменится id и переменные станут разными
# st = 'dsfghedfdeghhjegjg'
# st1 = st
# print(st, type(st), id(st))
# print(st1, type(st1), id(st1))
#
# st= st.replace('e', 'E', 2)
# print(st, type(st), id(st))
# print(st1, type(st1), id(st1))



lst = [] # объявление списка через скобки

print(lst, type(lst))
print()

lst = [2, 6, 4.5, 'hellow', True]
print(lst, type(lst))
print()

lst = list() # создание списка через оператор list
print(lst, type(lst))
print()

lst = list('Hellow World!')
print(lst, type(lst))
print()

lst = list(str('123456'))
print(lst, type(lst))
print()

# индексирование как в строках слева направо начиная с 0
# справа налево с -1, и как в строках можно делать срезы

#создание списка с одинаковыми элементами с использованием *
numbers = [5] * 6  # [5, 5, 5, 5, 5, 5]
print(numbers)

x = 4
lst = [x, 5, 6]
x = 4-3
print(lst, x)
print()
# в список передается только занчение переменной

x1 = [1,2,3,4,5]
x2 = [6,7,8,9,0]
x3 = x1+x2
print('x1 + x2 =', x3)
print()
# списки можно складывать и умножать
x4 = x1*3
print(x4)
print()

#list1.extend(list2) - расширяет list1  элементами list2, те list1 увеличивается в размере
x1.extend(x2)
print('extend x1', x1)
print()

x5 = [0]*10 # так можно создать список с одинаковыми элементами
print('10 одинаковых элементов', x5)
print()

lst = list ('Process finished ')
# len
print('длина списка = ', len(lst))
print()

# in, not in
print('а есть в списке =', 'a' in lst)
print('о есть в списке =', 'o' in lst)
print('a нет в списке =', 'a' not in lst)
print()

# min, max, sum
lst = [4,5,3,7,9,3,4,4,5,6,2,3,3,3,8,9,33]
print('список:', lst)
print('min=', min(lst))
print('max=', max(lst))
print('sum=', sum(lst))
print()

#list.index(x) - возвращает индекс искомого объектаб может искать по диапазону внутри списка

print('на каком месте 8?',lst.index(8))
#print(lst.index(48)) - если такого элемента нет, то произойдет ошибка выполнения
print()

#list.count(x) - считает количество вхождений
print('кол-во 3 в списке =', lst.count(3))
print('34 в списке не обнаружено=', lst.count(34))

#list.pop(), list.pop(idx) вытаскивает элемент из списка
# и может присвоить его значение перменной, если список закончится то попытка pop()
# выдаст ошибку
print('было 17 элементов', lst)
print('забрали конечный элемент ', lst.pop())
print('стало 16 элементов', lst)
print('забрали элемент с индексом [3](на самом деле 4-й)',lst.pop(3))
print('стало 15 элементов', lst)
print()

#list.append(value) - добавление в конец списка
lst.append(55)
print('добавили элемент в конец',lst)


# list.insert(idx, value)
lst.insert(3,44)
print('инсерт 44 по индексу 3', lst)
print()

#list.clear - список очищается, но продолжает существовать

#lst.clear(lst)

# list.remove (value) - удаляет 1 элемент данного занчения
lst.remove(3)
print('удалили 1 тройку первую с начала списка', lst)
#lst.remove(33) удаление несуществующего элемента ведет к ошибке выполнения

for _ in range(lst.count(3)):
    lst.remove(3)
print('удалили циклом все тройки',lst)

#del list(idx)
del lst[3]
print('удалили 9 с индексом 3', lst)

#del lst - удаление списка как объекта

#list.revers() - переворачивает элементы ВНУТРИ списка
lst.reverse()
print('перевернули реверсом',lst)

lst1 = lst[::-1] # срез с -1 создает новый список
print ('перевернули обратно срезом с -1 и создался новый список', lst1)
print()

#split (), join()
s = 'Process finished with exit code 0' #разбиение строки по пробелам и закидывание ее в список
print('строка s:',s, type(s))
lst = s.split(' ')
print('поделили строку на слова по пробелам сплитом и получили список:', lst, type(lst))

s2= ' - '.join(lst)
print('сделали из списка строку s2 джоин с "-"',s2, type(s2))