# В матрице найти суммы элементов каждой строки и поместить их в
# новый массив. Выполнить замену элементов третьего столбца исходной
# матрицы на полученные суммы

import random

stl = int(input("Введите кол-во столбцов: "))
str = int(input("Введите кол-во строк: "))
matrix = [[random.randint(-10, 10) for i in range(stl)] for j in range(str)]
print('Исходная: ')
for v in matrix:
    print(v)

m_sum = []
for j in range(str):
    m_sum.append(sum(matrix[j]))
for j in range(str):
    matrix[j][2] = m_sum[j]

print('Сумма каждой строки', m_sum)
print('Результат: ')
for v in matrix:
    print(v)