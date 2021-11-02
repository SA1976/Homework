import random


def line_search(array, key_value):
    for i in range(len(array)):
        if array[i] == key_value:
            return i
    return -1


lst = [random.randint(10, 99) for _ in range(20)]

print(lst)
key = int(input('Please enter a number: '))

res = line_search(lst, key)
if res < 0:
    print('Key not found.')
else:
    print('Index:', res)