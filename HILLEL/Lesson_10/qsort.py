import sys
import random

print(dir(sys))
print(sys.float_info)
i = 348654398659832634986539826539876
print(sys.getsizeof(i))
print(sys.getrefcount(i))
print(sys.int_info)
print(sys.getrecursionlimit())
# sys.setrecursionlimit(1010)
# print(sys.getrecursionlimit())


def rpow(num, ex):
    if ex == 0:
        return 1

    return num * rpow(num, ex-1)


print(rpow(2, 6))


def qsort(nums, first_idx, last_idx, revers=False):
    if first_idx >= last_idx: # конец цикла индексы сошлись в середине
        return

    i, j = first_idx, last_idx # двигаемся от концов списка к середине
    middle_value = nums[(first_idx + last_idx) // 2] # делим последовательсность пополам

    while i <= j: # перебераем элементы и сравниваем их с средним элементом
        while nums[i] < middle_value:
            i += 1 # если левый меньше середины - двигаемся к следующему
        while nums[j] > middle_value:
            j -= 1 # если правый больше середины - двигаемся к предидущему

        if i <= j:
            nums[i], nums[j] = nums[j], nums[i] # когда найдены два таких элемента меняем их местами
            i, j = i+1, j-1 # после этого сдвигаем снова индексы до тех пор пока они не сойдутся в середине

    qsort(nums, first_idx, j) # рекурсия только для левой части
    qsort(nums, i, last_idx) #  рекурсия только для правой части


lst = [random.randint(10, 99) for _ in range(20)]
print(lst)
qsort(lst, 0, len(lst)-1)
print(lst)