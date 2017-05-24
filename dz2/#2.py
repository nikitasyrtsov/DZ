'''Упражнение 2 Пользователь вводит число. Очистить ввод пользователя, проверить что введено только одно число. Вывести является ли число чётным.
'''
x = input('vvedite 4islo')
y = x.split()
if  len(y) == 1:
  if int(x) % 2 == 0:
    print('4etnoe')
  else:
    print('ne4etnoe')
else:
  print('vvedite odno 4islo')