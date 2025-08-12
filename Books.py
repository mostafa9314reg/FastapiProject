from fastapi import FastAPI,Body

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


@app.get("/books/by_author")
async  def read_books_by_author(Author:str):
    books_to_return = []
    for book in BOOKS :
        if book.get('Author').casefold() == Author.casefold():
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


@app.post("/books/create_book")
async def creat_new_book(new_book=Body()):
    BOOKS.append(new_book)

@app.put("/books/update_book")
async def update_book(updated_book=Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('Title').casefold() == updated_book.get('Title').casefold():
            BOOKS[i] = updated_book

@app.delete("/books/delete_book/{book_title}")
async def delete_book(book_title : str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('Title').casefold() == book_title.casefold():
            BOOKS.pop(i)
            break
