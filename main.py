from fastapi import FastAPI, Request
from message_handler import MessageParser, conversation


app = FastAPI()


@app.post('/')
async def index(req: Request):
    msg = await req.json()
    chat_id, text = await MessageParser(msg)
    await conversation(chat_id, text)


@app.get("/")
async def index_get():
    return "Nothing here!"
