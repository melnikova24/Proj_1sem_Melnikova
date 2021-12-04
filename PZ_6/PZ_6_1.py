# Вариант 27
# Дан список A размера N. Найти минимальный элемент из его элементов
# с чётными номерами: A2, A4, A6,... .

import random

N = int(input("Введите размер списка A: "))

A = []
t = 0
while t < N:
    A.append(random.randint(0, 100))
    t += 1

B = []
for I in range(N):
    if I % 2 == 0:
        B. append(A[I - 1])
print(min(B))
