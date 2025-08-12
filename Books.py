from fastapi import FastAPI

app = FastAPI()

BOOKS= {"Title":"book1","Author":"Author1","Category":"Category1"}


@app.get("/allbooks")
async def first_api():
    #return  {"message":"This is our first fastapi try"}
    return BOOKS
