"""
 - public           открытый интерфейс
 - protected        защищённая часть реализации
 - private          закрытая часть реализации
"""


class Computer:
    def __init__(self, cpu, memory, hdd):
        self.cpu = cpu              # public
        self._memory = memory       # protected
        self.__hdd = hdd            # private

    def print_computer(self):
        print(f'CPU: {self.cpu}, MEMORY: {self._memory}, HDD: {self.__hdd}')


comp = Computer(2300, 16000, 2000)
print(dir(comp))
print(comp.cpu)
print(comp._memory)
print(comp._Computer__hdd)
comp.print_computer()