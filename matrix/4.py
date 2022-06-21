# В матрице найти сумму отрицательных элементов в первой трети матрицы

import random

stl = int(input("Введите кол-во столбцов: "))
str = int(input("Введите кол-во строк: "))
matrix = [[random.randint(-10, 10) for i in range(stl)] for j in range(str)]
print('Исходная: ')
for v in matrix:
    print(v)

n = int(str // 3)
a = []
b = 0
for j in range(str):
    if j < n:
        a.append(matrix[j])
for j in a:
    for g in j:
        if g < 0:
            b += g

print('b: ', b)
