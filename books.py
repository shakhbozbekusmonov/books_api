from fastapi import FastAPI

app = FastAPI()


BOOKS = [
    {"title": "FastAPI Book", "author": "Tanner Linsley", "price": 39.99},
    {"title": "FastAPI Book 2", "author": "Tanner Linsley", "price": 49.99},
    {"title": "FastAPI Book 3", "author": "Tanner Linsley", "price": 59.99},
    {"title": "FastAPI Book 4", "author": "Tanner Linsley", "price": 69.99},
    {"title": "FastAPI Book 5", "author": "Tanner Linsley", "price": 79.99},
    {"title": "FastAPI Book 6", "author": "Tanner Linsley", "price": 89.99},
]


@app.get("/books")
async def read_all_books():
    return BOOKS
