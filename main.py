from fastapi import FastAPI
from pydantic import BaseModel

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
    global id_generate
    
    data = {
        "id": id_generate,
        "title": expense.title,
        "amount": expense.amount
    }
    
    expenses.append(data)
    id_generate += 1
    return {
        "message":"Expenses added success",
        "expenses":data
    }
    
@app.get("/list-expenses")
def get_expenses():
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