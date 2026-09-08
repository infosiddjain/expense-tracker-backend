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

@app.post("/add-expenses")
def add_expenses(expense: Expense):
    data = {
        "title": expense.title,
        "amount": expense.amount
    }
    
    expenses.append(data)
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