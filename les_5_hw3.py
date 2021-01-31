"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""

with open('les_5_hw3.txt') as f:
    lines = f.readlines()

salaries = []
for line in lines:
    name, salary = line.split('-')
    salaries.append(int(salary))
    if int(salary) < 20000:
        print(line, end='')
print('Средняя з/п по компании:', sum(salaries) / len(salaries))
