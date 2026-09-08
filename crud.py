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


def get_expense_by_id(expense_id:int):
    
    connection = get_connection()
    
    row = connection.execute(
        "SELECT * FROM expenses WHERE id = ?",
        (expense_id,)
    ).fetchone()
    
    connection.close()
    
    if row is None:
        return {
            "message":"expense no found"
        }
    
    return dict(row)
    
def delete_expense(expense_id: int):
    
    connection = get_connection()
    
    cursor = connection.execute(
        "DELETE FROM expenses WHERE id = ?", (expense_id,)
    )
    
    connection.commit()
    connection.close()
    
    return cursor.rowcount

def update_expense(expense_id: int, title: str, amount: float):

    connection = get_connection()

    cursor = connection.execute(
        """
        UPDATE expenses
        SET title = ?, amount = ?
        WHERE id = ?
        """,
        (title, amount, expense_id)
    )

    connection.commit()

    connection.close()

    return cursor.rowcount