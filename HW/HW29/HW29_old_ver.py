"""
В текстовый файл (файл прилагается), построчно записаны имя и
фамилия учащихся класса и их оценки.

1. Вывести на экран всех учащихся, чей средний балл меньше 5, также
посчитать и вывести средний балл по классу.

2. Так же, записать в новый файл всех учащихся в формате "Фамилия И. Ср. балл":
"""
from pprint import pprint

def inp_process(name):

    w_list = []
    with open(name, 'rt', encoding='utf-8') as src:
        for line in src:  # вытаскиваем нужные эл-ты
            w_list.append([el for el in line.strip().split()])# сплит и стрип вообще без параметров

    for el in w_list:  # превращаем оценки в цифры
        for i in range(2, len(el)):
            el[i] = int(el[i])

    return w_list


def main():
    name_src = 'src_14.txt'
    name_dst = 'list_of_results.txt'
    lst_all = inp_process(name_src)

    c = 0
    for line in lst_all:
        line.append(round(sum(x for x in line[2:]) / len(line[2:]), 2))  # формируем среднюю оценку каждого
        if line[-1] < 5:                                                 # если ср. оценка ниже 5 выводим на печать
            print(f'{line[1]+ " "+ line[0]:20} {line[-1]:4.2f}')
        c += line[-1]                                                   # формируем общие баллы класса
    print(f'Class average {c / len(lst_all):11.2f}')                   # печатаем строку со средним баллом класса

    with open(name_dst, 'wt', encoding='utf-8') as dst:  # запись в файл
        for i in range(len(lst_all)):
            dst.write(f'{lst_all[i][1]+ " " + lst_all[i][0][0] + ".":15} {lst_all[i][-1]:3.2f}\n')


if __name__ == '__main__':
    main()
