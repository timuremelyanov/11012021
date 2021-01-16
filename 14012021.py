# print(abs(-5))
# print(abs(5))


# print(5 & 3)
# print(5 | 3)
# print(5 ^ 3)
# print(6 >> 1)
# print(6 << 2)

# print(int('111', 3))
# print(bin(7))
# print(oct(10))
# print(hex(10))

# my_str = 'Konstantin, Petrovich, Ivanov'
# print(my_str.replace(',', '!'))
# print(my_str[0])
# print(my_str + my_str)
# print(my_str[1:6:2])  # [start:stop:step]
# print(my_str[1:6])  # [start:stop:step]
# print(my_str[1:])  # [start:stop:step]
# print(my_str[:5])  # [start:stop:step]
# print(my_str[1::3])  # [start:stop:step]
# print(my_str[-2])
# print(my_str[::-3])
# print(my_str[:-1])

# print(len(my_str))
# print(len(my_str))
# print(my_str.split())

# val = ['Kons', 'trovich', '1', '2']
# print(', '.join(val))
# print(my_str.capitalize())
# print(my_str.title())
# print(my_str.lower())
# print(my_str.upper())
# print(my_str.istitle())
# print(my_str.count('q'))
# print(my_str.find('o'))
# print(my_str.rfind('o'))


# my_list = ['Artyom', 50000, True, 12.3, 'Ab']
# my_list[2] = False
# print(my_list)
# my_list.append(100)
# my_list.insert(1, 100)
# qwe = my_list.pop(0)
# print(my_list, qwe)
# my_list.reverse()
# print(my_list.count('A'))
# print(my_list.index(5000))
# print(12.4 in my_list)

# my_tuple = ('Artyom', 50000, True, 12.3, 'Ab', 50000)
# qwe = list(my_tuple)
# qwe[0] = 'qwe'
# print(qwe)

# my_set = {1, 1, 1, 1, 2, 2, 2, 10, 2, 1001}
# print(my_set)
# qwe = [1, 1, 1, 1, 2, 2, 2, 10, 2, 1001]
# print(len(set(qwe)))
# a = {2, 3, 4}
# b = {4, 5, 6}
#
# # print(a | b)
# # print(a & b)
# # print(a - b)
# # print(a ^ b)
#
# a.remove(100)
# # a.discard(100)
# print(a)


# human = {'name': 'Ivan', 'age': 80, True: 'admin'}
# human['data'] = [1, 11, 1]
# print(human['age'])
# print(type(human))
# print(human.keys())
# print(human.values())
# print(human.items())
# print(human.get('zxc', 'default_val'))
# print(human.get('name', 'default_val'))
# val = human.pop('age')
# val = human.popitem()
# print(human, val)


# try:
#     a = int(input('Введите число: '))
#     print(100 / a)
# except ValueError:
#     print('Введено не число!')
# except ZeroDivisionError:
#     print('Введен 0!')

# my_tuple = ('Artyom', 50000, True, 12.3, 'Ab', 50000)
# human = {'name': 'name', 'age': 80, True: 'admin'}
#
# for key, val in human.items():
#     print(key, val, key == val)

# for key in human:
#     print(key)

# for i in range(10):
#     print(i, 'hello')


# age = 5

# if age >= 18:
#     print('Hello')
# else:
#     print('Bye')

# print('Hello' if age >= 18 else 'Bye')
# access = True if age >= 18 else False
# print(access)

# a = (5)
# b = (5)
# print(a == b)
#
# print(id(a))
# print(id(b))
# print(a is b)

# a = -7
# b = -7
# print(a is b)

import copy

a = [1, 2, 3, [100, 200]]

b = copy.deepcopy(a)
b[3].append(300)

print(a is b)
print(a)
print(b)