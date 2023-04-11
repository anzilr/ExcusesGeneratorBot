import json


# Inline Keyboard Generator
async def InlineKeyboardMarkup(buttons):
    keyboard = []
    for row in buttons:
        keyboard_row = []
        for button in row:
            if 'url' in button:
                # URL button
                keyboard_row.append({
                    'text': button['text'],
                    'url': button['url']
                })
            elif 'callback_data' in button:
                # Callback button
                keyboard_row.append({
                    'text': button['text'],
                    'callback_data': button['callback_data']
                })
            elif 'switch_inline_query' in button:
                # Switch to inline query button
                keyboard_row.append({
                    'text': button['text'],
                    'switch_inline_query': button['switch_inline_query']
                })
            elif 'switch_inline_query_current_chat' in button:
                # Switch to inline query in current chat button
                keyboard_row.append({
                    'text': button['text'],
                    'switch_inline_query_current_chat': button['switch_inline_query_current_chat']
                })
            elif 'pay' in button:
                # Pay button
                keyboard_row.append({
                    'text': button['text'],
                    'pay': True
                })
        keyboard.append(keyboard_row)
    return json.dumps({'inline_keyboard': keyboard})
