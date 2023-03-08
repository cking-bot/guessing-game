from collections import UserList
from dataclasses import dataclass
from sqlite3 import dbapi2
from psycopg2 import DatabaseError
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base
import os
import dotenv

dotenv.load_dotenv("secrets.env") # load
user = os.getenv("DBUSER")
port = os.getenv("DBPORT")
host = os.getenv("DBHOST")
db = os.getenv("DBNAME")

engine = create_engine(f"postgresql://{user}@{host}:{port}/{db}", echo=False)

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


