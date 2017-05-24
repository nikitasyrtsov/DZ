'''Упражнение 14 Дан список с числами. Найти второе наименьшее число.
'''
import random
spisok = sorted(list(set(input())), key = int)
print(spisok[1])