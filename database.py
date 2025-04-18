from typing import Optional

from sqlmodel import Field, Session, SQLModel, create_engine, select

class Hero(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: Optional[str] = None
    secret_name: str
    age: Optional[int] = None


async def add_heros(heros_list: dict):
    engine = create_engine("sqlite:///data-base-hero.db")
    
    with Session(engine) as session:
        try:
            for hero in heros_list:
                data_hero = Hero(name=hero.name, secret_name=hero.secret_name, age=hero.age)
                session.add(data_hero)
            session.commit()

        except Erro as error:
            print(f"Erro: {error}")
            session.rollback()

async def show_all_heros() -> dict:
    engine = create_engine("sqlite:///data-base-hero.db")

    with Session(engine) as session:
        try:
            statement = select(Hero)
            results = session.exec(statement)
            heros = results.all()
            return heros

        except expression as identifier:
            print(f"error na funcao show_all_heros\nErro {identifier}")
