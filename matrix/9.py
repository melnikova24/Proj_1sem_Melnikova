# В матрице элементы второго столбца возвести в квадрат

import random

stl = int(input('Введите количество столбцов: '))
str = int(input('Введите количество строк: '))

matrix = [[random.randint(1, 10) for i in range(stl)] for j in range(str)]
print('Исходная: ')
for v in matrix:
    print(v)

for i in range(stl):
    for j in range(str):
        if i == 0:
            matrix[j][i] = matrix[j][i] * matrix[j][i] * matrix[j][i]

print('Результат: ')
for v in matrix:
    print(v)