﻿'''Упражнение 27
Разработчик получает по 2$ за каждую закрытую в своём коде ошибку. Если программист за
месяц исправляет больше 5 ошибок он полчает 10$ премии, но если более 10 ошибок, то за
каждую ошибку из зарплаты отнимают 3$, но не более 50$.
Пользователь вводит число ошибок. Вывести сколько денег получит разработчик.
'''
errors = int(input('Введите количество закрытых ошибок\n'))
zp = 1000
if errors < 10 and errors >= 5:
    zp += (errors * 2) + 10
else:
    if errors * 3 <= 50:
        zp -= (errors * 3)
    zp -= 50
print('Зарплата', zp)

