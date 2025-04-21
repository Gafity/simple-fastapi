from typing import Optional

from sqlmodel import Field, Session, SQLModel, create_engine, select

class Hero(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: Optional[str] = None
    secret_name: str
    age: Optional[int] = None


async def add_heros(hero_data: dict):
    engine = create_engine("sqlite:///data-base-hero.db")
    
    with Session(engine) as session:
        try:
            hero = Hero(**hero_data)
            session.add(hero)
            session.commit()

        except Exception as error:
            print(f"Erro: {error}")
            session.rollback()

async def show_all_heros():
    engine = create_engine("sqlite:///data-base-hero.db")

    with Session(engine) as session:
        try:
            statement = select(Hero)
            results = session.exec(statement)
            heros = results.all()
            print(heros)
            return heros

        except Exception as identifier:
            print(f"error na funcao show_all_heros\nErro {identifier}")

