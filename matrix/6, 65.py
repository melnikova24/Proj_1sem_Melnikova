# Из матрицы сформировать массив из положительных четных элементов,
# найти их сумму и среднее арифметическое

import random

stl = int(input('Введите количество столбцов: '))
str = int(input('Введите количество строк: '))

matrix = [[random.randint(-3, 10) for i in range(stl)] for j in range(str)]
print('Исходная: ')
for v in matrix:
    print(v)

n = []
for i in matrix:
    for t in i:
        if t > 0 and t % 2 == 0:
           n.append(t)

print('Массив из положительных четных элементов: ')
print(n)
print('Сумма элементов массива: ', sum(n))
print('Среднее арифметическое элементов массива: ', sum(n)/len(n))