from fastapi import FastAPI, HTTPException, Depends
import asyncpg
from pydantic import BaseModel, constr
import uvicorn
from database import Base, engine, SessionLocal, Session
from sqlalchemy import Column, Integer, String
from typing import List

app = FastAPI()
def get_db():
   db = SessionLocal()
   try:
      yield db
   finally:
      db.close()


books = []

class Books(Base):
    __tablename__ = "book"

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String(50), unique=True)
    author = Column(String(50))
    publisher = Column(String(50))
    Base.metadata.create_all(bind=engine)

class Book(BaseModel):
   id: int
   title: str
   author:str
   publisher: str
   class Config:
      orm_mode = True   

@app.get('/books', response_model=List[Book])
def get_books(db: Session = Depends(get_db)):
   recs = db.query(Books).all()
   return recs

# Database connection settings
# DATABASE_URL = "postgresql://postgres:mysecretpassword@127.0.0.1/postgres"

# # Function to establish database connection
# def get_database_connection():
#     return asyncpg.connect(DATABASE_URL)

# # Endpoint to create a new book
# @app.post('/book/')
# async def create_book(book: Book):
#     try:
#         connection = await get_database_connection()
#         # Establish database connection
#         async with connection.transaction():
#             # Execute SQL query to insert new book into the database
#             query = "INSERT INTO public.books (id, title, author, publisher) VALUES ($1, $2, $3, $4) RETURNING id"
#             book_id = await connection.fetchval(query, book.id, book.title, book.author, book.publisher)
        
#         return {"message": "Book created successfully", "book_id": book_id}
    
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))

# # Endpoint to get all books
# @app.get('/books/')
# async def get_books():
#     try:
#         connection = await get_database_connection()
#         # Establish database connection
#         async with connection.transaction():
#             # Execute SQL query to fetch all books from the database
#             query = "SELECT * FROM books"
#             books = await connection.fetch(query)
        
#         return books
    
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))

if __name__ == '__main__':
    uvicorn.run("db:app", reload = True)