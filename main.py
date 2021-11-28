from aiogram import executor
from root import dp
from data_base import sqlite_db

from handlers import client, admin, other


async def on_startup(_):
    sqlite_db.sql_start()
    print('Bot was started')



client.register_handlers_client(dp)
admin.register_handler_admin(dp)
other.register_handlers_other(dp)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
