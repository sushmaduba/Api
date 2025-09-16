from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class MainModel(BaseModel):
    a: int
    b: int
    operation: str

def addition(a,b):
    return a+b

def substraction(a,b):
    return a-b

def multiplication(a,b):
    return a*b

def division(a,b):
    return a/b

@app.post('/calculator')
def calculator(model: MainModel):
    if model.operation == "add":
        return addition(model.a, model.b)
    elif model.operation == "substract":
        return substraction(model.a, model.b)
    elif model.operation == "multiply":
        return multiplication(model.a, model.b)
    elif model.operation == "divide":
        return division(model.a, model.b) 
    else:
        return "incorrect operation!! (operation performed: add, substract, multiply, divide)"