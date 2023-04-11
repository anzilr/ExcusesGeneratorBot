from pydantic import BaseModel
import traceback
from utils.inlinekeyboard import InlineKeyboardMarkup
from utils.sender import SendMessage
from utils.api import Generator
from config import START_TEXT


# Creating conversation data model
class ConversationData(BaseModel):
    state: int
    messup: str = ""
    professionalism: int = ""
    target: str = ""


# Defining conversation states

STATE_START = 0
STATE_MESSUP = 1
STATE_PROFESSIONALISM = 2
STATE_TARGET = 3

# Creating a dictionary to store conversation data
conversation_data = {}

CMD = ["/start", "/help"]
CONV_CMD = ["/excuse", "/excuses"]


async def conversation(chat_id, text):
    try:
        # Getting the current state of the conversation
        state = conversation_data.get(chat_id, ConversationData(state=STATE_START)).state

        if text in CMD:
            reply_markup = await InlineKeyboardMarkup(buttons=[
                [
                    {'text': '🗃️ Source', 'url': 'https://github.com/anzilr/ExcusesGeneratorBot'},
                    {'text': '↩️ Share Me', 'url': 't.me/share/url?url=Hi! I am 🤖 @ExcuseGenBot. I can give you 🧠 AI generated excuses for your mess-ups 😜.'}
                ]
            ])

            await SendMessage(chat_id, START_TEXT, reply_markup)

        elif text in CONV_CMD:
            # Starting the conversation by asking the reason
            await SendMessage(chat_id,
                              text="Give me a reason to generate an excuse.\n\nExample: <i>Missed the boys night</i>")
            # Storing the current state
            conversation_data[chat_id] = ConversationData(state=STATE_MESSUP)

        elif state == STATE_MESSUP:
            # Storing the reason and asking for the professionalism
            conversation_data[chat_id].messup = text
            await SendMessage(chat_id,
                              text="Ok. Now tell me how much professional the excuse should be. Pass a value between 1 - 100\n\nExample: <i>20</i>")
            conversation_data[chat_id].state = STATE_PROFESSIONALISM

        elif state == STATE_PROFESSIONALISM:
            # Storing the professionalism and asking for the target
            conversation_data[chat_id].professionalism = int(text)
            await SendMessage(chat_id, text="Name the person you make the excuse.\n\nExample: <i>Friend</i>")
            conversation_data[chat_id].state = STATE_TARGET

        elif state == STATE_TARGET:
            # Storing the target and generating response
            conversation_data[chat_id].target = text
            await SendMessage(chat_id, text="Please wait. Generating the excuse.")
            response = await Generator(
                conversation_data[chat_id].messup, conversation_data[chat_id].professionalism,
                conversation_data[chat_id].target)
            reply_markup = await InlineKeyboardMarkup(buttons=[
                [
                    {'text': '🔄 Regenerate', 'callback_data': f'{conversation_data[chat_id].messup}|{conversation_data[chat_id].professionalism}|{conversation_data[chat_id].target}'}
                ]
            ])
            await SendMessage(chat_id, response, reply_markup)
            del conversation_data[chat_id]

        else:
            await SendMessage(chat_id, text='Send "/excuse" to start')

    except Exception:
        print(traceback.format_exc())


