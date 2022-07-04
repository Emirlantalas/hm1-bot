from aiogram import Bot, Dispatcher
from decouple import config
from aiogram.contrib.fsm_storage.memory import MemoryStorage

stroage = MemoryStorage()

TOKEN = config("TOKEN")

bot = Bot(TOKEN)

dp = Dispatcher(bot=bot, storage=stroage)

ADMIN = 1286486288

URL ="https://pythonlol.herokuapp.com/"