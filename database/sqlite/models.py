from database import Base
from sqlalchemy import UUID, Column, String, Integer

class Book(Base):
    __tablename__ = "books"

    id = Column(String, primary_key=True, index=True)
    title = Column(String)
    author = Column(String)
    description = Column(String)
    price = Column(Integer)
    