
def my_sol_euler1(): #0,0003
    #col_list = []
    col = 0
    for i in range(999, 0, -1):
        if i % 3 == 0 or i % 5 == 0:
            col += i
            #col_list.append(i)
    # print(col_list)
    # print(col)
    return col

def pr_euler_sol1(): #  dhtvz 5 -5


    def simple_division(n):
    # берем все кратные 3 + все кратные 5 и вычитаем повторяющиеся кратные 15
    # напр 3+ 6+9 + ... +999 = 3*(1+2+3+ ... +333)
    # сумма ряда 1+2+3+...+p = p*(p+1)/2
        p = 999 // n #  находим р
        return n*(p*(p+1)) // 2 # считаем сумму ряда

    return (simple_division(3) + simple_division(5) - simple_division(15))

def main():
    from time import time
    start = time()

    #print(my_sol_euler1())
    print(pr_euler_sol1())



    end = time()
    print(end - start)

if __name__ == '__main__':
    main()





