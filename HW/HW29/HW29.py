def main():
    name_src = 'src_14.txt'
    name_dst = 'list_of_results.txt'
    col = 0
    count= 0

    with open(name_src, 'rt', encoding='utf-8') as src, open(name_dst, 'wt', encoding='utf-8') as dst:
        for line in src:  # вытаскиваем нужные эл-ты
            tmp = [el for el in line.strip().split()]

            tmp.append(str(round(sum(int(x) for x in tmp[2:]) / len(tmp[2:]), 2))) # добавляем среднюю оценку каждого студента

            if float(tmp[-1]) < 5:  # если ср. оценка ниже 5 выводим на печать
                print(f'{tmp[1] + " " + tmp[0]:20} {tmp[-1]:4}')

            col += float(tmp[-1])
            count += 1

            dst.write(f'{tmp[1] + " " + tmp[0][0] + ".":15} {tmp[-1]:4}\n')

    print(f'Class average {col / count:11.3}')



if __name__ == '__main__':
    main()