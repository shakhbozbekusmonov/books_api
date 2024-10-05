from fastapi import FastAPI

app = FastAPI()


BOOKS = [
    {
        "title": "FastAPI Book",
        "slug": "fastapi-book",
        "category": "Python",
        "author": "Tanner Linsley",
        "price": 39.99
    },
    {
        "title": "Go Book",
        "slug": "go-book",
        "category": "Golang",
        "author": "Tanner Linsley",
        "price": 49.99
    },
    {
        "title": "Java Book",
        "slug": "java-book",
        "category": "Java",
        "author": "Tanner Linsley",
        "price": 59.99
    },
]


@app.get("/books/")
async def read_all_books(category: str):
    if category:
        return [book for book in BOOKS if book["category"].lower() == category.lower()]
    return BOOKS


@app.get("/books/{slug}")
async def read_book_by_slug(slug: str):
    for book in BOOKS:
        if book["slug"] == slug:
            return book
