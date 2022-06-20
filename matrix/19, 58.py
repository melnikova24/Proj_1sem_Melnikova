# В матрице элементы третьей строки заменить элементами из
# одномерного массива соответствующей размерности

import random

stl = int(input('Введите количество столбцов: '))
str = int(input('Введите количество строк и размер массива: '))

matrix = [[random.randint(-3, 10) for i in range(stl)] for j in range(str)]
print('Исходная: ')
for v in matrix:
    print(v)

massiv = [random.randint(-3, 10) for m in range(str)]
print('Одномерный массив: ')
print(massiv)

for g in range(stl):
    for t in range(str):
       matrix[2][g] = massiv[t - g]

print('Результат: ')
for v in matrix:
    print(v)