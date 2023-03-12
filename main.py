import hashlib
import requests
from bs4 import BeautifulSoup
from aiogram import Bot, Dispatcher, types, utils
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from auth_data import token
import buttons as btn
# from youtybeSearch import inline_handler


bot = Bot(token=token)

dp = Dispatcher(bot=bot)


@dp.message_handler(commands=['start'])
async def cmd_start(call: types.Message):
    await call.answer('Text', reply_markup=btn.mainMenu)


@dp.message_handler()
async def bot_message(message: types.Message):
    if message.text == 'Anime':
        await bot.send_message(message.from_user.id, 'Выбери источники', reply_markup=btn.mainAnimeMenu)
    elif message.text == 'Movies':
        await bot.send_message(message.from_user.id, 'Выбери источники', reply_markup=btn.mainMoviesMenu)
    elif message.text == 'Series':
        await bot.send_message(message.from_user.id, 'Выбери источники', reply_markup=btn.mainSeriesMenu)
    elif message.text == 'Trail':
        await bot.send_message(message.from_user.id, 'Оснойной источник youtube', reply_markup=btn.mainTrailMenu)
    elif message.text == 'Главное меню':
        await bot.send_message(message.from_user.id, 'Главное меню', reply_markup=btn.mainMenu)
    else:
        await message.reply('Неизвестная команда')


@dp.message_handler(commands=['cancel'])
async def cmd_cancel(msg: types.Message):
    await msg.answer('Canceled', reply_markup=types.ReplyKeyboardRemove())


if __name__ == '__main__':
    executor.start_polling(dp)
