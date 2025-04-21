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
    hero_dict = hero.dict()
    await add_heros(hero_dict)
    return {"message": "Hero added successfully"}


@app.get("/list_heros")
async def list_heros():
    heros = await  show_all_heros()
    return {"all heros": heros}

#  app.get("/super hero/")
#  async def get_parameter(parameter: Super_Heros):
    #  pass
