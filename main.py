
import asyncio
from aiogram.utils import executor
from handlers import extra, client, admin, callback, fsm_anketa, notification, inline

from config import dp, bot, URL
import logging
from database.bot_db import sql_create
#from decouple import


async def on_startup(_):
    await bot.set_webhook(URL)
    asyncio.create_task(notification.scheduler())
    sql_create()

async def on_shutdown(dp):
    await bot.delete_webhook()

admin.register_handlers_admin(dp)
fsm_anketa.register_handler_fsmanketa(dp)
client.register_handlers_client(dp)
callback.register_handlers_callback(dp)
notification.register_handler_notification(dp)
inline.register_inline_handler(dp)


extra.register_handlers_extra(dp)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    #executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
    executor.start_webhook(
        dispatcher=dp,
        webhook_path="",
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        skip_updates=True,
        host='0.0.0.0',
        port=config("PORT", cast=int)

    )
