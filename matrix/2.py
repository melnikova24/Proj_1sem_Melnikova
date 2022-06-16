# В матрице отрицательные элементы возвести в квадрат.

import random

stl = int(input('Введите колчетсво столбцов: '))
str = int(input('Введите колчетсво строк: '))

matrix = [[random.randint(-4, 10) for i in range(stl)] for j in range(str)]
print('Исходная матрица: ')
for v in matrix:
    print(v)

for g in range(stl):      # проверяем элементы строк и столбиков на < 0
    for t in range(str):
        if matrix[g][t] < 0:
            matrix[g][t] = matrix[g][t] * matrix[g][t]

print('Результат: ')
for v in matrix:
    print(v)