"""
1. Создать список и заполнить его элементами различных типов данных.
Реализовать скрипт проверки типа данных каждого элемента. Использовать функцию type() для проверки типа.
Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
"""

my_list = ['список', True, -2, 54.5, [1, 2, 'Geekbrains']]
my_list.reverse()
while len(my_list) != 0:
    new_list = my_list.pop()
    print(type(new_list))

"""
Вариант от предподавателя:
"""
# some_var = ['123', 123, 123.0, False]
# for i in some_var:
#     print(type(i))
