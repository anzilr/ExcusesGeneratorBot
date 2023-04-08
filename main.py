from fastapi import FastAPI, Request
from api import Generator
from config import START_TEXT, WRONG_INPUT
from message_handler import SendMessage, MessageParser

app = FastAPI()


@app.post("/")
async def index(req: Request):
    msg = await req.json()

    chat_id, text = await MessageParser(msg)
    #print(text)
    try:
        if text == "/start":
            await SendMessage(chat_id, text=START_TEXT)

        else:
            try:
                messup, professionalism, target = text.split("|")
                response = await Generator(messup, professionalism, target)
                await SendMessage(chat_id, response)

            except ValueError:
                await SendMessage(chat_id, text=WRONG_INPUT)
    except:
        pass

