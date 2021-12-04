# Вариант 27
# Дано целое число N (>0). Найти сумму 1 + 1/2 + 1/3 + ... + 1/N

N = input("Введите колличество элементов (целое число): ")

while type(N) != float:
    try:
        N = float(N)
    except ValueError:
        print("Введено неверное число")
        N = input("Введите колличество элементов (целое число): ")

    try:
        if N <= 0:
            print("Введено неверное число")
            N = input("Введите колличество элементов (целое число): ")
    except TypeError:
        continue

a = 1
s = 0
while a <= N:
    b = 1/a
    s += b
    a += 1

print(s)