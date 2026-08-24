from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn, time

app = FastAPI()

books = []

class Book(BaseModel):
    id: int
    title: str
    author: str
    publisher: str

@app.post("/book/")
def add_book(book: Book):
    books.append(book.model_dump())
    time.sleep(30)
    return books

@app.get("/books/")
def get_books():
    return books

@app.get("/book/{id}/")
def get_book(id: int):
    return books[id]

@app.put("/book/{id}/")
def update_book(id: int, book: Book):
    books[id] = book
    return books

@app.delete("/book/{id}/")
def delete_book(id: int):
    books.pop(id)
    return books

if __name__ == '__main__':
    uvicorn.run("crud:app", reload = True)