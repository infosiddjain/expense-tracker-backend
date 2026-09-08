from fastapi import FastAPI
from pydantic import BaseModel

from database import get_connection , create_table 

app = FastAPI()

class Expense(BaseModel):
    title:str
    amount: float


@app.get("/")
def home():
    return {"message":"expense tracker web site is running"}

expenses = []
id_generate = 1

@app.post("/add-expenses")
def add_expenses(expense: Expense):
    
    connection = get_connection()
    
    cursor = connection.execute("""
        INSERT INTO expenses (title, amount)
        VALUES (?, ?)
        """,
        (expense.title, expense.amount))
    
    connection.commit()
    
    expense_id = cursor.lastrowid
    
    connection.close()
    return {
        "message":"Expenses added success",
        "expenses": {
            "id": expense_id,
            "title": expense.title,
            "amount": expense.amount
        }
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
    
    for data in expenses:
        if data["id"] == expense_id:
            return {
                "message" :"Get expense data ",
                "expense": data
            }
    
    return {
        "message" :"expense not found"
    }
    
@app.delete("/delete-expense/{expense_id}")
def delete_expense(expense_id:int):
    
    for data in expenses:
        if data["id"] == expense_id:
            expenses.remove(data)
            return {
                "message":"Expense delete successfully",
                "expense":data
            }
    return {
        "message":"expense not found"
    }
            
@app.put("/update-expense/{expense_id}")
def update_expense(expense_id: int, updated_content: Expense):
    for data in expenses:
        if data["id"] == expense_id:
            data["title"] = updated_content.title
            data["amount"] = updated_content.amount
            
            return {
                "message":"update expense success",
                "data":data
            }
    return{
        "message":"no expense found"
    }