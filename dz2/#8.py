'''Упражнение 8 Написать программу, которая по названию месяца выводит количество дней в месяце. Месяц может быть введён как число. Примечание. Используйте модуль calendar.
'''
import calendar
a={'январь':1,'февраль':2,'март':3,'апрель':4,'май':5,'июнь':6,'июль':7,'август':8,'сентабрь':9,'октябрь':10,'ноябрь':11,'декабрь':12}
month = input('Введите месяц в 2017 году')
if len(month) <= 2:
  month = int(month)
  kol_day = calendar.monthrange(2017, month)
  print('Количество дней',kol_day[1])
else:
  month = month.lower()
  number_month = a.get(month)
  if number_month:
    kol_day = calendar.monthrange(2017, number_month)
    print('Количество дней',kol_day[1])
  else:
    print('Нет такого месяца')
	  
	
	