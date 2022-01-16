class Node:
    def __init__(self, value):
        self.__value = value
        self.__next = None

    # def __str__(self):      # __repr__
    #     print('__str__')
    #     return str(self.__value)

    def __repr__(self):
        # print('__repr__')
        return self.__value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, next_node):
        self.__next = next_node


# node = Node(5)
# print(str(node))
# s = str(node)
# print(s)
#
# d = node
# print(d)
# x = Node(node.__repr__())