'''Упражнение 8 Напечатать числа от 0 до 6, за исключением 3 и 6.
'''
for i in range(7):
  if i == 3 or i == 6:
    continue
  print(i)