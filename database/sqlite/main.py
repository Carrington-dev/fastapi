from uuid import uuid4
from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel, Field
from sqlalchemy import UUID
from sqlalchemy.orm import Session
from database import engine, SessionLocal
import models

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

class Book(BaseModel):
    id: str
    title: str = Field(min_length=2, max_length=150)
    description: str = Field(min_length=2, max_length=200)
    author: str = Field(min_length=2, max_length=150)
    price: int = Field(min=2)

def get_database():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@app.get("/books")
def get_books(db: Session = Depends(get_database)):
    return db.query(models.Book).all()

@app.post("/books")
def create_book(book: Book, db: Session = Depends(get_database)):
    new_book = models.Book()
    new_book.id = str(uuid4())
    new_book.author = book.author
    new_book.title = book.title
    new_book.price = book.price
    new_book.description = book.description
    db.add(new_book)
    db.commit()
    return book

@app.put("/books/{id}")
def update_book(book: Book, id:str,  db: Session = Depends(get_database)):
    new_book = db.query(models.Book).filter(models.Book.id == id).first()
    if new_book is None:
        return HTTPException(
            detail=f"Book: {id} , does not exist",
            status_code=404
        )
    new_book.author = book.author
    new_book.title = book.title
    new_book.price = book.price
    new_book.description = book.description
    db.add(new_book)
    db.commit()
    return book

@app.delete("/books/{id}", status_code=204)
def delete_book(id:str,  db: Session = Depends(get_database)):
    new_book = models.Book()
    new_book = db.query(models.Book).filter(models.Book.id == id).first()
    if new_book is None:
        return HTTPException(
            detail=f"Book: {id} , does not exist",
            status_code=404
        )
    
    # db.delete(new_book) # also works
    db.query(models.Book).filter(models.Book.id == id).delete()
    db.commit()
     

