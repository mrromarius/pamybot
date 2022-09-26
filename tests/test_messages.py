from unittest.mock import AsyncMock
import pytest
from aiogram import Bot, types
import pytest_asyncio

import logging

from bot import command_start, command_echo
from .types.dataset import MESSAGE_START, MESSAGE, CHAT


# @pytest.skip
@pytest.mark.asyncio
async def test_reply_commands_start_and_help():
    '''test: testing commands start and help when sending the bot'''
    text_reply = "Приветствую \U0001F64B\n\n*Что умеет бот* \n\nПревращать видео в _подкасты_ или _музыку_\n\n" \
                + "Пришли ссылку с [Youtube](https://www.youtube.com/) и получи обратно аудиофайл который можно слушать где удобно"

    message_mock = AsyncMock(MESSAGE_START)
    message_mock.chat = CHAT
    logging.warning("Тестинфо")
    logging.warning(message_mock.chat)
    await command_start(message=message_mock)
    message_mock.send_message.assert_called_with(text_reply)

