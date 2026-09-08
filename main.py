from fastapi import FastAPI
from database import get_connection , create_table 
from schemas import Expense
from crud import create_expense

app = FastAPI()

@app.get("/")
def home():
    return {"message":"expense tracker web site is running"}

expenses = []
id_generate = 1

@app.post("/add-expenses")
def add_expenses(expense: Expense):
    
    new_expense = create_expense(
        expense.title,
        expense.amount
    )
    
    return {
        "message":"Expenses added success",
        "expenses": new_expense
    }
    
@app.get("/list-expenses")
def get_expenses():
    
    connection = get_connection()
    
    rows = connection.execute(
        "SELECT * FROM expenses" 
    ).fetchall()
    
    connection.close()
    
    expenses = [dict(row) for row in rows]
        
    return {
        "message":"Expenses fetch success",
        "expenses": expenses
    }
    
    
@app.get("/expense/{expense_id}")
def expense_one(expense_id: int):
    
    connection = get_connection()
    
    row = connection.execute(
        "SELECT * FROM expenses WHERE id = ?",
        (expense_id,)
    ).fetchone()
    
    connection.close()
    if row is None:
         return {
             "message":"Expense not found"
         }
         
    return {
        "message" :"expense  found",
        "data": dict(row)
    }
    
@app.delete("/delete-expense/{expense_id}")
def delete_expense(expense_id:int):
    
    connection = get_connection()
    
    cursor = connection.execute( "DELETE FROM expenses WHERE id = ?",
        (expense_id,))
    
    connection.commit()
    
    connection.close()
    
    if cursor.rowcount == 0:
        return {
            "message":"expense not found"
        }
    
    return {
        "message":"expense delete successfully"
    }
            
@app.put("/update-expense/{expense_id}")
def update_expense(expense_id: int, expense: Expense):
    
    connection = get_connection()
    
    cursor = connection.execute(
          """
        UPDATE expenses
        SET title = ?, amount = ?
        WHERE id = ?
        """,
        (expense.title, expense.amount, expense_id)
    )
    
    connection.commit()
    connection.close()
    
    if cursor.rowcount == 0:
        return {
            "message":"no expense found"
        }
    
    return{
        "message":"expense found success",
        "expense": {
             "id": expense_id,
            "title": expense.title,
            "amount": expense.amount
        }
    }