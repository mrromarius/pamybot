# 
# TODO: 
# - Сделать ассинхронность боту
# - Вынести из бота русскоязыную общалку в отдельный ресурсный файл
# - Поработать над форматом сообщений, добавить красивостей
import os
import re

import telebot
from pytube import YouTube

import config  #config for bot?


bot=telebot.TeleBot(input("Введите TOKEN бота для запуска: "))
@bot.message_handler(content_types=['text'])
def get_text_message(message):
    # given message from user and load content
    if message.text.lower() in ['/start', 'привет','hi', 'hello']:
        bot.delete_message(message.chat.id, message.message_id)
        bot.send_message(message.chat.id, "Приветствую \U0001F64B\n\n*Что умеет бот* \n\nПревращать видео в _подкасты_ или _музыку_\n\n"
                        + "Пришли ссылку с [Youtube](https://www.youtube.com/) и получи обратно аудиофайл котрый можно слушать где удобно", 
                        parse_mode='Markdown',
                        disable_web_page_preview=True)

    elif message.text.find("https://") != -1:
        link = message.text
        bot.delete_message(message.chat.id, message.message_id)
        message_bot = bot.send_message(message.chat.id, "Ссылка получена! Приступаю к работе! \U0001F916")
        file_name = get_audio_file(message.text)
        # If the download is not possible, send an error message
        if file_name:
            bot.delete_message(message.chat.id, message_bot.message_id)
            bot.send_message(message.chat.id, "Ваш аудиофайл подготовлен, пользуйтесь:")
            bot.send_audio(message.chat.id, open(file_name, 'rb'))
            os.remove(file_name)
        else:
            bot.delete_message(message.chat.id, message_bot.message_id)
            bot.send_message(message.chat.id, "По вашей ссылке неудалось выгрузить файл \U0001F613\nПопробуйте другую ссылку")

    else:
        bot.send_message(message.chat.id, "Моя твоя не понимать \U0001F616")

def get_audio_file(link):
    # convert video in audio
    try:
        yt_obj = YouTube(link)
        filters = yt_obj.streams.filter(abr="128kbps", progressive=False, type="audio")
        # clears special simbols
        file_name = re.sub('\W+', ' ',yt_obj.title) + '.mp4'
        filters.get_audio_only().download('audio', filename=file_name)
        return 'audio/' + file_name
    except Exception as e:
        return False

if __name__ == '__main__':
    bot.polling(non_stop=True)


