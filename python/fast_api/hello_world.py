import uvicorn
from fastapi import FastAPI, Path, Query

app = FastAPI()

@app.get("/")
async def index():
    return {"message": "Hello World!"}

# @app.get("/hello/{name}/{age}")
# async def hello(name: str = Path(..., min_length = 1, max_length = 10)
#                 , age: int = Path(..., ge = 18)
#                 , percent: float = Query(..., ge = 0, le = 100)
#                 ):
#     return {"hey": name, "age": age}

if __name__ == "__main__":
    uvicorn.run("hello_world:app", reload = True)