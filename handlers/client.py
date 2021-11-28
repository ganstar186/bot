from aiogram import types, Dispatcher

from data_base import sqlite_db
from root import dp, bot
from kb import kb_client
from aiogram.dispatcher.filters import Text

"""Создание функций обработчиков"""


# Начальная функция активации
async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, '**Добро пожаловать!**', reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply('Общение с ботом через лс')


# Обработчик "ЕГЭ"
async def ege_menu_command(message: types.Message):
    await sqlite_db.sql_read(message)
    await message.delete()


# Обработчик "О нас"
async def show_about_us(message: types.Message):
    await bot.send_message(message.from_user.id, 'Мы супер компания')
    await message.delete()


"""Регистрация функций обработчиков"""


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, Text(['/start', 'Начать']))
    dp.register_message_handler(ege_menu_command, Text(equals='ЕГЭ'))
    dp.register_message_handler(show_about_us, Text(equals=['О нас']))
