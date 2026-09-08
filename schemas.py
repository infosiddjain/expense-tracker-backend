from pydantic import BaseModel, Field

class Expense(BaseModel):
    title:str = Field(min_length=1)
    amount: float = Field(gt=0)