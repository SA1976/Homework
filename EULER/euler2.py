"""
Каждый следующий элемент ряда Фибоначчи получается при сложении двух предыдущих. Начиная с 1 и 2, первые 10 элементов будут:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

Найдите сумму всех четных элементов ряда Фибоначчи, которые не превышают четыре миллиона.

4613732 - 0.00020694732666015625 сек
"""

# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269, 2178309, 3524578, 5702887]

def my_sol_euler2(): #время 0,0001
    fib = [0, 1]
    i = 0
    while fib[i] + fib[i+1] <= 4000000:
        fib.append(fib[i] + fib[i+1])
        i+=1

    counter = 0
    for el in fib:
        if el % 2 == 0:
            counter += el

    print(sum(fib), '\n', fib)
    print(counter)


def not_my_sol(): # не я нвмного проще и время 5 - 5

    a = 0
    b = 1
    sum = 0
    while (a + b) < 4000000:
        b += a
        a = b - a
        if b % 2 == 0:
            sum += b

    return sum

def pr_euler_sol2(): # 5 -5

    sum = 0
    a = 1
    b = 2

    while b < 4000000:
        sum += b
        c = b
        b = 3 * b + 2 * a
        a = 2 * c + a

    return sum

def only_even_fibb(num): # время 5 -5
    # 0 2 8 34 144 610 2584 - это четные числа
    # из ряда фибонначии формула: F(n)=4*(Fn-1)+F(n-2)
    a = 0
    b = 2
    sum = 2
    while (a + b) < num:
        sum += 4 * b + a
        a, b = b, 4 * b + a

    return sum



def main():
    from time import time
    start = time()

    #print(my_sol_euler2())
    #print(not_my_sol())
    print(pr_euler_sol2())
    #print(only_even_fibb(4000000))



    end = time()
    print(end - start)

if __name__ == '__main__':
    main()
