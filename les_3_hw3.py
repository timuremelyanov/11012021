"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""


def my_func(num_1, num_2, num_3):
    numbers = [num_1, num_2, num_3]
    numbers.pop(numbers.index(min(numbers)))
    return sum(numbers)


print(my_func(50, 0, 100))


"""
Вариант от преподавателя:

def my_func(num_1, nim_2, num_3):
    my_list = [num_1, nim_2, num_3]
    try:
        my_list.pop(my_list.index(min(my_list)))
        return sum(my_list)
    except TypeError:
        return 'Check number'


print(my_func(3, 4, 5))
"""