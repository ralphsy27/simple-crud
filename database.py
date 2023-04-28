from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import sqlalchemy

#sqlite engine instance
engine = create_engine("sqlite:///todo.db")

#declarative base
Base = sqlalchemy.orm.declarative_base()

#Create session local class for session maker
SessionLocal = sessionmaker(bind=engine, expire_on_commit=False)

