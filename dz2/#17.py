'''Упражнение 17 Написать программу, которая проверяет существует ли ключ в данном словаре. Если существует, вывести значение, если не существует вывести "Пусто!".
'''
d = {1:2, 2:3, 3:4, 4:5, 5:6}
key = int(input('Введите ключ'))
if d.get(key):
  print('Значение', d.get(key))
else:
  print('Нет такого ключа')