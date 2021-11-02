string = input('String? ')
symbol = input('Symbol? ')
print()
if len(symbol) == 0:
    print('No symbol entered')
elif len(symbol) > 1:
    print('Only 1 symbol should be entered')
elif string.count(symbol) == 0:
    print('There is NO symbol\t"', symbol, '"\tinside')
else:
    start_position = 0
    print('Symbol\t"', symbol, '"\tfound at position No:', end='')
    for i in range(string.count(symbol)):
       start_position = string.find(symbol, start_position)
       start_position +=1
       print(start_position, ',', end='')
    print()
    print('Total:', string.count(symbol), 'times')
