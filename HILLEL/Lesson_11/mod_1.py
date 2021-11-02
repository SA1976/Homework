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


if __name__ == '__main__':
    main()