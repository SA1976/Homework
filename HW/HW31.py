def param_for_action():  # выбор параметров для методов сортировки группы из GroupClass
    # и метода изменения данных студента из StudentClass
    print('Please choose parametr for action:')
    print('press N for name')
    print('press S for surname')
    print('press A for age')
    print('press G for gender')
    while True:
        n = (input()).title()
        if n not in ('N', 'S', 'A', 'G'):
            print('Incorrect param. Please try again')
        else:
            break
    return n


class GroupClass:
    def __init__(self):
        self.st_list = []
        self.group_name = str

    def add_marks_for_group(self):  # добавление оценок каждому студенту группы
        for el in self.st_list:
            el.add_marks()   # вызов метода из StudentClass

    def change_group_name(self, new_name):  # измененение названия группы
        self.group_name = new_name.title()
        return self

    def add_student_to_group(self, *args):  # добавление студента в группу
        if args:  # с помощью переменных
            for param in args:
                self.st_list.append(param)
        else:  # добавление нового студента руками
            print('Add new student')
            tmp = StudentClass()
            tmp.student_creation()
            self.st_list.append(tmp)

    def delete_student_from_group(self, a):  # удаление студента из группы
        for i in range(len(self.st_list)):
            if self.st_list[i].surname == a.surname and self.st_list[i].name == a.name and self.st_list[i].age == a.age:
                c = i
        self.st_list.pop(c)
        return self

    def print_group_info(self):  # вывод группы на экран
        i = 1
        print(f'{self.group_name} :')
        for el in self.st_list:
            print(f'{i}.', end="")  # нумерация записей при выводе
            el.print_student_info()  # вызов метода из StudentClass
            i += 1

    def calculate_group_average_rating(self):  # средняя оценка группы
        tmp = 0
        for el in self.st_list:
            tmp += el.calculate_average_mark()  # вызов метода из StudentClass
        return round(tmp / len(self.st_list), 2)

    def sort_group_by_personal_info(self):  # сортирует группу по имени/фамилии/возрасту/пол
        param = param_for_action()
        if param == 'S':
            self.st_list.sort(key=lambda x: x.surname)
        if param == 'N':
            self.st_list.sort(key=lambda x: x.name)
        if param == 'A':
            self.st_list.sort(key=lambda x: x.age)
        if param == 'G':
            self.st_list.sort(key=lambda x: x.gender)
        return self

    def sort_group_by_marks(self):  # сортировка группы по оценкам
        return self.st_list.sort(key=lambda x: x.average_mark)


class StudentClass:
    def __init__ (self, age='?', gender='?', student_name='xxx',
                  student_surname='xxxxx', grades=[]):
        self.name = student_name
        self.surname = student_surname
        self.grades = grades
        self.age = age
        self.gender = gender
        self.average_mark = 0

    def student_creation(self):  # создание студента руками
        self.name = input('Please enter student name :').title()
        self.surname = input('Please enter student surname :').title()
        self.age = input('Please enter student age: ')
        self.gender = input('Please enter student gender: ').title()

    def correction_student_info(self):  # коррекция данных студента
        flag = True
        while flag:
            param = param_for_action()
            if param == 'N':
                self.name = input(f'Ready to correct field name {self.name}: ').title()
            elif param == 'S':
                self.surname = input(f'Ready to correct field surname {self.surname}: ').title()
            elif param == 'A':
                self.age = input(f'Ready to correct field age {self.age}: ')
            elif param == 'G':
                self.gender = input(f'Ready to correct field gender {self.gender} M(ale)/F(emale):')
            m = input(' Any key + Enter to ontinue correction. ''Z''+ Enter for exit ').title()
            if m == 'Z':
                break

    def add_marks(self):  # добавление любого количества оценок студенту. окончание цикла - 0
        while True:
            try:
                flag = False
                print(f'Add next mark for student {self.name, self.surname}. \nPress ''0'' for finish')
                print('Present grades: ', self.grades)
                print('Average mark: ', self.average_mark, "\n?")
                while not flag:
                    m = int(input())
                    if m == 0:
                        break
                    elif m in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12):
                        self.grades.append(m)
                        print(self.grades)
                    else:
                        print('Incorrect mark. Try agine.')
            except ValueError as ve:
                print('Not int value: ', ve)
            else:
                if len(self.grades) > 0:  # сразу пересчитываем среднюю оценку
                    self.average_mark = self.calculate_average_mark()
                    print(f'Average mark:{self.average_mark}')
                    break
        return self.grades, self.average_mark

    def calculate_average_mark(self):  # пересчёт средней оценки
        self.average_mark = round(sum(x for x in self.grades) / len(self.grades), 2)
        return self.average_mark

    def print_student_info(self, *args):  # вывод данных студента

        print(f' {self.name} {self.surname}, gender: {self.gender}, age: {self.age}')
        print(f'Present marks: {self.grades}')
        if len(self.grades) > 0:
            self.average_mark = self.calculate_average_mark()
            print(f'Average mark: {self.average_mark}')

        if args:
            for el in args:
                print(f' {el.name} {el.surname}, gender: {el.gender}, age: {el.age}')
                print(f'Present marks: {el.grades}')
                if len(el.grades) > 0:
                    el.average_mark = el.calculate_average_mark()
                    print(f'Average mark: {el.average_mark}')


if __name__ == '__main__':


# данные для демонстрации GroupClass
    a1 = StudentClass()
    a2 = StudentClass()
    a3 = StudentClass()
    a4 = StudentClass()
    a5 = StudentClass()
    a6 = StudentClass()
    a1.name, a2.name, a3.name, a4.name, a5.name, a6.name = 'Vasiliy', 'Tom', 'Jhon', 'Sveta', 'Mary', 'Hanna'
    a1.surname, a2.surname, a3.surname, a4.surname, a5.surname, a6.surname = 'Ivanov', 'Mouse', 'Smith', \
                                                                             'Ivanov', 'Darling', 'Lilmod'
    a1.age, a2.age, a3.age, a4.age, a5.age, a6.age = (22, 24, 34, 19, 25, 30)
    a1.gender, a2.gender, a3.gender, a4.gender, a5.gender, a6.gender = 'M', 'M', 'M', 'F', 'F', 'F'
    a1.grades = [10, 10, 12, 8]
    a2.grades = [8, 9, 7, 6]
    a3.grades = [4, 8, 9, 8]
    a4.grades = [4, 6, 4, 3]
    a5.grades = [11, 3, 4, 7]
    a6.grades = [12, 12, 12, 12]

    # a = StudentClass()
    # a.print_student_info()
    # a.student_creation() # cоздание нового студента руками
    # a.print_student_info()
    # exit(0)

    # a1.print_student_info()
    # a1.correction_student_info() # изменение имени/фамилии/возраста/пола студента
    # a1.print_student_info()
    # exit(0)

    # # выводим инфо нескольких студентов
    # StudentClass.print_student_info(a1, a4, a6)
    # print('_' * 30)
    # exit(0)

    # вывод среднего балла отдельного студента
    print(f' {a1.name, a1.surname} average mark {a1.calculate_average_mark()}')  # 10.0
    # print(f' {a2.name, a2.surname} average mark {a2.calculate_average_mark()}')  # 7.5
    # print(f' {a3.name, a1.surname} average mark {a3.calculate_average_mark()}')  # 7.25
    # print(f' {a4.name, a1.surname} average mark {a4.calculate_average_mark()}')  # 4.25
    # print(f' {a5.name, a1.surname} average mark {a5.calculate_average_mark()}')  # 6.25
    # print(f' {a6.name, a1.surname} average mark {a6.calculate_average_mark()}')  # 12.0
    print('_' * 30)

    # добавляем оценки студенту
    a1.add_marks()
    print('-' * 20)


    group_all = GroupClass()
    group_1 = GroupClass()
    group_2 = GroupClass()
    group_all.group_name = 'All class'  # общая группа для всех студентов
    group_1.group_name = 'French_group'  # группа франц языка
    group_2.group_name = 'English_group'  # группа англ языка

group_all.add_student_to_group(a1, a2, a3, a4, a5, a6) # добавление всех в общую группу
group_1.add_student_to_group(a1, a2, a3)
group_2.add_student_to_group(a4, a5, a6)
print('_'*30)

print('Personal info of all students')
group_all.print_group_info()
print('_'*30)

print('Overall average rating: ', group_all.calculate_group_average_rating()) # 7.88 - рейтинг всего класса
print('French group rating: ', group_1.calculate_group_average_rating()) # 8.25 -рейтинг group_1
print('English group rating: ', group_2.calculate_group_average_rating()) # 7.5 - рейтинг group_2

# # добавление оценок группе
# group_2.add_marks_for_group()
# print(group_2.calculate_group_average_rating() # 7.5 - рейтинг group_2

# # измененние данных студента
# a1.correction_student_info()
# group_1.print_group_info()


# перемещение студента из группы 1 в группу 2
group_1.delete_student_from_group(a3)  # из группы all удален студент Jhon Smith
print('Jhon Smith is deleted')
group_1.print_group_info()
print('_'*30)
group_2.add_student_to_group(a3)
group_2.print_group_info()
print('Jhon Smith is added')
print('_'*30)
exit(0)

group_all.sort_group_by_personal_info()  # группа all отсортирована по одному из параметров имя/фамилия/возраст/пол
print('Group sorted by name/surname/age/gender:')
group_all.print_group_info()
print('_'*30)

group_all.sort_group_by_marks()  # группа all отсортирована по средней оценке
print('Group sorted by average mark:')
group_all.print_group_info()

