# Домашнее задание по теме "Выбор элементов и функции в SQL запросах"

import sqlite3
import os
from pprint import pprint

if not os.path.exists('./database'):
    os.mkdir('./database')

connection = sqlite3.connect('./database/not_telegram.db')
cursor = connection.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS Users (
id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER,
    balance INTEGER NOT NULL
)
               ''')

for i in range(1, 11):
    cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)",
                   (f'User{i}', f'user{i}@gmail.com', 10 * i, 1000 * i))
connection.commit()

cursor.execute("SELECT * FROM Users")
records = cursor.fetchall()
for record in records:
    id, user = record[0], record[1:]
    if id % 2 == 1:
        cursor.execute("UPDATE Users SET balance = ? WHERE id = ?", (500, id))
connection.commit()
# pprint(records)

for record in records:
    id, user = record[0], record[1:]
    if id % 3 == 1:
        cursor.execute("DELETE FROM Users WHERE id = ?", (id,))
connection.commit()
# pprint(records)

cursor.execute("SELECT * FROM Users WHERE age <> ?", (60,))
records = cursor.fetchall()
for record in records:
    id, username, email, age, balance = record
    print(f"Имя: {username} | Почта: {email} | Возраст: {age} | Баланс: {balance}")

# end of previous module_14_1.py

cursor.execute("DELETE FROM Users WHERE id = ?", (6,))
connection.commit()

cursor.execute("SELECT COUNT(*) FROM Users")
total_users = cursor.fetchone()[0]

cursor.execute("SELECT SUM(balance) FROM Users")
all_balances = cursor.fetchone()[0]

print(all_balances / total_users)

connection.close()
