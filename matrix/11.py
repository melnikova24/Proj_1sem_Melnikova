# В матрице элементы первого столбца возвести в куб.

import random

stl = int(input('Введите количество столбцов: '))
str = int(input('Введите количество строк: '))
N = 1

matrix = [[random.randint(-3, 10) for i in range(stl)] for j in range(str)]
print('Исходная: ')
for v in matrix:
    print(v)

for i in range(stl):
    for j in range(str):
        if i == 0:
            matrix[i][j] = matrix[i][j] * matrix[i][j] * matrix[i][j]

print("Матрица после замены столбца: ")
for v in matrix:
    print(v)
