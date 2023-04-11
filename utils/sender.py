from config import BOT_TOKEN
import aiohttp


async def SendMessage(chat_id, text, reply_markup=None):
    url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'
    if reply_markup:
        payload = {
            'chat_id': chat_id,
            'text': text,
            'parse_mode': 'HTML',
            "reply_markup": reply_markup

        }
    else:
        payload = {
            'chat_id': chat_id,
            'text': text,
            'parse_mode': 'HTML'

        }

    async with aiohttp.ClientSession() as session:
        response = await session.post(url, json=payload)
    return response
