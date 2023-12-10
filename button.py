from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

bt1 = KeyboardButton('/Анекдоты')
key_start = ReplyKeyboardMarkup(resize_keyboard=True).add(bt1)

