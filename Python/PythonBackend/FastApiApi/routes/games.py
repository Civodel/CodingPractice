from fastapi import APIRouter

route =APIRouter(prefix="/games",
                 tags=["games"],
                 responses={404: {"description": "Not found"}})


games=['Elden Ring','Halo']

@route.get("/122")
async def games()->str:
    return 'fghgf'

@route.get("/{game}")
async def game(game:str)->dict:
    return {"game":game}