# В матрице элементы столбца N (N задать с клавиатуры) увеличить в два раза

import random

stl = int(input("Введите кол-во столбцов: "))
str = int(input("Введите кол-во строк: "))
N = int(input("Введите номер столбца N: "))
N -= 1
matrix = [[random.randint(1, 10) for x in range(stl)]for y in range(str)]

print("Исходная матрица: ")
for v in matrix:
    print(v)

for g in range(stl):
    matrix[g][N] = matrix[g][N] * matrix[g][N]
print("Результат: ")
for v in matrix:
    print(v)
