"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

with open('les_5_hw5.txt', 'w') as f:
    numbers = input('Введите числа: ')
    f.write(numbers)
    numbers = map(int, numbers.split())
    numbers_sum = sum(numbers)
    print('Сумма: ' + str(numbers_sum))
print('Сумма: ', numbers_sum)
