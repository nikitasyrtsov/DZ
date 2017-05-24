'''Упражнение 13 Написать прогамму, которая выводит произвольный элемент из списка. Написать программу всеми известными вам способами.'''
import random
spisok = list(input())
n = len(spisok)
elemet = random.choice(spisok)
m = random.randint(0, n)
print(spisok)
print(elemet)
print(random.randrange(1, 100, 2))
print(spisok[m])