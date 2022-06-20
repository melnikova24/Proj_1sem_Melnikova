# В матрице элементы второго столбца возвести в квадрат

import random

stl = int(input("Введите кол-во столбцов: "))
str = int(input("Введите кол-во строк: "))
matrix = [[random.randint(-10, 10) for i in range(stl)] for j in range(str)]
print('Исходная: ')
for v in matrix:
    print(v)

for i in range(stl):
    for j in range(str):
        if i == 1:
            matrix[j][i] = matrix[j][i] ** 2

print('Результат: ')
for v in matrix:
    print(v)