from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/sushma/duba")
def add(a:int,b:int):
    return a+b

print(add(2,3))

class MainModel(BaseModel):
    a: int
    b: int

def substract(a:int,b:int):
    return a-b

def multiply(a:int,b:int):
    return a*b

@app.post("/subtract")
def substract_number(model: MainModel):
    return substract(model.a, model.b)

@app.post("/multiply")
def multiply_number(model: MainModel):
    return multiply(model.a, model.b)

