import random

spisok = [random.randint(0, 99) for _ in range(int(input('Enter list length: ')))]
print(spisok)
print('List length:', len(spisok))

print('Enter index for element to be deleted? (from (0 to', len(spisok) - 1, '):', end=' ')
k = int(input())

if k >= len(spisok):
    print('No delete possible')
else:
    for i in range(k, len(spisok) - 1):
        spisok[i] = spisok[i+1]
    spisok.pop()
    print(spisok)
    print('Modified list length:', len(spisok))
