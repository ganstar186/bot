from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

btn0 = KeyboardButton('Начать')
btn1 = KeyboardButton('ЕГЭ')
btn2 = KeyboardButton('О нас')


kb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

kb_client.add(btn1).row(btn2, btn0)
