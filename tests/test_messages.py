from unittest import result
import pytest
from aiogram import Bot, types

from bot import command_start
from .types.dataset import MESSAGE_START, MESSAGE
from . import FakeTelegram

@pytest.mark.asyncio
async def test_reply_commands_start_and_help(bot : Bot):
    '''test: testing commands start and help when sending the bot'''
    text_reply = "Приветствую \U0001F64B\n\n*Что умеет бот* \n\nПревращать видео в _подкасты_ или _музыку_\n\n" \
                + "Пришли ссылку с [Youtube](https://www.youtube.com/) и получи обратно аудиофайл который можно слушать где удобно"

    msg = types.Message(**MESSAGE_START)
    msg.text = text_reply

    async with FakeTelegram(message_data=MESSAGE_START):
        result = await bot.send_message(chat_id = msg.chat.id, text = msg.text)
        assert result==msg