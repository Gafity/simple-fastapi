from typing import Optional

from sqlmodel import Field, Session, SQLModel, create_engine, select

class Hero(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: Optional[str] = None
    secret_name: str
    age: Optional[int] = None


def add_heros(heros_list):
    engine = create_engine("sqlite:///data-base-hero.db")
    
    with Session(engine) as session:
        try:
            for data_hero in heros_list:
                hero = Hero(data_hero.get(name), data_hero.get(secret_name, data_hero.get(age)))
                session.add(hero)
            session.commit()
        except expression as identifier:
            print(f"Erro: {identifier}")
            session.rollback()

def show_all_heros() -> dict:
    engine = create_engine("sqlite:///data-base-hero.db")

    with Session(engine) as session:
        try:
            statement = select(Hero)
            results = session.exec(statement)
            heros = results.all()
            return dict(heros)

        except expression as identifier:
            prin(f"error na funcao show_all_heros\nErro {identifier}")
