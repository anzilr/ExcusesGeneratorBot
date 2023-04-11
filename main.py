from fastapi import FastAPI, Request
from utils.parser import MessageParser


app = FastAPI()


@app.post('/')
async def index(request: Request):
    update = await request.json()
    await MessageParser(update)


@app.get("/")
async def index_get():
    return "Nothing here!"
