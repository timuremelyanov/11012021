"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""


def div_func(num_1, num_2):
    try:
        result = num_1 / num_2
    except ZeroDivisionError:
        return 'Деление на 0!'
    return result


print(div_func(float(input('Введите число 1\n>>> ')), float(input('Введите число 2\n>>> '))))


'''
Вариант от преподавателя:


def my_div(num_1, num_2):
    try:
        num_1, num_2 = float(num_1), float(num_2)
        answer = num_1 / num_2
    except ValueError:
        return 'error', 'ошибка числа'
    except ZeroDivisionError:
        return 'Деление на 0!'
    return answer


print(my_div(input(), input()))
'''