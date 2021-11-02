import random


def bubble_sort(array, revers=False):
    cnt = 0
    for i in range(len(array)-1):
        flag = True
        for j in range(len(array)-1-i):
            if revers:
                if array[j] < array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]
                    flag = False
            else:
                if array[j] > array[j+1]:
                    array[j], array[j+1] = array[j+1], array[j]
                    flag = False
        cnt += 1
        if flag:
            break
    print(cnt)





lst = [random.randint(10, 99) for _ in range(20)]
# lst = [19, 20, 38, 41, 43, 47, 49, 49, 61, 57, 68, 73, 82, 83, 84, 86, 88, 90, 91, 98]

print(lst)
bubble_sort(lst)
#bubble_sort(lst, revers=True)
print(lst)