"""
Последовательность треугольных чисел образуется путем сложения натуральных чисел.
 К примеру, 7-е треугольное число равно 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28.
 Первые десять треугольных чисел:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Перечислим делители первых семи треугольных чисел:

 1: 1
 3: (1+2) 1, 3
 6: (1+2+3) 1, 2, 3, 6
10: (1+2+3+4) 1, 2, 5, 10
15: (1+2+3+4+5) 1, 3, 5, 15
21: (1+2+3+4+5+6) 1, 3, 7, 21
28: (1+2+3+4+5+6+7) 1, 2, 4, 7, 14, 28
Как мы видим, 28 - первое треугольное число, у которого более пяти делителей.

Каково первое треугольное число, у которого более пятисот делителей?

сумма конечного ряда треугольных чисел: S(m) = (m*(m+1)*(m - 2)// 6
triangle number, i.e. num = 1 + 2 + ... + i = i * (i + 1) / 2
количество делителей = (степень1 простого делителя + 1)*(степень2-го простого + 1) ...

количество делителей числа 76576500 = 576, степени: [2, 2, 3, 1, 1, 1, 1]
{2: 2, 3: 2, 5: 3, 7: 1, 11: 1, 13: 1, 17: 1} 3 сек!!!!

"""
def my_sol_euler12 ():  # 2,96  сек
    def list_of_divisor(n, lst):  # или как в данном случае список степеней делителей
        temp = 0
        div_collector = {}
        rates = []
        for i in range(0, len(lst)):
            flag = True
            while flag:
                if n % lst[i] == 0:
                    temp += 1
                    n = n // lst[i]  # если темп = 1 сделать прерывание цикла
                else:
                    flag = False
            if temp != 0:
                div_collector[(lst[i])] = temp
                rates.append(temp)
                temp = 0
        if n != 1:
            rates.append(1)
            div_collector[n] = 1 # тут можно дополнить список простых чисел найденным простым остатком
            list_prime_rates.append(n) # добавляем в конец найденные по дороге простые числа
            list_prime_rates.sort() # сортируем список простых
        return rates,  div_collector, list_prime_rates

    a = 1
    n = 1
    m = 1

    list_prime_rates = [2]
    while m < 500:
        a += 1
        n = n + a
        m = 1

        rates, div_tuple, list_prime_rates = list_of_divisor(n, list_prime_rates)  # выдает степени простых делителей
        for i in range(len(rates)):
            m *= rates[i]+1
        #print(f' список простых делителей{list_prime_rates}')
    # print(f'количество делителей числа {n} = {m}, степени: {rates} - это {a}-е треуг число')
    # print(div_tuple)

    return n

#def test

"""
количество делителей числа 76576500 = 576, степени: [2, 2, 3, 1, 1, 1, 1] - это 12375-е треуг число
{2: 2, 3: 2, 5: 3, 7: 1, 11: 1, 13: 1, 17: 1}
количество делителей числа 842161320 = 1024, степени: [3, 3, 1, 1, 1, 1, 1, 1] - это 41040-е треуг число
{2: 3, 3: 3, 5: 1, 7: 1, 11: 1, 13: 1, 19: 1, 41: 1} - 26 сек
"""

def main():
    from time import time
    start = time()


    print(my_sol_euler12())

    end = time()
    print(end - start)

if __name__ == '__main__':
    main()
