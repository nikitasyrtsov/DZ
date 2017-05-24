'''Упражнение 27 Дано n спичек. Пользователь и компьютер поочерёдно берут несколько спичек (от 1 до p за ход). Проигрывает тот, кто делает ход последним. Напишите игру.'''
import random
p = random.randint(2, 5)#количество спичек разрешенное брать за ход
n = random.randint(10, 20)#начальное значение спичек
hod_comp = random.randint(1, p)
n_new = n - hod_comp
print('Количество спичек',n,'.За один ход вы можете брать не более',p,'спичек.','Компьютер ходит первый')
print('Компьютер забрал',hod_comp, 'спичек')
hod_human = input('Ваш ход')
while not hod_human.isdigit():#Проверка на ввод чисел
    print('Вводите цифры')
    hod_human = input('Ваш ход')
hod_human = int(hod_human)
while hod_human > p:#Проверка ввода числа не более p
    print('Вы нарушаете правила игры')
    hod_human = int(input('Ваш ход'))
n_new = n_new - hod_human
print('Осталось спичек',n_new)
while n_new > 1:
    hod_comp = random.randint(1, p)
    n_new = n_new - hod_comp
    print('Компьютер забрал',hod_comp, 'спичек')
    hod_human = int(input('Ваш ход'))
    n_new = n_new - hod_human
    print('Осталось спичек',n_new)
    while hod_human > p:
        print('Вы нарушаете правила игры')
        hod_human = int(input('Ваш ход'))
    if hod_comp >= n_new:
        print('Вы выйграли')
    elif hod_human >= n_new:
        print('Компьютер выйграл')