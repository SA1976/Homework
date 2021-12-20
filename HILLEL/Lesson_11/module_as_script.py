# from mod_1 import lst, print_list
# from mod_1 import lst, print_list
# from mod_1 import lst, print_list
# from mod_1 import lst, print_list
"""
Любой модуль может исполять 2 роли:
- как скрипт - то есть исполняться целиком
когда Питон видит импорт "from mod_1 import lst", то он исполняет весь файл целиком
Выходы:
- удалять или комментировать имполняемые строки кода
- использовать if __name__ == '__main__': см mod1 в этом уроке

print(dir(importlib)) - список функций модуля
print(help("importlib")) - описание модуля и его функций, имя модуля должно быть в виде строки

reload.importlib(имя модуля) - может перзагружзить модуль при работающей программе
sleep.time(сек) - приостанавливает работу программы на указанное время
"""
from mod_1 import lst
from mod_1 import print_list

# print_list(lst)

# import importlib
from importlib import reload
from time import sleep

import mod_1 # паузы для того что бы успеть внести изменения в mod1
sleep(5)

reload(mod_1)
sleep(5)

reload(mod_1)
sleep(5)

reload(mod_1)
sleep(5)

reload(mod_1)