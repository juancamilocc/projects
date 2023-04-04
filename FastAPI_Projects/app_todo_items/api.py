from fastapi import FastAPI
from routers import todo

app = FastAPI()
app.include_router(todo.router)

@app.get("/")
async def welcome() -> dict:
    return {
        "message": "Hello, this a first example with FastAPI"
    }

