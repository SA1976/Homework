n = int(input('Number? '))

result = 1
degree = 0

while result <= n:
    if (result * 2) > n:
        break
    degree +=1
    result = 2 * result
print (n,'\t', degree, result,'\t\t2 **',degree, ' = ',result)

