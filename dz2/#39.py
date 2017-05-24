'''Упражнение 39
Напечатать календарь на заданный год и месяц.
Примечание. Используйте модуль calendar.
'''
import calendar
y = int(input('Введите год\n'))
m = int(input('Введите месяц\n'))
calendar.prmonth(y, m)
