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