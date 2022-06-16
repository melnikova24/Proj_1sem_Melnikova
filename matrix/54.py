# В матрице элементы строки N (N задать с клавиатуры) увеличить на 3.

import random

st = int(input("Введите кол-во столбцов: "))
sr = int(input("Введите кол-во строк: "))
N = int(input("Введите номер строки N, ктр. увеличим на 3: "))
N -= 1
matrix = [[random.randint(1, 10) for x in range(st)]for y in range(sr)]

print("Исходная матрица: ")
for v in matrix:
    print(v)

for g in range(st):
    matrix[N][g] += 3

print("Матрица после замены столбца: ")
for v in matrix:
    print(v)