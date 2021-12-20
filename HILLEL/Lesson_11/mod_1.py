from random import randint


s = 'Hello World!'

lst = [randint(10, 99) for _ in range(25)]


def print_list(array):
    for el in array:
        print(el, end=' ')
    print()


print(__name__, 4)


def main():
    print_list(lst)
    print(s)


if __name__ == '__main__':  # это условие позволяет избежать запуска модуля как скрипта при импорте все исполняемые
    # команды передаются в функцию/набор функций или могут оставаться в теле if
    # еще этим способом пользуются что бы показать точку входа в программу - ОС будет искать ее для старта программы
    # и с запуска функции main начнется ее исполнение.

    main()
    # print_list(lst)
    # print(s)