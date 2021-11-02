"""
{
key1: value1,
key2: value2,
key3: value3,
key4: value4

}
"""
import pprint

# создание пустого словаря а НЕ множества
d = { }
print(d, type(d))
print()

# создание заранее заполненного словаря
d = {
    1: 'one',
    0: 'zero'
}

print(d, type(d))
pprint.pprint(d)
print()

# создание  словаря с помощью функции. Создает пустой  словарь если мы не передаем в неё параметры
d = dict()
print(d, type(d))
print()

d = {
    'Colorado': 'Rockies',
    'Boston': 'Red Socks',
    'Minnesota' : 'Twins',
    'Milwaukee': 'Brewers',
    'Seatle':  'Marines'
}
print('Вывод ч/з print:\n', d, type(d))
print('Вывод ч/з pprint:')
pprint.pprint(d)
print()

# функции dict должен быть передан список состоящий из кортежей каждый из которых
# содержит 2 элемента: 1-е элементы - ключи, 2-е элементы - значения. Так можно добавлять
# записи в словарь по ходу выполнения программы
d = dict(
    [
        ('Colorado', 'Rockies'),
        ('Boston', 'Red Socks'),
        ('Minnesota', 'Twins'),
        ('Milwaukee', 'Brewers'),
        ('Seatle',  'Marines')
    ]
)
pprint.pprint(d)
print()

# второй вариант создания словаря - с помощью набора именованных аргументов. Имя параметра
# предается в виде строковых значений в качестве ключа (это грубо говоря имена переенных),
# это будет не имя переменной, а просто строка.

# в качестве значения ключа.
d = dict(
    Colorado='Rockies',
    Boston='Red Socks',
    Minnesota='Twins',
    Milwaukee='Brewers',
    Seatle='Marines'
)
pprint.pprint(d)
print()

# имя переменных записанное большими буквами принято считаеть константой PRINT = 0

# порядок элементов в словаря сохраняется таким как добавлялись элементы, такая особенность есть,
# но целенаправленно её не сохраняют, вполне возможно, что в след версиях Питона ее не будет.

# pprint может менять местами элементы (сортировать), print этого не делает!!!

# эл-ты в словаре не индексируются и обращение к значениям идет по [ключам].

print(d['Boston'])
#print(d['Boston1']) # такого ключа нет - появится ошибка ' KeyError: 'Boston1''

# добавление новой записи - обращение к словарю по новому ключу
d['Texas'] = 'Red bull'
pprint.pprint(d)
"""
При чтении:
- если ключ есть - выдает значени
- если ключа нет - выдает ошибку KeyError

При записи:
- если ключ есть - обновляет значение
- если ключа нет - создаем новую запись с данным ключом и данным значением

"""
# обновление/изменение значения при обращении по существующему ключу
d['Boston'] = 'Red Sox Ex'

# если в виде значения будет список, то значений станет несколько
d['Boston'] = ['Red Sox', 'Red Sox Ex']
pprint.pprint(d)
"""
в качестве значений может использоваться ЛЮБОЙ тип данных: число, строка, список
или более сложные объекты - список списков, словарь списков, список словарей, итд

В качетве ключей используются ТОЛЬКО неизменяемые типы данных: строки, числа,
 кортежи, фрозенсеты
 key ==> str, int, tuple, frozenset
"""

d[(1,2)] = 'tuple', # создается запись с ключом-кортежем
pprint.pprint(d)
print()
"""
d[['a', 'b']] = 'letters' - передаем список в виде букв и получаем ошибку unhashable type: 'list'
в Питоне хэшируются только неизменяемые типы данных и так как ключи хэшируются поэтому
 и наложены ограничения на типы данных которые могут быть ключами
pprint.pprint(d)
"""
d[0] = 'zero' # ключ- число
pprint.pprint(d)

d = {
    0: 'zero',
    1: 'one',
    2: 'two'
}
# так как в виде ключей выступают числа, то кажется что ниже
# идет обращение по индексам, однако это не так
# глядя в коде на такую запись можно подумать что это - список
# нужно смотреть на тип объекта
print(d[0])
print(d[2])
print()

# словарь может быть заполнен постепенно
# для того что бы работать со словарем необходимо понимать его структуру

person = {}
person['name'] = 'Ivan'
person['age'] = 34
person['children'] = ['Olga', 'Petr', 'Elena'] # список детей
person['pets'] = {'cat': 'Fox', 'dog': 'Sharik'} # словарь петов
pprint.pprint(person)

print(person['name'])
print(person['children'][1]) #обращение к 1-му ребенку в списке по индексу
print(person['pets']['dog']) #обращение к разделу словаря [person] по ключу [pets]
# и обращение к внутренненму словарю [pets] по ключу [dog] для получения его значения

teams = dict(
    Colorado='Rockies',
    Boston='Red Socks',
    Minnesota='Twins',
    Milwaukee='Brewers',
    Seatle='Marines'
)
pprint.pprint(teams)
print()

# in         not in - проверка наличия ключа в словаре
print ('Boston' in teams)
print ('Boston1' in teams)
print ('Boston1' not in teams)
print()

#len(obj) - выдаст количество цельных записей
print(len(teams))
print()

# dict.clear() - очистка словаря
# teams.clear()
# print(teams) #  выдаст {}

#dict[key] - выдаст запись по ключу, если ключа нет выдаст KeyError
# dict.get(key, default_value) - выдаст значение если ключ есть / None -
# если такого ключа нет или  default_value если она указано - это может быть
# строка/число, True/False, словарь/список, итд
print(teams.get('Boston1', 'No team in dict'))
print()

# dict.keys() - специальный список ключей
#dict.values() - специальный список значений
#dict.items() - специальный список записей

print(teams.keys())
print(teams.values())
print(teams.items())
print()

# можно преобразовать в список и работать как с обычным списком
print(list(teams.keys()))
print(list(teams.values()))
print(list(teams.items()))
print()

# цикл for достает значения из teams.items и тут же распаковывает их в две переменные key и value для каждой записи

for key, value in teams.items():
    print(key, '-->', value)
print()

# пример упаковки чисел в кортеж и распаковки кортежа в переменные
t = (1, 2, 3, 4) # или просто t = 1, 2, 3, 4
a, b, c, d, = (1, 2, 3, 4)

# dict.pop(key) вытаскивание значения по ключу и удаление всей записи из словаря
pprint.pprint(teams)
print('Значение по ключу Бостон:', teams.pop('Boston'))
pprint.pprint(teams)
print()

#dict.popitem() вытаскивание случайной записи целиком  в виде кортежа и удаление из словаря
pprint.pprint(teams)
print('Запись целиком', teams.popitem())
pprint.pprint(teams)
print()

#dict1.update(dict2) обновление 1-го словаря 2-го словарем
# недостающие элементы 2-го словаря добавляются во 1-й словарь
#  существующие элеметы 1-го словаря заменяются на элементы 2-го
# 2-й словарь не меняется
d1 = {'a': 10, 'b':20, 'c': 30}
d2 = {'b':200, 'd':300}

print(d1)
print(d2)
d1.update(d2)
print(d1)
print(d2)