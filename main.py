from fastapi import FastAPI

from pydantic import BaseModel

from database import add_heros, show_all_heros

class Query_hero(BaseModel):
    name: str | None = None
    secret_name: str  
    age: int | None = None


class Post_heros(BaseModel):
    name: str = | None = None
    secret_name: str 
    age: int = | None = None

app = FastAPI()

app.post("/add heros")
async def root_add_heros(hero: Post_heros):
    add_heros(hero)

app.get("/list heros")
async def list_heros(limit: int = 10):
    heros = show_all_heros()
    return {[{hero.get(name): hero.value} for hero in heros]}

#  app.get("/super hero/")
#  async def get_parameter(parameter: Super_Heros):
    #  pass
