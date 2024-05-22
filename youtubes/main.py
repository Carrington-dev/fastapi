from uuid import UUID, uuid4
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI()

class Book(BaseModel):
    id: UUID
    title: str = Field(min_length=6, max_length=100)
    author: str = Field(min_length=6, max_length=100)
    description: str = Field(min_length=6, max_length=100)
    rating: int = Field(gt=-1, lt=101)

    
BOOKS = []
@app.get("/books")
def main():
    return BOOKS

@app.post("/books")
def create_book(book: Book):
    book.id = uuid4()
    BOOKS.append(book)
    return book

@app.put("/books")
def update_book(book: Book):
    BOOKS.append(book)
    return book

@app.get("/books/{id}")
def view_book(id: UUID):
    books = [ i for i in BOOKS if i.id == id ]
    if len(books) > 0:
        return (books[0])
    return { "message": f"Book with id {id} not found", }

@app.delete("/books/{id}")
def delete_book(id: UUID):
    books = [ i for i in BOOKS if i.id == id ]
    if len(books) > 0:
        BOOKS.remove(books[0])
        return { "message": f"Book with id {id} was deleted", }
    raise HTTPException(
        detail = f"Book with id {id} not found",
        status_code = 404
    )
