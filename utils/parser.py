from handlers.message_handler import conversation
from handlers.callback_query_handler import CallbackQueryHandler


async def MessageParser(update):
    # Parsing the message content
    if 'message' in update:
        chat_id = update['message']['chat']['id']
        text = update['message']['text']
        await conversation(chat_id, text)
    elif 'callback_query' in update:
        chat_id = update['callback_query']['from']['id']
        data = update['callback_query']['data']
        await CallbackQueryHandler(chat_id, data)
