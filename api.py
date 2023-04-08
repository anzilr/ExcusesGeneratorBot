import aiohttp
import json

url = "https://excuses.ai/api/trpc/generate.generateExcuse?batch=1"

headers = {
    'authority': 'excuses.ai',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ml;q=0.8',
    'content-type': 'application/json',
    'cookie': '_ga=GA1.1.2095312288.1680526871; _ga_N02B1SQPHQ=GS1.1.1680526870.1.1.1680527414.0.0.0',
    'dnt': '1',
    'origin': 'https://excuses.ai',
    'referer': 'https://excuses.ai/',
    'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
}


async def Generator(messup, professionalism, target):
    professionalism = int(professionalism)
    payload = json.dumps({
        "0": {
            "json": {
                "messup": messup,
                "request": "",
                "professionalism": professionalism,
                "target": target
            }
        }
    })

    async with aiohttp.ClientSession() as session:
        async with session.post(url, headers=headers, data=payload) as resp:
            response = await resp.json()
            response = response[0]
            result = response['result']['data']['json']['generation']
            result = f'🤖 Here is an excuse to your "<b>{target}</b>" for "<b>{messup}</b>".\n\n<code>{result}</code>'
    return result
