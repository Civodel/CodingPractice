from typing import Union
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from routes import games


app =FastAPI()


#routers

app.include_router(games.route)
app.mount('/static', StaticFiles(directory='static'),name='static')

@app.get("/")
async def read_root()->dict:
    return {"Hello": "World"}



@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}