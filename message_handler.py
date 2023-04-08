from config import BOT_TOKEN
import aiohttp


async def SendMessage(chat_id, text):
    url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'
    payload = {
        'chat_id': chat_id,
        'text': text,
        'parse_mode': 'HTML'
    }
    async with aiohttp.ClientSession() as session:
        response = await session.post(url, json=payload)
    return response


async def MessageParser(message):
    #print(message)
    chat_id = message['message']['chat']['id']
    text = message['message']['text']
    return chat_id, text