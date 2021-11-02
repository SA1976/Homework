s1 = 'fhjbsjhbfjksndckjsn'
s2 = "djbsdhjfnjwnkjsdnkjsndf"
#s3 = 'dfsdfsddsfsdfsd"
s4 = """
fhjbsjhbfjhshbdnf
wejkfnwenf
wejknkwjfn

"""
s5 = '''
ewfjnwkenf
            ehfbwjehbf
efwefwef
''' # текст в тройных кавычках будет выведен в том же формате со всеми отступами
# внутри строк работают эскейп символы \n, \b, \t итд !!!! только внутри строк!!!!
#print(s5)

# строки можно складывать и умножать (на целое число)



s = '\u26bd'
print('\u26bd')
# \u - дальше идет 2 байта для кодировки 16-ного кода
# \U - даьлше идут 4 байта для кодировки 16 -го кода
s = '\U0001f6a3'

print('печать символа в виде строки с  его кодом начиная со \\', s)

x = chr(0x26bd)
print('печать переменной с 16-м кодом мяча', x)
print('chr создает символ по 16-му коду:', chr(0x26bd))
print('chr создает символ по 10-му коду:', chr(9917))

print('орд возвращает код символа мяч', ord('⚽'))
print()
#    0  1   2   3   4 - положительные индексы, последний символ = длина строки - 1
#   'H  E   L   L   O'
#   -5 -4  -3  -2  -1 - отрицательные индексы
# обращение по индексу быстрее чем подсчет длины строки и
#
s = 'Hello Word!'
x = len(s)
print('Len дает длину строки', x)

# str[index] - получение 1-го символу
print('символ с индексом 2 =', s[2])
print('предпоследний символ =', s[-2]) # получение предпоследнего символа
print('предпоследний символ через len', s[len(s)-2]) # другой вариант предпоследнего символа
print(12)
print(-14)
print()

# slices - получение подстроки
# str[start: stop(символ ДО которого нужно остановится (в как и в range): step]

s = 'Process finished with exit code 0'
print('печать всей строки ч/з слайс:', s[:])
s1 = s[:]
print(s1)
print(id(s1))
print(id(s))
print(s[:])
print('слайса с идексами 0-7',s[0: 7])
print('слайса до индекса 7', s[: 7])
print('слайс 8-16', s[8: 16])
print('слайс 27-33', s[27: 33])
print('если индексы больше начала и конца строки\n'
      'печатается вся строка',s[-3475683658732:3892374982374])
print('шаг = 2 и вся строка через одну букву',s[::2]) #вся строка через одну букву
print('шаг = -1 и строка переворачивается зеркально',s[::-1]) #строка переворачивается зеркально
print()

# # функции строк
#
# # len(str)
# # int(str), float(str),
# #str(int), str(float)
#
# # find(substr, #start, #stop) cлева направо, rfind(substr, #start, #stop) справа налево
# # s = 'Process finished with exit code 0'
# # print(len(s))
# # print(s.find('with'))
# # print(s.find('e'))
# # print(s.find('e', 5))
# # print(s.find('e', 15))
# # print(s.find('e', 23))
# # print(s.find('e', 31)) # тут результатом будет -1 так
# # последнее 'e' находится на 30-м месте
#
# # строка неизменяемый объект!!!!
# # str.replace(старый символ, новый символ, сколько раз)
s1 = s.replace('e', 'E', 2)
print(s)
print('заменили 2 первых "e" на "Е"',s1)
print()

#
# # str.count(sub) количество вхождений подстроки в строку
# если такой подстроки нет - результат будет = 0
print('подсчет количества "it" в строке =', s.count('it'))
print()

s = 'Process finished with exit'
# str.strip(sub) удаляет ведущие и конечные символы, если п fрараметр не указан
# то она удаляет ведущие и конечные пробелы
print('"'+ s + '"')
s = '              Process finished with exit code 0         '
print('"'+ s + '"')
print('пробелы убраны стрипом', '"'+ s.strip() + '"')
s = ' rrrarrarr arrr Process finished with exit code 0 aaara aara aa'
print('"'+ s.strip('r').strip('a') + '"')# тут удаляются r, a
print('"'+ s.strip('r a') + '"')# тут удаляются пробелы, r, a

print(len(s))
print(s[0:54:1])
print(s[0:54:2])
print(s[::2])
print(s[0:54:3])
print(s[0:54:4])
print(s[0:54:5])
print(s[0:54:6])

#функции джойн и сплит описаны в collection_list