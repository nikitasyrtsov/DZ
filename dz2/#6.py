'''Упражнение 6 Пользователь может ввести число от 0 до 50. Если число делится на 3 вывести "Foo", если делится на 5, то "Bar".
'''
x = int(input('vvedite 4islo'))
if  x >= 0 and x <= 50:
  if x % 3 == 0:
    print('foo')
  if x % 5 == 0:
    print('bar')
else:
  print('vvedite ot 0 do 50')