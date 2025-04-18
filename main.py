from fastapi import FastAPI

from pydantic import BaseModel

from database import add_heros, show_all_heros

class Query_hero(BaseModel):
    name: str | None = None
    secret_name: str
    age: int | None = None


class Post_heros(BaseModel):
    name: str | None = None
    secret_name: str
    age: int | None = None

app = FastAPI()


@app.post("/add_heros")
async def root_add_heros(hero: Post_heros):
    add_heros(hero)
    return {"message": "Hero added successfully"}


@app.get("/list_heros")
async def list_heros(limit: int = 10):
    heros = show_all_heros()
    return heros

#  app.get("/super hero/")
#  async def get_parameter(parameter: Super_Heros):
    #  pass
