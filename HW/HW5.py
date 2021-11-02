a = int(input('Number? '))
if a != 0:
    summ = 0
    evens = 0
    odds = 0
    qty = 0
    a_max = a
    a_min = a

    while a != 0:
        qty += 1
        summ += a
        if a_max <= a:
            a_max = a
        if a_min >= a:
            a_min = a
        if a % 2 == 0:
            evens += 1
        else:
            odds += 1
        a = int(input('Number? '))

    print('q_ty\t\t= ', qty)
    print('sum\t\t= ', summ)
    print('average\t= ', summ / qty)
    print('a_even\t= ', evens, '\ta_odd= ', odds)
    print('a_max\t= ', a_max, '\ta_min= ', a_min)


