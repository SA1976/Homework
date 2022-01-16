class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f'Имя: {self.name}, Возраст: {self.age}')


class Employee(Person):
    def __init__(self, name, age, company):
        super().__init__(name, age)
        self.company = company

    def display_info(self):
        super().display_info()
        print(f'Компания: {self.company}')


class Student(Person):
    def __init__(self, name, age, university):
        super().__init__(name, age)
        self.university = university

    def display_info(self):
        print(f'Студент {self.name} учится в {self.university}')


lst = [Person('Tom', 23), Student('Bob', 19, 'Harvard'), Employee('Sam', 35, 'Google')]
print(lst)

for person in lst:
    person.display_info()
    print('-' * 30)