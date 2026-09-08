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