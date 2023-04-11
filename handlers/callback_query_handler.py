from utils.api import Generator
from utils.inlinekeyboard import InlineKeyboardMarkup
from utils.sender import SendMessage


# Using CallbackQuery to regenerate result
async def CallbackQueryHandler(chat_id, data):
    messup, professionalism, target = data.split('|')
    response = await Generator(messup, professionalism, target)
    reply_markup = await InlineKeyboardMarkup(buttons=[
        [
            {'text': '🔄 Regenerate',
             'callback_data': f'{messup}|{professionalism}|{target}'}
        ]
    ])
    await SendMessage(chat_id, response, reply_markup)
