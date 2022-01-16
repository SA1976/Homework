"""
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names,
begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value
by its alphabetical position in the list to obtain a name score.
For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53,
is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.
What is the total of all the name scores in the file?
"""
from pprint import pprint as pp
from string import ascii_uppercase
from time import time
from functools import reduce

def my_sol(): # использование соваря делает выолнение быстрее
    file = open('p022_names.txt')
    s = file.read()
    file.close()

    lst = s[1:-1].split('","')
    lst.sort()
    # lst=list(sorted(map(lambda x: x.strip('"'), open('p022_names.txt').read().split(','))))

    dct = {ascii_uppercase[i]: i + 1 for i in range(len(ascii_uppercase))}
    # dct = dict(zip([x for x in ascii_uppercase], range(1, 27)))
    # 2 варианта создания словаря
    # print(dct)

    outer_collector = 0
    for i in range(len(lst)):
        inner_collector = 0
        for j in range(len(lst[i])):
            inner_collector += dct[lst[i][j]]
            #inner_collector += ord(lst[i][j]) - 64
        inner_collector *= i + 1
        outer_collector += inner_collector
    return outer_collector

def my_sol_2():

    lst=sorted(map(lambda x: x.strip('"'), open('p022_names.txt').read().split(',')))
    return sum(sum(ord(el)-64 for el in value)*idx for idx, value in enumerate(lst, start=1))

def my_sol_3():

    lst=sorted(map(lambda x: x.strip('"'), open('p022_names.txt').read().split(',')))
    return sum(reduce(lambda x, y: x+y, [ord(el)-64 for el in value])*idx for idx, value in enumerate(lst, start=1))

def my_sol_4():
    return sum(reduce(lambda x, y: x+y, [ord(el)-64 for el in value])*idx
               for idx, value in enumerate(sorted(map(lambda x: x.strip('"'), open('p022_names.txt').read().split(','))), start=1))

def euler_sol():
    names = sorted(map(lambda x: x.strip('"'), open('p022_names.txt').read().strip().split(',')))
    return sum(sum(map(lambda x: ord(x) - 64, names[index])) * (index + 1) for index in range(len(names)))
    # unicod заглавных латинских начинается с 65, поэтому "- 64"
def main():

    start = time()
    print(my_sol())
    end = time()
    print(end - start)

    start = time()
    print(my_sol_2())
    end = time()
    print(end - start)

    start = time()
    print(my_sol_3())
    end = time()
    print(end - start)

    start = time()
    print(my_sol_4())
    end = time()
    print(end - start)

    start = time()
    print(euler_sol())
    end = time()
    print(end - start)

if __name__ == '__main__':
    main()
