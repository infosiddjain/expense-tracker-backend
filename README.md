## Project python how it's starting

### First make it a folder

```
- mkdir expense-tracker-api
- cd expense-tracker-api
```

### Create virtual environment

```
- python3 -m venv venv
```

### Now need to activate

```
- source venv/bin/activate
```

### And install some packages

```
- pip install fastapi uvicorn
- For check purpose use this command ( pip list )
```

### Now make it file for checking all install dependency

```
- pip freeze > [filename].txt example [requirements.txt]
```

### Now make it a file

```
- main.py

- and insert this line of code for setup

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Expense Tracker API is running!"}

```

### Start this code

```
- uvicorn main:app --reload
```
