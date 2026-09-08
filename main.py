from fastapi import FastAPI ,HTTPException
from database import  create_table 
from schemas import Expense
from crud import create_expense , get_all_expenses ,get_expense_by_id , delete_expense , update_expense

app = FastAPI()

create_table()

@app.get("/")
def home():
    return {"message":"expense tracker web site is running"}


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
    
    expenses = get_all_expenses()
        
    return {
        "message":"Expenses fetch success",
        "expenses": expenses
    }
    
    
@app.get("/expense/{expense_id}")
def expense_one(expense_id: int):
    
    expense = get_expense_by_id(expense_id)
    
    if expense is None:
         raise HTTPException(
             status_code=404,
             detail="Expense not found"
         )
         
    return {
        "message" :"expense  found",
        "data": expense
    }
    
@app.delete("/delete-expense/{expense_id}")
def delete_expense_route(expense_id:int):
    
    deleted = delete_expense(expense_id)
    
    if deleted == 0:
        raise HTTPException(
            status_code=404,
            detail="Expense not found"
        )
    
    return {
        "message":"expense delete successfully"
    }
            
@app.put("/update-expense/{expense_id}")
def update_expense_route(expense_id: int, expense: Expense):

    updated = update_expense(
        expense_id,
        expense.title,
        expense.amount
    )

    if updated == 0:
        raise HTTPException(
            status_code=404,
            detail="Expense not found"
        )

    return {
        "message": "Expense updated successfully",
        "expense": {
            "id": expense_id,
            "title": expense.title,
            "amount": expense.amount
        }
    }