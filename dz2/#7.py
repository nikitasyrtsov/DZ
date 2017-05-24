'''Упражнение 7 Написать программу, которая проверяет, достаточно ли сложный пароль. Сообщения выводить только в конце после всех проверок. Пароль должен: 1. Содержать символы в нижнем и верхнем регистре. 2. Содержать числа. 3. Содержать специальный символ. 4. Длинна пароля от 6 до 16 символов.
'''
import string
password = input('Придумайте пароль')
lower = string.ascii_lowercase
upper = string.ascii_uppercase
numbers = string.digits
special = string.punctuation
errors = []
if not set(password) & set(lower):
  errors.append('Нет маленьких букв')
if not set(password) & set(upper):
  errors.append('Нет больших букв')
if not set(password) & set(special):
  errors.append('Нет специальных символов')
if len(password) < 6 or len(password) > 16:
  errors.append('Пароль должен содержать от 6 до 16 символов')
if not set(password) & set(numbers):
  errors.append('Нет цифр')
else:
  print('OK')
print('\n'.join(errors))