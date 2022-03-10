# Вариант 27.
# В последовательности их N чисел (N-четное) в первой ее половине найти
# сумму элементов меньших 0.

N = 20
NT = []

i = -20

a = lambda a: a != 0 and a % 2 == 0
while i <= N:
    if a(i):
        NT.append(i)
    i += 1

curLen = len(NT) * 0.5

rez = 1
for k, v in enumerate(NT):
    if k < curLen:
        rez *= NT[v]

print("Результат: ", rez)
