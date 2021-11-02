"""
1. Представьте себе бухгалтерскую книгу в книжном магазине. В этой книге хранятся
записи о номере заказа, названии книги, количестве и стоимости одной книги, как
представлено ниже, в таблице.

+--------------+------------------------------------+----------+----------------+
| Order Number |       Book Title and Author        | Quantity | Price per Item |
+--------------+------------------------------------+----------+----------------+
|        34587 | Learning Python, Mark Lutz         |        4 |          40.95 |
|        98762 | Programming Python, Mark Lutz      |        5 |          56.80 |
|        77226 | Head First Python, Paul Barry      |        3 |          32.95 |
|        88112 | Einfuhrung in Python3, Bernd Klein |        3 |          24.99 |
+--------------+------------------------------------+----------+----------------+

Напишите программу на Python, которая на вход получает список списков:
[
	[34587, 'Learning Python, Mark Lutz', 4, 40.95],
	[98762, 'Programming Python, Mark Lutz', 5, 56.80],
	[77226, 'Head First Python, Paul Barry', 3, 32.95],
	[88112, 'Einfuhrung in Python3, Bernd Klein', 3, 24.99]
]

и возвращает список кортежей. Каждый кортеж состоит из номера заказа и произведения
цены на товары и количества. Стоимость заказа должна быть увеличена на $10, если она меньше $100. Программа должна использовать lambda, map, однострочный if, round и list.

"""


def order_formation(a):

    res = list(map(lambda elm: (elm[0], round(elm[2] * elm[3], 2) if elm[2] * elm[3] >= 100 else round(elm[2] * elm[3] + 10, 2)), a))

    return res


acc_book = [
    [34587, 'Learning Python, Mark Lutz', 4, 40.95],
    [98762, 'Programming Python, Mark Lutz', 5, 56.80],
    [77226, 'Head First Python, Paul Barry', 3, 32.95],
    [88112, 'Einfuhrung in Python3, Bernd Klein', 3, 24.99]
    ]

order = order_formation(acc_book)

print(order, type(order))
for el in order:
    print(el, type(el))
