import random

spisok = [random.randint(-99, 99) for _ in range(int(input('Enter list length: ')))]
print(spisok)
print()

for i in range(0, len(spisok) // 2):
    a = spisok[i]
    spisok[i] = spisok[len(spisok) - 1 - i]
    spisok[len(spisok) - 1 - i] = a

print(spisok)
print()
