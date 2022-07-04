from aiogram import types, Dispatcher
from config import dp, bot

async def echo(message: types.Message):
    bad_words = ['дурак', "плохой", 'java', 'js', 'uxui']
    for word in bad_words:
        if word in message.text.lower():
            await bot.send_message(message.chat.id,
                                   f"Не матерись {message.from_user.full_name} "
                                   f"сам ты {word}")
            await bot.delete_message(message.chat.id, message.message_id)

    if message.text.startswith('pin'):
        await bot.pin_chat_message(message.chat.id, message.message_id)

    if message.text.lower() == 'dice':
        d = await bot.send_dice(message.chat.id, emoji='🎯')
        print(d.dice.value)


def register_handlers_extra(dp: Dispatcher):
    dp.register_callback_query_handler(echo)