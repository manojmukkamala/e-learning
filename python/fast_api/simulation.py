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

if __name__ == '__main__':
    uvicorn.run("crud:app", reload = True)