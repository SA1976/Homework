from datetime import datetime


def calculate_time(arg):
    print(arg)
    def outer(func):
        def wrapper(*args, **kwargs):   # (param)
            start = datetime.now()
            result = func(*args, **kwargs)
            print(datetime.now() - start)
            return result
        return wrapper
    return outer


@calculate_time('Hello')
def generator_1(cnt):
    lst = []
    for i in range(cnt):
        if i % 2 == 0:
            lst.append(i)

    return lst


@calculate_time('Test')
def generator_2():
    lst = [i for i in range(10_000_000) if i % 2 == 0]
    return lst


# print(len(generator_1(10**7)))       # print(len(wrapper()))
# print(len(generator_2()))