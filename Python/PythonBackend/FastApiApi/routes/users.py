from fastapi import APIRouter

from PythonBackend.FastApiApi.models import User


route =APIRouter(prefix="/users",
                 tags=["users"],
                 responses={404: {"description": "Not found"}})



# uvicorn users:users --reload


users_list=[User(id=1,name="Tilapia",surname="Madona",age=12,game_id=1500),User(id=2,name="Rawr",surname="dinosaur",age=12,game_id=1501)]


@route.get("/users_info/")
async def get_users_list()->list:

    return users_list

