# Вариант 27.
# В соответствии с номером варианта перейти по ссылке на прототип.
# Реализовать его в IDE PyCharm Community с применением пакета tk.
# Получить интерфейс максимально приближенный к оригиналу
# https://pbs.twimg.com/media/CWgn_1CUAAAVQP4.png:large

from tkinter import *

root = Tk()
root.title("PZ_12_1")
root.geometry("450x450")
root.configure(bg="#d3d3d3")

Label(text="Регион", width=65, height=3, fg="black", bg="#d3d3d3", font="arial 11").place(x=-220, y=5)
Label(text="Район", width=65, height=3, fg="black", bg="#d3d3d3", font="arial 11").place(x=-220, y=60)
Label(text="Город", width=65, height=3, fg="black", bg="#d3d3d3", font="arial 11").place(x=-220, y=110)
Label(text="Улица", width=65, height=3, fg="black", bg="#d3d3d3", font="arial 11").place(x=-220, y=160)

Label(text="Дом", width=65, height=3, fg="black", bg="#d3d3d3", font="arial 11").place(x=-225, y=230)
Entry(width=10, font="arial 11").place(x=130, y=250)
Label(text="Стр./вл.", width=65, height=3, fg="black", bg="#d3d3d3", font="arial 11").place(x=-215, y=280)
Entry(width=9, font="arial 12").place(x=130, y=300)
Label(text="Корпус", width=10, height=3, fg="black", bg="#d3d3d3", font="arial 11").place(x=220, y=230)
Entry(width=9, font="arial 12").place(x=320, y=250)
Label(text="Кв./Офис", width=10, height=3, fg="black", bg="#d3d3d3", font="arial 11").place(x=220, y=280)
Entry(width=9, font="arial 12").place(x=320, y=300)
Button(root, width=6, text="ОК",  bg=("#e3e1dd"), fg="#3fa6da", font=("Bodoni MT Black", 20)).place(x=100, y=350)
Button(root, width=7, text="ОТМЕНА", bg=("#e3e1dd"),  fg="#3fa6da", font=("Bodoni MT Black", 20)).place(x=250, y=350)

from tkinter.ttk import *

combo = Combobox(root, width=47, font=("Arial", 10))
combo["values"] = ("[не выбранo]", "Ростовская область", "Московская область", "Архангельская область",
                  "Рязанская область", "Белгородская область",)
combo.current(0)            #Элемент выбранный по умолчанию
combo.place(x=50, y=50)

combo = Combobox(root, width=47, font=("Candara Light", 10))
combo["values"] = ( "Выберите район", "Аксайский район",  "Пушкинский район",  "Приморский район",
                   "Михайловский район",  "Шебекинский район")
combo.current(0)
combo.place(x=50, y=100)

combo = Combobox(root, width=47, font=("Candara Light", 10))
combo["values"] = ("Выберите город", "г. Аксай", "г. Пушкино", "г. Архангельск", "г. Михайлов", "г. Шебекино")
combo.current(0)
combo.place(x=50, y=150)

combo = Combobox(root, width = 47, font=("Candara Light", 10))
combo["values"] = ("Выберите улицу", "ул. Советская", "ул. Учинская", "ул. Салютина", "ул. Герцена",
                   "ул. Космическая")
combo.current(0)
combo.place(x=50, y=200)


root.mainloop()