'''Упражнение 41
Напишите программу которая выводит, сколько дней осталось до вашего день рождения.
Дату ввести с клавиатуры.
'''
import datetime
y = int(input('Введите год\n'))
m = int(input('Введите месяц\n'))
d = int(input('Введите день\n'))
today = datetime.datetime.now()
a = today.replace(y)
dr = datetime.datetime(y, m, d)
ostalos = dr - a
print(ostalos)
