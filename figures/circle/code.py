def circle_perimetr():
    print("Команды: 1-Ввести свой радиус.  2-Использовать дефолтный радиус.")
    n = int(input("Выберите команду 1 или 2: "))
    while (n != 1) and (n != 2):
        try:
            print("Такой команды нет")
            n = int(input("Выберите команду 1/2: "))
        except ValueError:
            pass
    if n == 1:
        r = int(input("Введите радиус: "))
    else:
        r = default_radius
    pi = 3.14
    p = 2*pi*r
    print("Длина окружности = ", p)


def circle_area():
    print("Команды: 1-Ввести свой радиус.  2-Использовать дефолтный радиус.")
    n = int(input("Выберите команду 1/2: "))
    while (n != 1) and (n != 2):
        try:
            print("Такой команды нет")
            n = int(input("Выберите команду 1 или 2: "))
        except ValueError:
            pass
    if n == 1:
        r = int(input("Введите радиус: "))
    else:
        r = default_radius
    pi = 3.14
    s = pi*r**2
    print("Площадь окружности: ", s)


default_radius = 5
