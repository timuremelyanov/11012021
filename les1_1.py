# print('Hello world!')  # to console
# Ctrl + /
#
# print(1 + 1)
# print(1 - 1)
# print(5 * 3)
# print(6 / 9)


# print(10 // 3)
# print(10 % 3)
# print(5 ** 3)


# x = 5
# print(x + 9)
# x += 10
# print(x)

# speed_car = 50  # snake_style

# my_string = 'Hello'
# print(type(my_string))

# my_int = 50
# print(type(my_int))

# my_float = 5.1
# print(type(my_float))

# my_bool = True  # False
# print(type(my_bool))


# num = 5
# num = 'hello'
# print(num)

# print(5 > 6)
# print(5 < 6)
# print(5 =< 6)
# print(5 => 6)
# print(5 == 6)
# print(5 != 6)
# x = - 10
# print(5 != 6 and x > 0)
# print(5 != 6 or x > 0)

# x = int(input('Ввеите цифру: '))
# print(x + 1)


# orig_pass = 'qwerty'
#
# user_pass = input('Введите пароль: ')
#
# if user_pass == orig_pass:
#     print('Авторизован успешно!')
#     if input('Пароль админа: ') == 'admin':
#         print('Вы теперь админ')
#     else:
#         print('Не админ')
# else:
#     print('Ошибка пароля!')





# color = 'red'
#
# if color == 'red':
#     print('Красный')
# elif color == 'green':
#     print('Зеленый')
# elif color == 'blue':
#     print('Синий')
# else:
#     print('Неизвестный')


# number = int(input('Число: '))
#
# while True:
#     number += 1
#     if number == 5:
#         continue
#     print(number)
#     if number == 11:
#         break


name = 'Ivan'
surname = 'Ivanov'
age = 80

print('Имя:', name, 'Фамилия:', surname, 'Возраст:', age)
print('Имя: %s Фамилия: %s Возраст: %d' % (name, surname, age))
print('Имя: {} Фамилия: {} Возраст: {}'.format(name, surname, age))
print(f'Имя: {name} Фамилия: {surname} Возраст: {age}')

my_float = 5.659615461541654
print(f'{my_float:.1f}')