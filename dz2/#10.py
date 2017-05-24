'''Упражнение 10 Написать программу, которая выводит следующий день после введённой даты. Дата вводится как год, день и число.
Примечание. Используйте модуль datetime. У объекта datetime  есть метод replace, либо используте объект timedelta.
'''
import datetime
year = int(input('год'))
month = int(input('месяц'))
day = int(input('день'))
print(datetime.date(year, month, day+1))