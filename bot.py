# 
# TODO: 
# [x] Сделать ассинхронность боту
# - Вынести из бота русскоязыную общалку в отдельный ресурсный файл
# - Поработать над форматом сообщений, добавить красивостей
# - Сделать настройки, хранить в системе
from importlib.resources import path
from pathlib import Path
import os
import re
import ssl #error ssl.sertificate on Macos

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from pytube import YouTube

import config  #config for bot?

#error ssl.sertificate on Macos
ssl._create_default_https_context = ssl._create_stdlib_context
bot=Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot)

@dp.message_handler()
async def command_echo(message : types.Message):
    await message.answer(message.text)

@dp.message_handler(commands=['start', 'help'])
async def command_start(message : types.Message):
    await bot.send_message(message.from_user.id, "Приветствую \U0001F64B\n\n*Что умеет бот* \n\nПревращать видео в _подкасты_ или _музыку_\n\n"
                    + "Пришли ссылку с [Youtube](https://www.youtube.com/) и получи обратно аудиофайл который можно слушать где удобно", 
                    parse_mode='Markdown',
                    disable_web_page_preview=True)
@dp.message_handler()
async def get_text_message(message: types.Message):
    # given message from user and load content
    if message.text.find("https://") != -1:
        link = message.text
        await bot.delete_message(message.chat.id, message.message_id)
        message_bot = await bot.send_message(message.chat.id, "Ссылка получена! Приступаю к работе! \U0001F916")
        file_name = get_audio_file(message.text)
        # If the download is not possible, send an error message
        if file_name:
            await bot.delete_message(message.chat.id, message_bot.message_id)
            await bot.send_message(message.chat.id, "Ваш аудиофайл подготовлен, пользуйтесь:")
            await bot.send_audio(message.chat.id, open(file_name, 'rb'))
            os.remove(file_name)
        else:
            await bot.delete_message(message.chat.id, message_bot.message_id)
            await bot.send_message(message.chat.id, "По вашей ссылке неудалось выгрузить файл \U0001F613\nПопробуйте другую ссылку")

    else:
        await bot.send_message(message.chat.id, "Моя твоя не понимать \U0001F616")


def get_audio_file(link):
    # convert video in audio
    try:
        yt_obj = YouTube(link)
        filters = yt_obj.streams.filter(abr="128kbps", progressive=False, type="audio")
        # clears special simbols
        file_name = re.sub('\W+', ' ',yt_obj.title) + '.mp4'
        file_path = Path('audio')
        filters.get_audio_only().download(file_path, filename=file_name)
        return Path(file_path, file_name)
    except Exception as e:
        return False

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

