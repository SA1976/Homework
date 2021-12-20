"""
Следующая повторяющаяся последовательность определена для множества натуральных чисел:

n → n/2 (n - четное)
n → 3n + 1 (n - нечетное)

Используя описанное выше правило и начиная с 13, сгенерируется следующая последовательность:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
Получившаяся последовательность (начиная с 13 и заканчивая 1) содержит 10 элементов.
Хотя это до сих пор и не доказано (проблема Коллатца (Collatz)),
предполагается, что все сгенерированные
таким образом последовательности оканчиваются на 1.

Какой начальный элемент меньше миллиона генерирует самую длинную последовательность?

Примечание: Следующие за первым элементы последовательности могут быть больше миллиона.
длина 524, число 837799 - около 70 сек
c запоминанием результатов в словаре -  6.0 cек
и изменить цикл if n < 1000000 and d[n] > 0: то время сократится до 5 сек изменения в цикл нужны так как в
последовательности появляются цифра 56 991 483 520
c  данной модификацией алгортма - 3,07 cек
подсмотренный с рекурсией на проекте - 2,13
если добавить заранее заполненный 0 словарь d = {n: 0 for n in range(1, 1000000)}

10 - 6 этапов
13 - 3 до 10 и 6 после = итого 9
11 - 5 до 13 = итого 14
14 - 3 до 11 = итого 17
15 - 11 до 10 = итого 16





"""


def my_sol_euler14():

    cnt_max = 0
    n_max = 0
    # total_max = 0 # ловим самое большое число
    d = {}
    for n in range(1, 1000000):
        # print(n, end=' ')
        n_count = n
        cnt = 1
        while n > 1:
            # if n > total_max:
            # total_max = n
            if n % 2 == 0:
                n = n // 2

                if n in d:
                    cnt += d[n]
                    break
                else:
                    cnt += 1
            else:
                n = 3 * n + 1
                if n in d:
                    cnt += d[n]
                    break
                else:
                    cnt += 1
            # print(n, end=' ')
        d[n_count] = cnt
        # print('cnt =', cnt)
        if cnt > cnt_max:
            cnt_max, n_max = cnt, n_count
        # print()
    # print(d)
    # print(n_max)
    # print(cnt_max)
    # print(total_max)
    return n_max, cnt_max


"""
1 
2 1 
3 10 5 16 8 4 2 1 
4 2 1 
5 16 8 4 2 1 
6 3 10 5 16 8 4 2 1 
7 22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 1 
8 4 2 1 
9 28 14 7 22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 1 
10 5 16 8 4 2 1 
11 34 17 52 26 13 40 20 10 5 16 8 4 2 1 
12 6 3 10 5 16 8 4 2 1 
13 40 20 10 5 16 8 4 2 1 
14 7 22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 1 
15 46 23 70 35 106 53 160 80 40 20 10 5 16 8 4 2 1 
16 8 4 2 1 
17 52 26 13 40 20 10 5 16 8 4 2 1 
18 9 28 14 7 22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 1 
19 58 29 88 44 22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 1 
20 10 5 16 8 4 2 1 
21 64 32 16 8 4 2 1 
22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 1 
23 70 35 106 53 160 80 40 20 10 5 16 8 4 2 1 
24 12 6 3 10 5 16 8 4 2 1 
25 76 38 19 58 29 88 44 22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 1 
26 13 40 20 10 5 16 8 4 2 1 
27 82 41 124 62 31 94 47 142 71 214 107 322 161 484 242 121 364 182 91 274 137 412 206 103 310 155 466 233 700 350 175 526 263 790 395 1186 593 1780 890 445 1336 668 334 167 502 251 754 377 1132 566 283 850 425 1276 638 319 958 479 1438 719 2158 1079 3238 1619 4858 2429 7288 3644 1822 911 2734 1367 4102 2051 6154 3077 9232 4616 2308 1154 577 1732 866 433 1300 650 325 976 488 244 122 61 184 92 46 23 70 35 106 53 160 80 40 20 10 5 16 8 4 2 1 
28 14 7 22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 1 
29 88 44 22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 1 
30 15 46 23 70 35 106 53 160 80 40 20 10 5 16 8 4 2 1 
31 94 47 142 71 214 107 322 161 484 242 121 364 182 91 274 137 412 206 103 310 155 466 233 700 350 175 526 263 790 395 1186 593 1780 890 445 1336 668 334 167 502 251 754 377 1132 566 283 850 425 1276 638 319 958 479 1438 719 2158 1079 3238 1619 4858 2429 7288 3644 1822 911 2734 1367 4102 2051 6154 3077 9232 4616 2308 1154 577 1732 866 433 1300 650 325 976 488 244 122 61 184 92 46 23 70 35 106 53 160 80 40 20 10 5 16 8 4 2 1 
32 16 8 4 2 1 
33 100 50 25 76 38 19 58 29 88 44 22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 1 
34 17 52 26 13 40 20 10 5 16 8 4 2 1 
35 106 53 160 80 40 20 10 5 16 8 4 2 1 
36 18 9 28 14 7 22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 1 
37 112 56 28 14 7 22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 1 
38 19 58 29 88 44 22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 1 
39 118 59 178 89 268 134 67 202 101 304 152 76 38 19 58 29 88 44 22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 1 
40 20 10 5 16 8 4 2 1 
41 124 62 31 94 47 142 71 214 107 322 161 484 242 121 364 182 91 274 137 412 206 103 310 155 466 233 700 350 175 526 263 790 395 1186 593 1780 890 445 1336 668 334 167 502 251 754 377 1132 566 283 850 425 1276 638 319 958 479 1438 719 2158 1079 3238 1619 4858 2429 7288 3644 1822 911 2734 1367 4102 2051 6154 3077 9232 4616 2308 1154 577 1732 866 433 1300 650 325 976 488 244 122 61 184 92 46 23 70 35 106 53 160 80 40 20 10 5 16 8 4 2 1 
42 21 64 32 16 8 4 2 1 
43 130 65 196 98 49 148 74 37 112 56 28 14 7 22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 1 
44 22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 1 
45 136 68 34 17 52 26 13 40 20 10 5 16 8 4 2 1 
46 23 70 35 106 53 160 80 40 20 10 5 16 8 4 2 1 
47 142 71 214 107 322 161 484 242 121 364 182 91 274 137 412 206 103 310 155 466 233 700 350 175 526 263 790 395 1186 593 1780 890 445 1336 668 334 167 502 251 754 377 1132 566 283 850 425 1276 638 319 958 479 1438 719 2158 1079 3238 1619 4858 2429 7288 3644 1822 911 2734 1367 4102 2051 6154 3077 9232 4616 2308 1154 577 1732 866 433 1300 650 325 976 488 244 122 61 184 92 46 23 70 35 106 53 160 80 40 20 10 5 16 8 4 2 1 
48 24 12 6 3 10 5 16 8 4 2 1 
49 148 74 37 112 56 28 14 7 22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 1 
50 25 76 38 19 58 29 88 44 22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 1 
51 154 77 232 116 58 29 88 44 22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 1 
52 26 13 40 20 10 5 16 8 4 2 1 
53 160 80 40 20 10 5 16 8 4 2 1 
54 27 82 41 124 62 31 94 47 142 71 214 107 322 161 484 242 121 364 182 91 274 137 412 206 103 310 155 466 233 700 350 175 526 263 790 395 1186 593 1780 890 445 1336 668 334 167 502 251 754 377 1132 566 283 850 425 1276 638 319 958 479 1438 719 2158 1079 3238 1619 4858 2429 7288 3644 1822 911 2734 1367 4102 2051 6154 3077 9232 4616 2308 1154 577 1732 866 433 1300 650 325 976 488 244 122 61 184 92 46 23 70 35 106 53 160 80 40 20 10 5 16 8 4 2 1 
55 166 83 250 125 376 188 94 47 142 71 214 107 322 161 484 242 121 364 182 91 274 137 412 206 103 310 155 466 233 700 350 175 526 263 790 395 1186 593 1780 890 445 1336 668 334 167 502 251 754 377 1132 566 283 850 425 1276 638 319 958 479 1438 719 2158 1079 3238 1619 4858 2429 7288 3644 1822 911 2734 1367 4102 2051 6154 3077 9232 4616 2308 1154 577 1732 866 433 1300 650 325 976 488 244 122 61 184 92 46 23 70 35 106 53 160 80 40 20 10 5 16 8 4 2 1 
56 28 14 7 22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 1 
57 172 86 43 130 65 196 98 49 148 74 37 112 56 28 14 7 22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 1 
58 29 88 44 22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 1 
59 178 89 268 134 67 202 101 304 152 76 38 19 58 29 88 44 22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 1 
60 30 15 46 23 70 35 106 53 160 80 40 20 10 5 16 8 4 2 1 
61 184 92 46 23 70 35 106 53 160 80 40 20 10 5 16 8 4 2 1 
62 31 94 47 142 71 214 107 322 161 484 242 121 364 182 91 274 137 412 206 103 310 155 466 233 700 350 175 526 263 790 395 1186 593 1780 890 445 1336 668 334 167 502 251 754 377 1132 566 283 850 425 1276 638 319 958 479 1438 719 2158 1079 3238 1619 4858 2429 7288 3644 1822 911 2734 1367 4102 2051 6154 3077 9232 4616 2308 1154 577 1732 866 433 1300 650 325 976 488 244 122 61 184 92 46 23 70 35 106 53 160 80 40 20 10 5 16 8 4 2 1 
63 190 95 286 143 430 215 646 323 970 485 1456 728 364 182 91 274 137 412 206 103 310 155 466 233 700 350 175 526 263 790 395 1186 593 1780 890 445 1336 668 334 167 502 251 754 377 1132 566 283 850 425 1276 638 319 958 479 1438 719 2158 1079 3238 1619 4858 2429 7288 3644 1822 911 2734 1367 4102 2051 6154 3077 9232 4616 2308 1154 577 1732 866 433 1300 650 325 976 488 244 122 61 184 92 46 23 70 35 106 53 160 80 40 20 10 5 16 8 4 2 1 
64 32 16 8 4 2 1 
65 196 98 49 148 74 37 112 56 28 14 7 22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 1 
66 33 100 50 25 76 38 19 58 29 88 44 22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 1 
67 202 101 304 152 76 38 19 58 29 88 44 22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 1 
68 34 17 52 26 13 40 20 10 5 16 8 4 2 1 
69 208 104 52 26 13 40 20 10 5 16 8 4 2 1 
70 35 106 53 160 80 40 20 10 5 16 8 4 2 1 
71 214 107 322 161 484 242 121 364 182 91 274 137 412 206 103 310 155 466 233 700 350 175 526 263 790 395 1186 593 1780 890 445 1336 668 334 167 502 251 754 377 1132 566 283 850 425 1276 638 319 958 479 1438 719 2158 1079 3238 1619 4858 2429 7288 3644 1822 911 2734 1367 4102 2051 6154 3077 9232 4616 2308 1154 577 1732 866 433 1300 650 325 976 488 244 122 61 184 92 46 23 70 35 106 53 160 80 40 20 10 5 16 8 4 2 1 
72 36 18 9 28 14 7 22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 1 
73 220 110 55 166 83 250 125 376 188 94 47 142 71 214 107 322 161 484 242 121 364 182 91 274 137 412 206 103 310 155 466 233 700 350 175 526 263 790 395 1186 593 1780 890 445 1336 668 334 167 502 251 754 377 1132 566 283 850 425 1276 638 319 958 479 1438 719 2158 1079 3238 1619 4858 2429 7288 3644 1822 911 2734 1367 4102 2051 6154 3077 9232 4616 2308 1154 577 1732 866 433 1300 650 325 976 488 244 122 61 184 92 46 23 70 35 106 53 160 80 40 20 10 5 16 8 4 2 1 
74 37 112 56 28 14 7 22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 1 
75 226 113 340 170 85 256 128 64 32 16 8 4 2 1 
76 38 19 58 29 88 44 22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 1 
77 232 116 58 29 88 44 22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 1 
78 39 118 59 178 89 268 134 67 202 101 304 152 76 38 19 58 29 88 44 22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 1 
79 238 119 358 179 538 269 808 404 202 101 304 152 76 38 19 58 29 88 44 22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 1 
80 40 20 10 5 16 8 4 2 1 
81 244 122 61 184 92 46 23 70 35 106 53 160 80 40 20 10 5 16 8 4 2 1 
82 41 124 62 31 94 47 142 71 214 107 322 161 484 242 121 364 182 91 274 137 412 206 103 310 155 466 233 700 350 175 526 263 790 395 1186 593 1780 890 445 1336 668 334 167 502 251 754 377 1132 566 283 850 425 1276 638 319 958 479 1438 719 2158 1079 3238 1619 4858 2429 7288 3644 1822 911 2734 1367 4102 2051 6154 3077 9232 4616 2308 1154 577 1732 866 433 1300 650 325 976 488 244 122 61 184 92 46 23 70 35 106 53 160 80 40 20 10 5 16 8 4 2 1 
83 250 125 376 188 94 47 142 71 214 107 322 161 484 242 121 364 182 91 274 137 412 206 103 310 155 466 233 700 350 175 526 263 790 395 1186 593 1780 890 445 1336 668 334 167 502 251 754 377 1132 566 283 850 425 1276 638 319 958 479 1438 719 2158 1079 3238 1619 4858 2429 7288 3644 1822 911 2734 1367 4102 2051 6154 3077 9232 4616 2308 1154 577 1732 866 433 1300 650 325 976 488 244 122 61 184 92 46 23 70 35 106 53 160 80 40 20 10 5 16 8 4 2 1 
84 42 21 64 32 16 8 4 2 1 
85 256 128 64 32 16 8 4 2 1 
86 43 130 65 196 98 49 148 74 37 112 56 28 14 7 22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 1 
87 262 131 394 197 592 296 148 74 37 112 56 28 14 7 22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 1 
88 44 22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 1 
89 268 134 67 202 101 304 152 76 38 19 58 29 88 44 22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 1 
90 45 136 68 34 17 52 26 13 40 20 10 5 16 8 4 2 1 
91 274 137 412 206 103 310 155 466 233 700 350 175 526 263 790 395 1186 593 1780 890 445 1336 668 334 167 502 251 754 377 1132 566 283 850 425 1276 638 319 958 479 1438 719 2158 1079 3238 1619 4858 2429 7288 3644 1822 911 2734 1367 4102 2051 6154 3077 9232 4616 2308 1154 577 1732 866 433 1300 650 325 976 488 244 122 61 184 92 46 23 70 35 106 53 160 80 40 20 10 5 16 8 4 2 1 
92 46 23 70 35 106 53 160 80 40 20 10 5 16 8 4 2 1 
93 280 140 70 35 106 53 160 80 40 20 10 5 16 8 4 2 1 
94 47 142 71 214 107 322 161 484 242 121 364 182 91 274 137 412 206 103 310 155 466 233 700 350 175 526 263 790 395 1186 593 1780 890 445 1336 668 334 167 502 251 754 377 1132 566 283 850 425 1276 638 319 958 479 1438 719 2158 1079 3238 1619 4858 2429 7288 3644 1822 911 2734 1367 4102 2051 6154 3077 9232 4616 2308 1154 577 1732 866 433 1300 650 325 976 488 244 122 61 184 92 46 23 70 35 106 53 160 80 40 20 10 5 16 8 4 2 1 
95 286 143 430 215 646 323 970 485 1456 728 364 182 91 274 137 412 206 103 310 155 466 233 700 350 175 526 263 790 395 1186 593 1780 890 445 1336 668 334 167 502 251 754 377 1132 566 283 850 425 1276 638 319 958 479 1438 719 2158 1079 3238 1619 4858 2429 7288 3644 1822 911 2734 1367 4102 2051 6154 3077 9232 4616 2308 1154 577 1732 866 433 1300 650 325 976 488 244 122 61 184 92 46 23 70 35 106 53 160 80 40 20 10 5 16 8 4 2 1 
96 48 24 12 6 3 10 5 16 8 4 2 1 
97 292 146 73 220 110 55 166 83 250 125 376 188 94 47 142 71 214 107 322 161 484 242 121 364 182 91 274 137 412 206 103 310 155 466 233 700 350 175 526 263 790 395 1186 593 1780 890 445 1336 668 334 167 502 251 754 377 1132 566 283 850 425 1276 638 319 958 479 1438 719 2158 1079 3238 1619 4858 2429 7288 3644 1822 911 2734 1367 4102 2051 6154 3077 9232 4616 2308 1154 577 1732 866 433 1300 650 325 976 488 244 122 61 184 92 46 23 70 35 106 53 160 80 40 20 10 5 16 8 4 2 1 
98 49 148 74 37 112 56 28 14 7 22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 1 
99 298 149 448 224 112 56 28 14 7 22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 1
"""


def rec():  # алгоритм из проект эйлер - рекурсия = 2.377289056777954 сек

    def count_chain(n, dict_reslt):
        if n in dict_reslt:
            return dict_reslt[n]
        if n % 2 == 0:
            dict_reslt[n] = 1 + count_chain(n // 2, dict_reslt)  # развернутая в обратную сторону первая часть формулы - если
        else:
            dict_reslt[n] = 2 + count_chain((3 * n + 1) // 2, dict_reslt)  # если n нечётное,
            # то ему предшествует четное число в последовательность и мы можем пропустить целых 2 шага

        return dict_reslt[n]

    longest_chain = 0
    answer = -1
    dict_reslt = {1: 1}

    for i in range(500000, 999999):
        if count_chain(i, dict_reslt) > longest_chain:
            longest_chain = count_chain(i, dict_reslt)
            answer = i

    return answer


def main():
    from time import time
    start = time()

    print(rec())
    # print(my_sol_euler14())

    end = time()
    print(end - start)


if __name__ == '__main__':
    main()
