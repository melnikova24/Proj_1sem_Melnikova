# В матрице элементы последнего столбца заменить на -1.

import random         # проблемы с выбором последнего столбца

stl = int(input('Введите количество столбцов: '))
str = int(input('Введите количество строк: '))

matrix = [[random.randint(1, 10) for i in range(stl)] for j in range(str)]
print('Исходная: ')
for v in matrix:
    print(v)

for j in range(str):
    for i in range(stl):
        if i == stl - 1:
            matrix[j][i] = -1

print('Результат: ')
for v in matrix:
    print(v)