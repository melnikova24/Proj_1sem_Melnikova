# В матрице найти минимальный и максимальные элементы

import random

stl = int(input('Введите количество столбцов : '))
str = int(input('Введите количество строк: '))

matrix = [[random.randint(-3, 10) for i in range(stl)] for j in range(str)]
print('Исходная: ')
for v in matrix:
    print(v)

min = [0][0]
max = [0][0]
for g in range(stl):
    for t in range(str):
        if (matrix[g][t] < min):
            min = matrix[g][t]
        if (matrix[g][t] > max):
            max = matrix[g][t]
print(min)
print(max)