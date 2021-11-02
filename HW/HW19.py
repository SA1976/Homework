

h = int(input('rhombus height?:'))
i = 1

while i <= h // 2 + 1:
    for j in range(h):
        if j <= h // 2 - i or j >= h // 2 + i:
            print(' ', end=' ')
        else:
            print('*', end=' ')
    print()
    i += 1
while i <= h:
    for j in range(h):
        if j == i - h // 2 - 1 or j == h - (i - h // 2) or j == h // 2:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
    i += 1
