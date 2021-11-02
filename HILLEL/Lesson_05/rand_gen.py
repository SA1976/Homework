import random

# randint ()
#randrange()
# random()
# uniform

#randrange(start,stop,step) stop НЕ входит в диапазон
# выдает одно значение из указанного диапазона
# range (1, 20, 2) 1,3,5,7,9,11,13,15,17,19
# randrange (1, 20, 2) 5, 11, 13 , 1, 5,3

print('случайные целые нечетные из диапазона 1-20')
for _ in range (15):
    print(random.randrange(1, 20, 2), end=' ')
print()
print()

#randint(start, stop) тут стоп входит в даиапазон!!!!
print('случайные из диапазона 1-10')
for _ in range(15):
    print(random.randint(1,10), end = ' ')
print()
print()

# random() случайные числа в диапазоне 0 - 1
print('случайные числа в диапазоне 0-1')
for _ in range(15):
    print(random.random(), end = ' ')
print()
print()

print('то же самое но с округлением до 2-го знака')
for _ in range(15):
    print(round(random.random(), 2), end = ' ')
print()
print()

#uniform (start, stop) stop входит
print('вещественные числа из диапазона 0.1 - 20.9')
for _ in range(15):
    print(random.uniform(0.1, 20.9), end = ' ')