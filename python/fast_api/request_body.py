import uvicorn
from fastapi import FastAPI
from typing import List
from pydantic import BaseModel, Field

app = FastAPI()

class Student(BaseModel):
    id: int
    name: str = Field(None, title = "Name of the Student", max_length = 10)
    subjects: List[str] = []

@app.post("/students/")
async def student_data(s: Student):
    return s

if __name__ == "__main__":
    uvicorn.run("request_body:app", reload = True)