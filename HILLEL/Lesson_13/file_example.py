from pprint import pprint as pp

lst = [
    'Максимальное напряжение, B              250',
    'Максимальный ток, А                     6',
    'Тип рабочего тока                       переменный',
    'Высота педали, мм                       43.5',
    'Толщина педали, мм                      18',
    'Количество контактов (без реверса)      6'
]

pp(lst)

file = open('example_file.txt', 'w') # открываем файл на запись как текстовый
for line in lst: # читая список поэлементно
    file.write(line) # каждую строку записываем в файл
    file.write('\n') # записываем \n

file.close()
print()


# read all
print()
file = open('example_file.txt')
lst = file.read()  # функция read считывает в память весь файл, для большого файла памяти может не хватить
file.close()
pp(lst) # на выходе получим кортеж который содержит одну большую строку
print()

# read all
print()
file = open('example_file.txt')
lst = file.readlines()  # считывает все строки файла, и каждая строка станет элементом списка который эта функция вернёт.
                        # readlines ищет символы \n и ориентируется на них. Тут результат записывается в переменную lst
file.close()
pp(list(map(lambda x: x.strip('\n'), lst))) # удаляем из списка \n и получаем чистый список
print()

# read by 40 symbols
lst = []
pp(lst)
file = open('example_file.txt') # открываем файл на чтение
while True:
    line = file.readline(40)    # считывает файл построчно, только одну строку, параметр (40) означает
                                # что считывать будет порциями по 40 символов, оставлять там файловый курсор, (если до 40 не хватает - просто дойдёт до конца строки)
    if line != '': # line станет пустой в конце файла и тогда произойдёт выход из цикла
        lst.append(line.strip('\n')) #  очищаем от \n и добавляем в пустой список lst
    else:
        break
file.close()
print()
pp(lst)

"""  результат работы readlines
['Максимальное напряжение, B              ',
 '250',
 'Максимальный ток, А                     ',
 '6',
 'Тип рабочего тока                       ',
 'переменный',
 'Высота педали, мм                       ',
 '43.5',
 'Толщина педали, мм                      ',
 '18',
 'Количество контактов (без реверса)      ',
 '6']
"""


# read by line
lst = []
pp(lst) # делает то же самое что и первый пример с readlines
file = open('example_file.txt')
for line in file.readlines(): # только здесь readlines становится частью цикла
    lst.append(line.strip('\n'))
file.close()
print()
pp(lst)

# read by line без readline или radlines
lst = []
pp(lst)
file = open('example_file.txt')
for line in file: #  сразу передаем указатель на файловый объект оператору forкоторый умеет считывать этот объет построчно
    lst.append(line.strip('\n')) #  чистим от \n и передаём списку lst
file.close()
print()
pp(lst)


size_buff = 32 # сколько байт за 1 раз мы используем для записи или чтения файла
src = open('Image_Cover.jpg', 'rb') #  исходный файл
dst = open('Image_Cover_copy.jpg', 'wb') # файл для записи

while True:
    data = src.read(size_buff)
    if data: #  если data не пустая переменная, то записываем новый файл
        dst.write(data)
    else:
        break

src.close()
dst.close()

if src.closed: #проверка закрытия файла через атрибут closed
    print('Source file was closed')

# менджер контекста with позволяет автоматически закрывать файлы
with open('Image_Cover.jpg', 'rb') as src, open('Image_Cover_copy_2.jpg', 'wb') as dst:
    if not src.closed:
        print('Source file is open')
    # with open('Image_Cover_copy_2.jpg', 'wb') as dst:
    while True:
        data = src.read(size_buff)
        if data:
            dst.write(data)
        else:
            break

if src.closed:
    print('Source file was closed')