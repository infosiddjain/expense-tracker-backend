from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message":"expense tracker web site is running"}


