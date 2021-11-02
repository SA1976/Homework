"""
try:
    operator_1
    operator_2
    operator_3
    operator_4
    .
    .
    .
    operator_N
except TypeError_1 as ex:
    # logging issues
except TypeError_2 as ex:
    # logging issues
except TypeError_3 as ex:
    # logging issues
"""


z = 0
while True:
    try:
        x = int(input('Please enter first value: '))
        y = int(input('Please enter second value: '))
        z = x / y
        # break
    except ZeroDivisionError as ex:
        print('Error:', ex)
    except ValueError as ex:
        print('Error:', ex)
    else:                               # необязательный оператор
        print('No errors')
        break
    finally:                            # необязательный оператор
        print('Finally block')

print('Result:', z)


"""
FloatingPointError
        |
  OverflowError
        |
ZeroDivisionError
        |
  ArithmeticError
        |
    Exception
"""