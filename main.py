from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN
from button import key_start
import requests
from  bs4 import BeautifulSoup
from  time import sleep
import random


async def on_startup(_):
    print('Бот вышел онлайн')


bot = Bot(TOKEN)
dp =Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def mes_start(message : types.Message):
    await bot.send_message(message.from_user.id, f'Привет  {message.from_user.full_name}!!!  Я 🤖 обращайтесь ко мне и получайте свежие анекдоты' , reply_markup=key_start)

@dp.message_handler(commands=['Анекдоты'])
async def mes_start(message : types.Message):
    headers = {
        "Accept": "*/*",
        "User-Agent": "UserAgent().chrome"
    }
    url = 'https://anekdotbar.ru/top-100-2.html'
    r = requests.get(url, headers=headers)
    src = r.text

    sleep(2)
    soup = BeautifulSoup(src, 'lxml')

    text = soup.find_all(class_="tecst")

    await bot.send_message(message.from_user.id, random.choice(text).text )


executor.start_polling(dp,skip_updates=True, on_startup=on_startup)







