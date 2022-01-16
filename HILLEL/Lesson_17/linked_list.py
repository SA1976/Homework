from lesson_17.node import Node


class SingleLinkedList:
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            src_list = nodes.copy()
            node = Node(value=src_list.pop(0))
            self.head = node
            for element in src_list:
                node.next = Node(value=element)
                node = node.next

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.value)
            node = node.next
        nodes.append('None')

        return ' --> '.join(nodes)

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def add_to_head(self, value):
        node = Node(value=value)
        node.next = self.head
        self.head = node

    def add_to_tail(self, value):
        node = Node(value=value)
        if self.head is None:
            self.head = node
            return

        curr_node = None
        for curr_node in self:
            pass

        curr_node.next = node

    def insert_after(self, target_value, new_value):
        if self.head is None:
            raise Exception('List is empty')

        new_node = Node(value=new_value)
        for node in self:
            if node.value == target_value:
                new_node.next = node.next
                node.next = new_node
                return

        raise Exception(f'Node with value {target_value} not found')

    def insert_before(self, target_value, new_value):
        if self.head is None:
            raise Exception('List is empty')

        if self.head.value == target_value:
            self.add_to_head(new_value)
            return

        new_node = Node(new_value)
        prev_node = self.head
        for node in self:
            if node.value == target_value:
                prev_node.next = new_node
                new_node.next = node
                return
            prev_node = node

        raise Exception(f'Node with value {target_value} not found')

    def remove(self, value):
        if self.head is None:
            raise Exception('List is empty')

        if self.head.value == value:
            self.head = self.head.next

        prev_node = self.head
        for node in self:
            if node.value == value:
                prev_node.next = node.next
                return
            prev_node = node

        raise Exception(f'Node with value {value} not found')


lst = SingleLinkedList()
print(lst)
lst.add_to_head('1')
print(lst)
lst.add_to_head('2')
print(lst)
lst.add_to_tail('3')
print(lst)
lst.insert_before('1', '5')
print(lst)
lst.insert_after('1', '6')
print(lst)
lst.remove('1')
print(lst)

lst1 = SingleLinkedList(['1', '2', '3', '4', '5', '6'])
print(lst1)

for el in lst1:
    print(el, end=' ')
print()

lst1.add_to_head('0')
print(lst1)
lst1.add_to_tail('7')
print(lst1)
lst1.insert_after('3', 'a')
print(lst1)
lst1.insert_before('3', 'b')
print(lst1)
lst1.remove('3')
print(lst1)

# def f(a, b, c, d=1, e=3, f=4):
#     pass
#
#
# f(1, 2, 3)
# f(1, 2, 3, 4)
# f(1, 2, 3, 4, 5)
# f(1, 2, 3, 4, 5, 6)
# f(e=6, b=7, c=1, a=7, f=3)