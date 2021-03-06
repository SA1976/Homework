"""
file = open(file_name, mode, encoding)
...
file_name может Не содержать путь, если он находится рядом со скриптом
файл может быть открыт только для чтения, только на запись или в смешанном режимее
Кодировка важна! Питон 3 использует UTF-8, Мак и Линукс исползуют UTF-8
При работе в Windows, файл Питона может записаться в UTF-8, а открываться в Win-1251
поэтому необходимо ЯВНО указывать в какой кодировки мы будем записывать и читать файл при открытии файла!!!

Если файл был успешно открыт то функция open вернёт файловый объект (переменную), то есть объект через
который мы будем работать с этим файлом.


file.close() - используя файловый объект вызываем функцию close которая закрывает файл и освобождает ресурсы???

При записи файла происходит буфферизация - данные перемещаются в память,
где ожидают пока будут записаны на диск, а программа продолжает свою работу. Если закрыть программу, то ОС сама закроет
 файл, а данные еще находящиеся в буфере там и остануться.
 Если программа закончена, а файл еще открыт, то ОС может некоректно его закрыть и повредить
Функция close принудительно выдавливает все данные из буфера и после этого попытается закрыть этот файл.
Если она не сможет этого сделать, то она выдаст сообщение об ошибке в МОЕЙ программе, где эту ошибку можно обработать.


"""

"""
Mode
r       read (default) - означает что мы сможем применять к этому файлу только операции чтения
        когда мы открываем файл на чтение, то он должен уже существовать и находится на том месте где мы его ищем
w       write - файл может отсутствовать, в этом случае он будет создан и открыт на запись
        Если он существует, то он будет открыт на запись и содерживое его будет удалено.
x       exclusive - похож на w, если файла нет - то он будет создан и открыт. 
        Но если файл есть - получим ошибку - этим файл защищен от перезаписи
a       append - дозапись, если файла нет - будет создан и открыт для записи. 
        Если есть, то файл будет открыт, но содержимое не будет стерто. 
        Мы будем дописывать в конец файла , добавлять данные.
b       binary - открываем файл в бинарном режиме
t       text (default) - открываем файл в текстовом режиме

rt      ниже комбинации всего перечисленного
wt
xt
at
rb
wb
xb
ab
"""

file = open('file.txt', 'w', encoding='utf-8')
file.write('Hello World!\n')
# file.write('\n')
file.write('Привет Мир!')
file.close()