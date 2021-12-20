from time import time
def divisorss(n):
    from collections import Counter
    ls = get_ls(n)                  # for n=1568 -> ls = [2, 2, 2, 2, 2, 7, 7]
    pairs = dict(Counter(ls))       #  {2: 5, 7: 2}
    from itertools import product, starmap
    from operator import mul
    from functools import reduce
    #  список всех различных делитей числа
    bases = [b for b in pairs.keys()]   # [2, 7]
    #print(bases)

    #  список степеней, в которые возводятся уникальные делители для получения числа  
    powers = [[i for i in range(k+1)] for k in pairs.values()]
    #print(powers)


    # генерирование всех наборов для получения делителей исходного числа
    multi = product(*powers)
    #print(multi)

    #  сцепка списка оснований с возможными вариантами степеней
    wrk =(zip(bases,power) for power in multi)
    #print(wrk)

    # наборы чисел, которые нужно перемножить для получения делителя
    rezzz =(starmap( pow, row) for row in wrk)
    #print(rezzz)

    # возвращение списка всех делителей
    return [reduce(mul,i) for i in rezzz]

def get_ls(n):
    """Разложить число на множители"""
    #result = [1]
    result = []
    i = 2
    while i*i <= n:
        if n % i == 0:
            n //= i
            result.append(i)
        else:
            i += 1
    if n > 1:
        result.append(n)
    return result

start = time()
n = 76576500

print(sorted(divisorss(n)))
end = time()
print(end - start) # 0.002989053726196289