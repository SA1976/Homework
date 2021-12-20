import random
# поиск в отсортированном списке, находим середину и смотрим с какой  от стороны
# середины находится нужный элемент. В результате середина должна совпасть с
# искомым элементом (или его нет в списке) https://prog-cpp.ru/search-binary/

#                   30                 10      20
def binary_search(array, key_value, left=0, right=None):
    if right is None: # если граница не передается( то есть не нужно искать в срезе) -
                             # она устанавливается по краю списка
        right = len(array)

    middle = (left + right) // 2
    while array[middle] != key_value and left <= right:
        if array[middle] < key_value:
            left = middle + 1 # этим ускоряется поиск: граница сдвигается на след элемент за середину
        else:
            right = middle - 1 # то же самое

        middle = (left + right) // 2

    return (True, middle) if not (left > right) else (False, middle+1)


lst = [random.randint(10, 99) for _ in range(20)]

print(lst)
key = int(input('Please enter a number: '))

if key in lst:
    print(f'Key {key} present in List')
else:
    print(f'Key {key} not present in List')

lst.sort()
print(lst)
res = binary_search(lst, key)
if res[0]:
    print(f'Key {key} found {res[1]}')
else:
    lst.insert(res[1], key)
    print(lst)