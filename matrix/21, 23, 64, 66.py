# В матрице найти сумму и произведение элементов столбца N (N задать с клавиатуры)

import random

stl = int(input("Введите кол-во столбцов: "))
str = int(input("Введите кол-во строк: "))
N = int(input("Введите номер столбца N: "))
N -= 1
matrix = [[random.randint(1, 10) for x in range(stl)]for y in range(str)]

print("Исходная матрица: ")
for v in matrix:
    print(v)
m_sum = 0
m_mul = 1
for i in matrix:
    m_sum += i[N]
    m_mul *= i[N]
print('Сумма элементов столбца N: ', m_sum)
print('Произведение элементов столбца N: ', m_mul)