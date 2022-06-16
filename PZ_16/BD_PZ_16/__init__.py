import sqlite3 as sq

with sq.connect('shop.db') as con:
    cur = con.cursor()
    #cur.execute("DROP TABLE IF EXISTS users")
    cur.execute("""CREATE TABLE IF NOT EXISTS users (
        add_FIO TEXT NOT NULL,
        product TEXT NOT NULL,
        measurement INTEGER NOT NULL DEFAULT 1,
        quantity INTEGER,
        price INTEGER
        )""")