from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

user_db = {
    1:{"name":"Sushma", "age": 22},
    2:{"name":"Ranjan", "age": 29},
    3:{"name":"Sudhanshu", "age": 30}
}

class User(BaseModel):
    name : str
    age : int 

@app.put('/update/{user_id}')
def user_update(user_id:int,user:User):
    if user_id in user_db:
        user_db[user_id] = user.dict()
        return{"message":"User Updated successfully","user": user_db[user_id]}
    else:
        return {"message" : "User not found"}