# Приложение ИНТЕРНЕТ-МАГАЗИН для некоторой организации. БД должна
# содержать таблицу Продажи со следующей структурой записи: ФИО покупателя, товар,
# единицу измерения (штуки, килограммы, литры), количество, стоимость.
# БД должна обеспечивать получение информации по стоимости.

import tkinter as tk
from tkinter import ttk
import sqlite3 as sq


class Main(tk.Frame):

    """Класс для главного окна"""

    def __init__(self, root):
        super().__init__(root)
        self.init_main()
        self.db = db
        self.view_records()

    def init_main(self):
        toolbar = tk.Frame(bg='#41e8bf', bd=4)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        self.add_img = tk.PhotoImage(file="BD_PZ_16/11.gif")
        self.btn_open_dialog = tk.Button(toolbar, text='Добавить покупателя', command=self.open_dialog, bg='#a6f8e4', bd=0,
                                    compound=tk.TOP, width=150, image=self.add_img)
        self.btn_open_dialog.pack(side=tk.LEFT)

        self.update_img = tk.PhotoImage(file="BD_PZ_16/12.gif")
        btn_edit_dialog = tk.Button(toolbar, text="Редактировать", command=self.open_update_dialog, bg='#a6f8e4',
                                    bd=0, compound=tk.TOP, width=150, image=self.update_img)
        btn_edit_dialog.pack(side=tk.LEFT)

        self.delete_img = tk.PhotoImage(file="BD_PZ_16/13.gif")
        btn_delete = tk.Button(toolbar, text="Удалить запись", command=self.delete_records, bg='#a6f8e4',
                                    bd=0, compound=tk.TOP, width=150, image=self.delete_img)
        btn_delete.pack(side=tk.LEFT)

        self.search_img = tk.PhotoImage(file="BD_PZ_16/14.gif")
        btn_search = tk.Button(toolbar, text="Поиск записи", command=self.open_search_dialog, bg='#a6f8e4',
                               bd=0, compound=tk.TOP, width=150, image=self.search_img)
        btn_search.pack(side=tk.LEFT)

        self.refresh_img = tk.PhotoImage(file="BD_PZ_16/15.gif")
        btn_refresh = tk.Button(toolbar, text="Обновить экран", command=self.view_records, bg='#a6f8e4',
                               bd=0, compound=tk.TOP, width=150, image=self.refresh_img)
        btn_refresh.pack(side=tk.LEFT)

        self.tree = ttk.Treeview(self, columns=('add_FIO', 'product', 'measurement', 'quantity', 'price'), height=15, show='headings')

        self.tree.column('add_FIO', width=220, anchor=tk.CENTER)
        self.tree.column('product', width=190, anchor=tk.CENTER)
        self.tree.column('measurement', width=130, anchor=tk.CENTER)
        self.tree.column('quantity', width=120, anchor=tk.CENTER)
        self.tree.column('price', width=100, anchor=tk.CENTER)

        self.tree.heading('add_FIO', text='ФИО покупателя')
        self.tree.heading('product', text='Товар')
        self.tree.heading('measurement', text='Един. измерения')
        self.tree.heading('quantity', text='Количество')
        self.tree.heading('price', text='Стоимость')

        self.tree.pack()

    def records(self, add_FIO, product, measurement, quantity, price):
        self.db.insert_data(add_FIO, product, measurement, quantity, price)
        self.view_records()

    def update_record(self, add_FIO, product, measurement, quantity, price):
        self.db.cur.execute("""UPDATE users SET add_FIO=?, product=?, measurement=?, quantity=?, price=? WHERE add_FIO=?""",
                            (add_FIO, product, measurement, quantity, price, self.tree.set(self.tree.selection()[0], '#1')))
        self.db.con.commit()
        self.view_records()

    def view_records(self):
        self.db.cur.execute("""SELECT * FROM users""")
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.cur.fetchall()]

    def delete_records(self):
        for selection_item in self.tree.selection():
            self.db.cur.execute("""DELETE FROM users WHERE add_FIO=?""", (self.tree.set(selection_item, '#1'),))
        self.db.con.commit()
        self.view_records()

    def search_records(self, price):
        price = ("%" + price + "%",)
        self.db.cur.execute("""SELECT * FROM users WHERE price LIKE ?""", price)
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.cur.fetchall()]

    # def search_records(self, score):
    #    score = (score,)
    #    self.db.cur.execute("""SELECT * FROM users WHERE score>?""", score)
    #    [self.tree.delete(i) for i in self.tree.get_children()]
    #    [self.tree.insert('', 'end', values=row) for row in self.db.cur.fetchall()]


    def open_dialog(self):
        Child(root, app)

    def open_update_dialog(self):
        Update()

    def open_search_dialog(self):
        Search()

class Child(tk.Toplevel):

    """Класс для дочернего окна"""

    def __init__(self, root, app):
        super().__init__(root)
        self.init_child()
        self.view = app

    def init_child(self):
        self.title('Продажи')
        self.geometry('400x220+400+300')
        self.resizable(False, False)

        label_add_FIO = tk.Label(self, text='ФИО покупателя')
        label_add_FIO.place(x=20, y=25)
        self.entry_add_FIO = ttk.Entry(self)
        self.entry_add_FIO.place(x=130, y=25)

        label_product = tk.Label(self, text='Товар')
        label_product.place(x=80, y=50)
        self.entry_product = ttk.Entry(self)
        self.entry_product.place(x=130, y=50)

        label_measurement = tk.Label(self, text='Единица измерения')
        label_measurement.place(x=6, y=75)
        self.combobox = ttk.Combobox(self, values=[u'штук (шт.)', u'килограм (кг.)', u'литров (л.)'])
        self.combobox.current(0)
        self.combobox.place(x=130, y=75)

        label_quantity = tk.Label(self, text='Количество')
        label_quantity.place(x=50, y=100)
        self.entry_quantity = ttk.Entry(self)
        self.entry_quantity.place(x=130, y=100)

        label_price = tk.Label(self, text='Стоимость')
        label_price.place(x=63, y=125)
        self.entry_price = ttk.Entry(self)
        self.entry_price.place(x=130, y=125)

        btn_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
        btn_cancel.place(x=300, y=170)

        self.btn_ok = ttk.Button(self, text='Добавить')
        self.btn_ok.place(x=220, y=170)
        self.btn_ok.bind('<Button-1>', lambda event: self.view.records(self.entry_add_FIO.get(),
                                                                       self.entry_product.get(),
                                                                       self.combobox.get(),
                                                                       self.entry_quantity.get(),
                                                                       self.entry_price.get()))

        self.grab_set()
        self.focus_set()

class Update(Child):
    def __init__(self):
        super().__init__(root, app)
        self.init_edit()
        self.view = app

    def init_edit(self):
        self.title("Редактировать запись")
        btn_edit = ttk.Button(self, text="Редактировать")
        btn_edit.place(x=205, y=170)
        btn_edit.bind('<Button-1>', lambda event: self.view.update_record(self.entry_add_FIO.get(),
                                                                          self.entry_product.get(),
                                                                          self.combobox.get(),
                                                                          self.entry_quantity.get(),
                                                                          self.entry_price.get()))
        self.btn_ok.destroy()

class Search(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.init_search()
        self.view = app

    def init_search(self):
        self.title("Поиск по стоимости")
        self.geometry("300x100+400+300")
        self.resizable(False, False)

        label_search = tk.Label(self, text="Поиск")
        label_search.place(x=50, y=20)

        self.entry_search = ttk.Entry(self)
        self.entry_search.place(x=105, y=20, width=150)

        btn_cancel = ttk.Button(self, text="Закрыть", command=self.destroy)
        btn_cancel.place(x=185, y=50)

        btn_search = ttk.Button(self, text="Поиск")
        btn_search.place(x=105, y=50)
        btn_search.bind('<Button-1>', lambda event: self.view.search_records(self.entry_search.get()))
        btn_search.bind('<Button-1>', lambda event: self.destroy(), add='+')

class DB:
    def __init__(self):

        with sq.connect('BD_PZ_16/shop.db') as self.con:
            self.cur = self.con.cursor()
            self.cur.execute("""CREATE TABLE IF NOT EXISTS users (
                add_FIO TEXT NOT NULL,
                product TEXT NOT NULL,
                measurement INTEGER NOT NULL DEFAULT 1,
                quantity INTEGER,
                price INTEGER
                )""")

    def insert_data(self, add_FIO, product, maesurement, quantity, price):
        self.cur.execute("""INSERT INTO users(add_FIO, product, measurement, quantity, price) VALUES (?, ?, ?, ?, ?)""", (add_FIO, product, maesurement, quantity, price))
        self.con.commit()

if __name__ == "__main__":
    root = tk.Tk()
    db = DB()
    app = Main(root)
    app.pack()
    root.title("ИНТЕРНЕТ-МАГАЗИН")
    root.geometry("750x450+400+300")
    root.resizable(False, False)
    root.mainloop()