'''Упражнение 24 Напечатать словарь в виде таблицы.
'''
d = {}
for i in range(1,10 + 1):
	d[i] = i * i 
print(d)
for key, value in d.items():
	print('{0:>d} : {1:<3d}'.format(key, value))