from database import get_connection

def create_expense(title:str,amount:int):
    
    connection = get_connection()
    
    cursor = connection.execute(
        """
        INSERT INTO expenses (title, amount)
        VALUES (?, ?)
        """,
        (title, amount)
    )
    
    connection.commit()
    
    expense_id = cursor.lastrowid
    
    connection.close()
    
    return {
        "id":expense_id,
        "title": title,
        "amount": amount
    }
    
def get_all_expenses():
    
    connection = get_connection()
    
    rows = connection.execute(
        "SELECT * FROM expenses"
    ).fetchall()
    
    connection.close()
    
    return [dict(row) for row in rows]