# Из матрицы сформировать массив из положительных четных элементов,
# найти их сумму и среднее арифметическое.

import random

stl = int(input("Введите кол-во столбцов: "))
str = int(input("Введите кол-во строк: "))
matrix = [[random.randint(-10, 10) for i in range(stl)] for j in range(str)]
print('Исходная: ')
for v in matrix:
    print(v)

n = []
for g in range(stl):
    for t in range(str):
        if matrix[g][t] > 0 and matrix[g][t] % 2 == 0:
            n.append(matrix[g][t])
print("Массив: ")
print(n)
