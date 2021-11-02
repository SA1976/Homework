import random

spisok = [random.randint(0, 99) for _ in range(int(input('Enter list length: ')))]
print(spisok)
print()

a = 0
for i in range(1, len(spisok)-2):
    if spisok[i] > spisok[i-1] and spisok[i] > spisok[i+1]:
        print('position:', i+1, '- ', spisok[i],)
        a += 1
print()
print('Selected', a, 'items')
