a = int(input('Number? '))
hundreds = a // 100
tens_and_units = a % 100
tens = tens_and_units // 10
units = tens_and_units % 10
result = units * 100 + tens * 10 + hundreds
print('Converted number = ', result)
