# Вариант №27.
# Разработать программу с применением пакета tk, взяв в качестве условия одну
# любую задачу из ПЗ № 3 – 8.
# Взята задача ПЗ_3_1:
# Даны числа x, у. Проверить истинность высказывания: «Точка с координатами
# (x, у) лежит во второй или третьей координатной четверти»


from tkinter import *

root = Tk()
root.title("PZ_12_2")
root.geometry("730x115")

lbl1 = Label(root, text="Проверка истинности высказывания: "
                        "«Точка с координатами (x,y) лежит в лежит во второй или "
                        "третьей координатной четверти»")
lbl1.place(x=0, y=0)
lbl2 = Label(root, text="Введите первое число")
lbl2.place(x=200, y=20)

lbl3 = Label(root, text="Введите второе число")
lbl3.place(x=200, y=40)
tx = Entry(root, width=10)

tx.place(x=330, y=20)

tx2 = Entry(root, width=10)
tx2.place(x=330, y=40)


def clicked():
    x = tx.get()
    x = int(x)
    y = tx2.get()
    y = int(y)

    if (x < 0) and (y > 0):
        lbl4 = Label(root, text="True", font=("Arial Bold", 10), fg='green')
        lbl4.place(x=310, y=90)

    elif (x < 0) and (y < 0):
        lbl4 = Label(root, text="True", font=("Arial Bold", 10), fg='green')
        lbl4.place(x=310, y=90)

    else:
        lbl4 = Label(root, text="False", font=("Arial Bold", 10), fg='red')
        lbl4.place(x=307, y=90)


bt = Button(root, text='Вывести', command=clicked)
bt.place(x=300, y=60)

root.mainloop()