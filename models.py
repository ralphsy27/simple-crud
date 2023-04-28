#creating database model to represent db tables

from sqlalchemy import Column, Integer, String
from database import Base

class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True)
    task = Column(String(256))

