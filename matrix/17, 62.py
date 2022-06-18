# В матрице элементы второго столбца заменить элементами из
# одномерного массива соответствующей размерности

import random

stl = int(input('Введите количество столбцов и одномерного массива: '))
str = int(input('Введите количество строк: '))

matrix = [[random.randint(-3, 10) for i in range(stl)] for j in range(str)]
print('Исходная: ')
for v in matrix:
    print(v)

massiv = [random.randint(1, 10) for m in range(stl)]
print('Одномерный массив: ')
print(massiv)

for g in range(stl):
    for t in range(stl):
        matrix[g][1] = massiv[t - g]

print('Результат: ')
for v in matrix:
    print(v)
