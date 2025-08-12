from fastapi import FastAPI

app = FastAPI()

BOOKS= [{"Title":"book1","Author":"Author1","Category":"Category1"},
        {"Title":"book2","Author":"Author2","Category":"Category1"},
        {"Title":"book3","Author":"Author3","Category":"Category3"},
        {"Title":"book4","Author":"Author4","Category":"Category4"},
]

@app.get("/allbooks")
async def read_aLL_books():
    #return  {"message":"This is our first fastapi try"}
    return BOOKS

@app.get("/book/{book_title}")
async def read_book(book_title:str):
    for book in BOOKS:
        if book.get('Title').casefold() == book_title.casefold():
            return book

@app.get("/books/")
async def  read_author_category(category:str):
    books_to_return =[]
    for book in BOOKS:
        if book.get('Category').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return



@app.get("/books/{book_author}/")
async def  read_author_category(category:str,book_author:str):
    books_to_return =[]
    for book in BOOKS:
        if book.get('Category').casefold() == category.casefold() and \
            book.get('Author').casefold() == book_author.casefold():
            books_to_return.append(book)
    return books_to_return
