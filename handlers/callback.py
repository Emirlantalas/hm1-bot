from aiogram import types, Dispatcher
from aiogram.types import ParseMode, InlineKeyboardButton, InlineKeyboardMarkup

import random

from config import bot, dp, ADMIN

#@dp.message_handler(commands=['mem'])
async def pic(message: types.Message):
    photo = open("media/4-6.jpg", 'rb')
    await bot.send_photo(message.from_user.id, photo=photo)

#@dp.callback_query_handler(lambda call: call.data == "button_call_1")
async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_2 = InlineKeyboardButton(
        "NEXT",
        callback_data='button_call_2'
    )
    markup.add(button_call_2)

    question = 'Кто такой Benito Musalini'
    answers = [
        'канцлер', 'безумный безумец', 'диктатор', 'маршал'
    ]
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        explanation="ДУМАЙ БРО",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=markup
    )

async def quiz_3(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_3 = InlineKeyboardButton("NEXT",
                                         callback_data="button_call_3")
    markup.add(button_call_3)
    question = "поисковая система?"
    answers = ['Yahoo!', 'Go', 'King']
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=0,
        explanation="Это же легко",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
    )

async def game_callback(message: types.Message):
    if message.from_user.id != ADMIN:
        await message.reply("Ты не мой admin!")
    else:
        if message.text.lower() == "game":
            a = ['⚽', '🏀', '🎲', '🎯', '🎳', '🎰']
            await bot.send_dice(message.chat.id, emoji=random.choice(a))


def register_handlers_callback(dp: Dispatcher):
    dp.register_message_handler(pic, commands=['mem'])
    dp.register_callback_query_handler(quiz_2, lambda call: call.data == "button_call_1")
    dp.register_callback_query_handler(quiz_3, lambda call: call.data == "button_call_2")
    dp.register_message_handler(game_callback)
