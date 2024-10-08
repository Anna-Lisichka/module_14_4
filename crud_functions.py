import sqlite3

connection = sqlite3.connect('database.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Products(
id INT PRIMARY KEY,
title TEXT NOT NULL,
description TEXT,
price INT NOT NULL
);
''')

def base():
    for i in range(1, 5):
        cursor.execute("INSERT INTO Products (id, title, description, price) VALUES (?, ?, ?, ?)",
                       (i, f"Продукт: {i}", f"Описание: {i}", i*100))
    connection.commit()
base()

def get_all_products():
    cursor.execute("SELECT title, description, price FROM Products")
    list = cursor.fetchall()
    return list


connection.commit()
