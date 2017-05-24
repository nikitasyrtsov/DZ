import calendar
import random
l3 = [1, 2, 3, 4]
l4 = [4, 5, 6, 7]
l5 = list(set(l3) ^ set(l4))
if l5:
	print(l5)
else:
	print('net obshih')
