from typing import Optional

from fastapi import APIRouter
from pydantic import BaseModel

route =APIRouter(prefix="/users",
                 tags=["users"],
                 responses={404: {"description": "Not found"}})



# uvicorn users:users --reload

class User(BaseModel):
    id:int
    name:str
    surname:str
    age:int
    game_id:int

users_list=[User(id=1,name="Tilapia",surname="Madona",age=12,game_id=1500),User(id=2,name="Rawr",surname="dinosaur",age=12,game_id=1501)]
@route.get("/users_info/")
async def get_users_list()->list:

    return users_list

@route.get(f"/user/{id}")
async def get_user(id:int)->dict:
    filter_user=filter(lambda user: user.id == id,users_list)
    return list(filter_user)



@route.post("/new_user/")
async def create_user(user: User):

    if type(search_user_by_game_id(user.game_id)) == User:
        return {'error':"User with the same game id already exists"}
    else:
        user.id=users_list[-1].id+1
        users_list.append(user)

    return users_list

@route.put(f"/user/{id}/")
async def update_user(user: User):
    found=False
    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index]=user
            found=True

    if found:
        return users_list
    else:
        return {'error':"User not found"}


def search_user_by_game_id(game_id:int)->Optional[User]:
    users=filter(lambda user:user.game_id == game_id, users_list)
    try:
        return list(users)[0]
    except:
        return {'error':"Non User"}