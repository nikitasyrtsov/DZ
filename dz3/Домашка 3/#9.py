'''Упражнение 9 Напечатать числа Фибоначчи от 1 до 50. Числа напечатать в одну строку.
'''
fib1 = 1
fib2 = 1
for i in range(1,50):
    fib_sum = fib1 + fib2
    fib1 = fib2
    fib2 = fib_sum
    print(fib_sum, end = ' ')