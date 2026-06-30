from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

class ItemModel(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    description = Column(Text, default="")
