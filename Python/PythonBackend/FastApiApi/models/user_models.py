from pydantic import BaseModel

class User(BaseModel):
    id:int
    name:str
    surname:str
    age:int
    game_id:int
