# TO-DO: Вынести из бота русскоязыную общалку в отдельный ресурсный файл
# TO-D0: Поработать над форматом сообщений, добавить красивостей
import os
import re

import telebot
from pytube import YouTube

import config  #config for bot?

bot=telebot.TeleBot(input("Введите TOKEN бота для запуска: "))

@bot.message_handler(content_types=['text'])
def get_text_message(message):
    # given message from user and load content
    if message.text.find("https://") != -1:
        bot.send_message(message.chat.id, "Приступаю к работе! \U0001F916")
        file_name = get_audio_file(message.text)
        bot.send_audio(message.chat.id, open(file_name, 'rb'))
        os.remove(file_name)
        
    elif message.text in ['Привет', 'Hello', 'Hi', 'Здравствуйте']:
        bot.send_message(message.chat.id, "Здравствуй! \U0001F601\nПревращаю видео в подкасты или музыку\nПришли ссылку с Youtube")
    else:
        bot.send_message(message.chat.id, "Моя твоя не понимать \U0001F616")

def get_audio_file(link):
    # convert video in audio
    try:
        yt_obj = YouTube(link)
        filters = yt_obj.streams.filter(abr="128kbps", progressive=False, type="audio")
        file_name = re.sub('\W+', ' ',yt_obj.title) + '.mp4'
        filters.get_audio_only().download('audio', filename=file_name)
        return 'audio/' + file_name
    except Exception as e:
        print(e)
bot.polling(non_stop=True)

