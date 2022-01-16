
class Mine:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def set_x(self, x):
        if 0 <= x <= 8:
            self.__x = x

    def set_y(self, y):
        if 0 <= y <= 8:
            self.__y = y

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    x = property(get_x, set_x)
    y = property(get_y, set_y)


m = Mine(4, 5)
# print(m.get_x())
# m.set_x(7)
# print(m.get_x())

m.x = 6
print(m.x)

z = 153 + 284 + 1245        # 1.53 + 2.84 + 12.45 = 16.82
print(f'{z//100}грн. {z%100}коп.')


class Mine1:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @x.setter
    def x(self, x):
        if 0 <= x <= 8:
            self.__x = x

    @y.setter
    def y(self, y):
        if 0 <= y <= 8:
            self.__y = y


m1 = Mine1(4, 5)
# print(m.get_x())
# m.set_x(7)
# print(m.get_x())

m1.x = 6
print(m1.x)