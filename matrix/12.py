# Сгенерировать матрицу, в которой элементы больше 10 заменяются на 0.

import random

stl = int(input('Введите количество столбцов: '))
str = int(input('Введите количество строк: '))

matrix = [[random.randint(1, 20) for i in range(stl)] for j in range(str)]
print('Исходная: ')
for v in matrix:
    print(v)

for g in range(stl):
    for t in range(str):
        if matrix[g][t] > 10:
            matrix[g][t] = 0

print('Результат: ')
for v in matrix:
    print(v)