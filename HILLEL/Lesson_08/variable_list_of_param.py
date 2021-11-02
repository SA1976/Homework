def func1(*args): # любое количество неименованных аргументов, вместо args может быть 'Вася' - важна *.
    # Аргументы передаются в виде кортежа
    print(args, type(args))

    for param in args:
        print(param, end=' ')
    print()


func1()
func1(1, 2.4, 'Test', True)
func1(1, 2, 3, 4, 5, 6, 7, 8)
print()


def func2(**kwargs):# любое количество именованных аргументов, вместо kwargs может быть 'Вася' - важна *.
    # Аргументы передаются в виде словаря
    print(kwargs, type(kwargs))

func2()
func2(a=1, t=2.4, s='Test', b=True)
func2(x1=1, x2=2, x3=3, x4=4, x5=5, x6=6, x7=7, x8=8)

print()

def func3(*args, **kwargs): # микс предидущих вариантов. Питон сам упакует
    # неименнованные аргументы в кортеж, а именованные в словарь
    print(args, type(args))
    print(kwargs, type(kwargs))

func3()
print()
func3(1, 2.4, 'Test', True, a=1, t=2.4, s='Test', b=True)
print()
func3(1, 2, 3, 4, 5, 6, 7, 8, x1=1, x2=2, x3=3, x4=4, x5=5, x6=6, x7=7, x8=8)