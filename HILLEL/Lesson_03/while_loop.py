"""
while condition(когда условие - TRUE, до тех пор поека не станет FALSE):
    operator1
    operator2
    operator3

operator 4 - не имеет отношение к телу цикла

бесконечный цикл:

while True:
    operator1
"""
# - однострочный комментарий
"""
многострочный
комментарий
орлор
олор
# """
# i = 1
# while  i <= 15:
#     print(i, end = ' ')
#     i += 1
# print() # этот принт стоит для перехода на новую строку в конце последовательности
#
# while True:
#     a = int(input('Введите первое число'))
#     b = int(input('Введите первое число'))
#     if b == 0:
#         break # выход из бесконечного цикла - прерывает весь цикл полностью
#     print('Результат:', a / b)
#
# print ()

# x = 1
# while x <= 50:
#     if x % 3 == 0: #проверка кратности 3
#          x +=1
#          continue #прерывает текущую итерацию
#     print(x, end=' ')
#     x +=1
# print()


x = 0
while x < 10:
    print(x, end=' ')
    x += 1
    if x == 15:
        break
else: #тут else выполняется только конгда станет ложным условие в цикле while,
    # если произойдет brake (если в if будет например 5), то елсе
    # не выполнится никогда
    print('ELSE')