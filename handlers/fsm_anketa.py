from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup

from config import bot

from keyboards.client_kb import cancel_markup

class FSMAdmin(StatesGroup):
    photo = State()
    name = State()
    surname = State()
    age = State()
    region = State()


async def fsm_start(message: types.Message):
    if message.chat.type == 'private':
        await FSMAdmin.photo.set()
        await message.answer(f"Салалекум {message.from_user.full_name}, "
                           f"скинь фотку...",
                             reply_markup=cancel_markup)
    else:
        await message.reply("Пиши в личку!")


async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['id'] = message.from_user.id
        data['username'] = f"@{message.from_user.username}"
        data['photo'] = message.photo[0].file_id
    await FSMAdmin.next()
    await message.answer("Как звать?")


async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await FSMAdmin.next()
    await message.answer("Какая фамилия??")


async def load_surname(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['surname'] = message.text
    await FSMAdmin.next()
    await message.answer("Какого года будешь ??")


async def load_age(message: types.Message, state: FSMContext):
    try:
        async with state.proxy() as data:
            data['age'] = 2022 - int(message.text)
        await FSMAdmin.next()
        await message.answer("Где живешь??")
    except:
        await message.answer("Только числа!")


async def load_region(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['region'] = message.text
        await bot.send_photo(message.from_user.id,
                             data['photo'],
                             caption=f"Name: {data['name']}\n"
                                     f"Surname: {data['surname']}\n"
                                     f"Age: {data['age']}\n"
                                     f"Region: {data['region']}\n\n"
                                     f"{data['username']}")
        print(data)

    await state.finish()
    await message.answer("Все свободен)")


async def cancel_registration(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    else:
        await state.finish()
        await message.answer("Регистрация отменена!")


def register_handler_fsmanketa(dp: Dispatcher):
    dp.register_message_handler(cancel_registration, state='*',
                                commands='cancel')
    dp.register_message_handler(cancel_registration,
                                Text(equals='cancel', ignore_case=True),
                                state='*')

    dp.register_message_handler(fsm_start, commands=['anketa'])
    dp.register_message_handler(load_photo, state=FSMAdmin.photo,
                                content_types=['photo'])
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_surname, state=FSMAdmin.surname)
    dp.register_message_handler(load_age, state=FSMAdmin.age)
    dp.register_message_handler(load_region, state=FSMAdmin.region)
