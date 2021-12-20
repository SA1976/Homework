"""
Реализовать класс цифрового счетчика. В классе реализовать методы:
- установки максимального, минимального и начального значения счётчика
- увеличения счетчика на 1
- возвращения текущего значения счётчика
"""


class MeterClass:
    a = 'electricity'
    b = 'water'
    c = 'gas'
    d = 'other'

    def __init__(self, value=0, max = 100, min = 0):
        self.max = max
        self.min = min
        self.collector = 0  # хранит количество совершённых полных оборотов счетчика

        if self.min <= value < self.max:  # если значение при установке не попадает в границы "min-max"
            self.present_value = value
        else:
            self.present_value = self.min # - устанавливаем min

    def meter_increasing(self):
        self.present_value = self.present_value + 1  # изменяем параметр на 1 ед
        if self.present_value == self.max:  # если выходим на max значение, то  present_value возвращается к min
            self.present_value = self.min
            self.collector = self.collector + 1 # и добавляем 1 оборот в коллектор

        return self.present_value

    def get_meter_val(self):  # данные коллектора оборотов и текущее значение счетчика
        return (f'Turnovers completed {self.collector}: meter\'s value {self.present_value}')

meter1 = MeterClass()
print('meter1: ', meter1.get_meter_val())
print('meter1 max value:', meter1.max)
print('meter1 min value:', meter1.min)
print()

meter1 = MeterClass(34, 200, 10)
print('meter1: ', meter1.get_meter_val())
print('meter1 max value:', meter1.max)
print('meter1 min value:', meter1.min)
print()

meter2 = MeterClass(-35) # начальное значение меньше min
print('meter2: ', meter2.get_meter_val())
print('meter2 max value:', meter2.max)
print('meter2 min value:', meter2.min)
print()

meter2 = MeterClass(110) # начальное значение больше max
print('meter2: ', meter2.get_meter_val())
print()

meter2 = MeterClass(70) # начальное значение в нужном диапазоне
print('meter2: ', meter2.get_meter_val())
print()

for i in range(15): # +15 прокруток счетчика
    meter2.meter_increasing()
print('meter2: ', meter2.get_meter_val())
print()

for i in range(3050): # еще крутим счетчик
    meter2.meter_increasing()
print('meter2: ', meter2.get_meter_val())
