# TO-DO: Вынести из бота русскоязыную общалку в отдельный ресурсный файл
import telebot
from yt_dlp import YoutubeDL

import config  #config for bot?

bot=telebot.TeleBot(input("Введите TOKEN бота для запуска: "))

@bot.message_handler(content_types=['text'])
def get_text_message(message):
    # given message from user and load content
    if message.text.find("https://you") != -1:
        bot.send_message(message.chat.id, "Приступаю к работе! U+1F916")
        bot.send_video(message.chat.id, get_audio_file(message.text))
    elif message.text in ['Привет', 'Hello', 'Hi', 'Здравствуйте']:
        bot.send_message(message.chat.id, "Здравствуй, юный падаван! U+1F608\nГотов помочь тебе с подкастами или музыкой\nПришли ссылку с Youtube")
    else:
        bot.send_message(message.chat.id, "Моя твоя не понимать :(")

def get_audio_file(link):
    # convert video in audio
    with YoutubeDL(config.ydl_opts) as ydl:
        return ydl.download([link])
bot.polling(non_stop=True)
