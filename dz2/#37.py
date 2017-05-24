'''Упражнение 37
Пользователь вводит дату в следующем формате:
2017-04-29
Вывести дату в формате:
Saturday, 29 September 17.'''
import datetime
date = input('Введите дату в формате ГГГГ-ММ-ДД')
date = date.split('-')
date = datetime.datetime(int(date[0]), int(date[1]), int(date[2]))
print(date.strftime('%A, %d  %B %y.'))
