'''Упражнение 10 Написать программу, котора считает количество символов и чисел в строке.
'''
st = input('Введите символы')
l = list(st)
l1 = []
l2 = []
for i in l:
    if i.isdigit():
        l1.append(i)
    elif i.isalpha() or i.isspace():
        l2.append(i)
print('Количество цифр', len(l1))
print('Количество букв', len(l2))