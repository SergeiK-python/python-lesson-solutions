# ассистент для ./module_14_4.py и ./module_14_5.py

import sqlite3

database_file = 'files/products.db'


def initiate_db():
    connection = sqlite3.connect(database_file)
    cursor = connection.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS Products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT,
        price INTEGER NOT NULL
    )''')
    connection.commit()
    connection.close()


def fill_db():
    connection = sqlite3.connect(database_file)
    cursor = connection.cursor()

    for i in range(1, 5):
        cursor.execute("INSERT INTO Products (title, description, price) VALUES (?, ?, ?)",
                       (f'Продукт {i}', f'Описание {i}', 100 * i))
    connection.commit()
    cursor.execute("SELECT * FROM Products")
    records = cursor.fetchall()
    connection.close()
    return records


def get_all_products():
    initiate_db()
    connection = sqlite3.connect(database_file)
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM Products")
    records = cursor.fetchall()
    connection.close()

    if len(records) == 0:
        records = fill_db()

    result = {}
    for record in records:
        id, product = record[0], record[1:]
        result[id] = product
    return result
