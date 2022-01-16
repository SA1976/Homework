def generator_1(num):
    lst = []
    while num != 0:
        lst.append(num-1)
        num -= 1

    return lst


def generator_2(num):
    while num != 0:
        yield num - 1
        num -= 1


# print(generator_1(1_000))
print(generator_2(1_000), type(generator_2(1_000)))

n = 1000
for i in generator_2(n):
    # print(i)
    if i > 500:
        break

print('-' * 20)
gen_2 = generator_2(5)
while True:
    try:
        print(next(gen_2))
    except StopIteration:
        break
print('After iteration')