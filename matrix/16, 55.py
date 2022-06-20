# В матрице элементы последней строки заменить на 0

import random

stl = int(input('Введите количество столбцов: '))
str = int(input('Введите количество строк: '))

matrix = [[random.randint(-3, 10) for i in range(stl)] for j in range(str)]
print('Исходная: ')
for v in matrix:
    print(v)

for i in range(stl):
    for j in range(str):
        if j == str - 1:
            matrix[j][i] = 0

print('Результат: ')
for v in matrix:
    print(v)