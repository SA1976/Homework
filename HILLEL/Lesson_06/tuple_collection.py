# кортежи - неизменяемые объекты
#проект Эйлера, питонтьютор, stepik
t = ()

print(t, type(t))

t= (5, 6, 7.8, 'Hello', True)
print(t, type(t))

t = tuple()
print(t, type(t))

t = tuple('Hello World!') # таким образом невозможно создать кортеж с числами, будет выдавать оштбку
print(t, type(t))

# индексы работают как в списках
print(t[0])
print(t[-1])
# 1 имеет индекс длина строки с минусом
print(t[0:12:2])

#t[5] = 'R'

# распаковка кортежа - должно быть соответсвие кол-ва переменных длине кортежа
s = (56, 56, True,  5.666,'o')

(a, b, c, d, e) = s

print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))
print(e, type(e))


#len()
print(len(t))
t1 = (1,2,3)
t2=(4,5,6)
t3=t1+t2
print(t3)

t4 = t1*4
print(t4)

# in     not in
print(4 in t1)
print(2 in t1)
print(4 not in t1)

#for
for element in t1:
    print(element, end=' ')
print()

for i in range (len(t1)):
    print(t1[i], end=' ')
print()

#index(value, start, stop)
print(t1.index(2))

#count(value)
print(t1.count(3))
print(t1.count(9))

# min, max, sum



#примененние кортежей
# 1 - создание констант
const = (9.8, 3.14)
# 2
a = [1,2,3]
b = 1, 2, 3 # упаковка в кортеж
print(b, type(b))

print(1, 4.5, 'Hellow World!', True)

t = (50) #не кортеж
print(t, type(t))

t = (50,)#кортеж
print(t, type(t))

t = 50, #кортеж
print(t, type(t))