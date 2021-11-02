n = int(input('Number? '))
a = 1
if n < 0:
    print ('no solution')
elif n == 0:
    print (0)
else:
    print(' ')
    while a ** 2 <= n:
        print(a ** 2, end=' ')
        a += 1