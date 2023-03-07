from collections import UserList
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine(f"postgresql://king@localhost:5432/game-info", echo=False)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


class UserData(Base):
    __tablename__ = "userdata"

    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
    wins = Column(Integer)
    losses = Column(Integer)


#users = session.query(UserData)

session.add(UserData(username="king", password="swordfish", wins=0, losses=0))
session.commit()