from aiogram import types, Dispatcher
from root import dp, bot


# @dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)


def register_handlers_other(dp: Dispatcher):
    dp.register_message_handler(echo)
