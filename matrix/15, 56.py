# В матрице элементы столбца N (N задать с клавиатуры) увеличить в два раза

import random

stl = int(input("Введите кол-во столбцов: "))
str = int(input("Введите кол-во строк: "))
N = int(input("Введите номер столбца: "))
N -= 1

matrix = [[random.randint(-10, 10) for i in range(stl)] for j in range(str)]
print('Исходная: ')
for v in matrix:
    print(v)

for g in range(stl):
    matrix[g][N] = matrix[g][N] * 2

print('Результат: ')
for v in matrix:
    print(v)
