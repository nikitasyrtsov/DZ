'''Упражнение 21 Написать программу, которая находит элементы с списке, значение которых больше заданного.
'''
n = int(input())
sp = [1, 1, 2, 3, 3, 11, 2, 4, 2, 4, 5, 43, 67, 21, 11]
for i in sp:
    if i > n:
       print(i) 