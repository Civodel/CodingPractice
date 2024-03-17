from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# uvicorn users:users --reload

class User(BaseModel):
    id:int
    name:str
    surname:str
    age:int
    game_id:int

users_list=[User(id=1,name="Tilapia",surname="Madona",age=12,game_id=1500),User(id=2,name="Rawr",surname="estoker",age=12,game_id=1501)]
@app.get("/users")
async def get_users_list()->list:

    return users_list

@app.get(f"/user/{id}")
async def get_user(id:int)->dict:
    filter_user=filter(lambda user: user.id == id,users_list)
    return list(filter_user)

