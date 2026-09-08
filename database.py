import sqlite3

def get_connection():
    connection = sqlite3.connect("expense.db")
    connection.row_factory = sqlite3.Row
    return connection

def create_table():
    connection = get_connection()
    
    connection.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            amount REAL NOT NULL
        )
    """)
    connection.commit()
    connection.close()