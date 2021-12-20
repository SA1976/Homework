"""
2**15 = 32768, сумма цифр этого числа равна 3 + 2 + 7 + 6 + 8 = 26.

Какова сумма цифр числа 2**1000?

"""

def two_rates_digits_sum (n, name_dst):
    with open(name_dst, 'wt', encoding='utf-8') as dst:  # запись в файл
        for i in range(1, n+1):
            c = 2**i
            su = 0
            dim = []
            dim_bin = []
            while c > 0:

                dim.append(str(c % 10))
                dim_bin.append(bin(c % 10))
                su += c % 10
                c = c // 10

            s = '+'.join(dim)[::-1]
            dim_bin.reverse()
            s_bin = '+'.join(dim_bin)
            #dst.write(f'2**{i} = {2**i} / {bin(2**i)} = {s} / {s_bin} = {su} / {bin(su)}\n')
            dst.write(f'2**{i} = {2 ** i}  = {s} = {su} \n')

def main():
    n = 50
    name_dst = 'euler16_dec.txt'
    two_rates_digits_sum(n, name_dst)

    from time import time
    start = time()
    print(sum(int(x) for x in str(2 ** 1000))) # брутфорс в одну строку




    end = time()
    print(end - start)

if __name__ == '__main__':
    main()