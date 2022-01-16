
class TestClass:
    a = 0

    def __init__(self):
        self.b = 4


tc1 = TestClass()
tc2 = TestClass()
print(tc1.a)
print(tc1.b)

tc1.a = 67
print(tc1.a)
print(tc2.a)
#print(tc1.c) # будет AttributeError - такого параметра нет


class AttributeOfClass:
    a = 9

    def __init__(self):
        self.b = 8

    def to_do(self, b):
        self.b = b
        x = self.b ** 2
        return x


ac = AttributeOfClass()
print('ac.b: ', ac.b)
ac.to_do(6)
print('значение b измененно  передачей в функцию to do', ac.b)
print(AttributeOfClass.__dict__)
print(ac.__dict__)
print(dir(AttributeOfClass))
print(dir(ac))