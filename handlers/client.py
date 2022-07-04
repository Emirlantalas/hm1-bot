from aiogram import types, Dispatcher
from aiogram.types import ParseMode, InlineKeyboardButton, InlineKeyboardMarkup

from config import bot
from keyboards.client_kb import start_markup
from database.bot_db import sql_command_random
from parsing import movies
from parsing import CARTOON
from parsing import anime

#@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id, f"hello my master{message.from_user.full_name}",
                           reply_markup=start_markup)

#@dp.message_handler(commands=['quiz'])
async def quiz_1(message: types.Message):

    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton(
        "NEXT",
        callback_data='button_call_1'
    )
    markup.add(button_call_1)

    question ='В какой из следующих империй не было письменности?'
    answers = [
        'ИНКОВ', 'АЦТЕКОВ', 'ЕГИПТЯН', 'РИМЛЯН'
    ]
    await bot.send_poll(
        chat_id=message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=0,
        explanation="ДУМАЙ БРО",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=markup
    )

async def show_random_user(message: types.Message):
    await sql_command_random(message)


async def parser_movies(message: types.Message):
    data = movies.parser()
    for movie in data:
        desc = movie['desc'].split(',')
        #await bot.from_user.id,
        await bot.send_message(
            message.from_user.id,
            f"{movie['title']}\n"
            f"Год: {desc[0]}\n"
            f"Город: {desc[1]}\n"
            f"Жанр: #{desc[2]}\n\n"
            f"{movie['link']}"
        )
async def parser_CARTOON_mult(message: types.Message):
    data = CARTOON.parser_2()
    for movie in data:
        desc = movie['desc'].split(',')
        #await bot.from_user.id,
        await bot.send_message(
            message.from_user.id,
            f"{movie['title']}\n"
            f"Год: {desc[0]}\n"
            f"Город: {desc[1]}\n"
            f"Жанр: #{desc[2]}\n\n"
            f"{movie['link']}"
        )
async def parser_animation(message: types.Message):
    data = anime.parser_3()
    for movie in data:
        desc = movie['desc'].split(',')
        #await bot.from_user.id,
        await bot.send_message(
            message.from_user.id,
            f"{movie['title']}\n"
            f"Год: {desc[0]}\n"
            f"Город: {desc[1]}\n"
            f"Жанр: #{desc[2]}\n\n"
            f"{movie['link']}"
        )


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start'])
    dp.register_message_handler(quiz_1, commands=['quiz'])
    dp.register_message_handler(show_random_user, commands=['random'])
    dp.register_message_handler(parser_movies, commands=['series'])
    dp.register_message_handler(parser_CARTOON_mult, commands=['mult'])
    dp.register_message_handler(parser_animation, commands=['nya'])