"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
"""

# dict
month = int(input('enter month\n>>> '))

if 0 < month <= 12:
    season = {1: 'Winter',
              2: 'Winter',
              3: 'Spring',
              4: 'Spring',
              5: 'Spring',
              6: 'Summer',
              7: 'Summer',
              8: 'Summer',
              9: 'Autumn',
              10: 'Autumn',
              11: 'Autumn',
              12: 'Winter'}
    print(season[month])
else:
    print('Incorrect month')

# list

season = ['',
          'Winter',
          'Winter',
          'Spring',
          'Spring',
          'Spring',
          'Summer',
          'Summer',
          'Summer',
          'Autumn',
          'Autumn',
          'Autumn',
          'Winter']
month = int(input('Enter month'))
print(season[month])
