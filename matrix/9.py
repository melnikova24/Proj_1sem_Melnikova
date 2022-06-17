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
        if i == 1:
            matrix[i][j] = matrix[i][j] * matrix[i][j]

print('Результат: ')
for v in matrix:
    print(v)