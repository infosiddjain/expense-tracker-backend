import sqlite3

connection = sqlite3.connect("expense.db")

cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        amount REAL NOT NULL
    )
""")

connection.commit()

connection.close()

print("Data base created successfully")