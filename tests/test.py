import pytest

from pathlib import Path
from unittest.mock import AsyncMock

from bot import command_echo, command_start, get_audio_file

def teardown_function(test_save_download_file_from_YT):
    for file in Path('audio').glob('*'):
        try:
            file.unlink()
        except OSError as e:
            print(f'Error: {file} : {e.strerror}')

def test_save_download_file_from_YT():
    '''test: check download file from youtube'''
    result = get_audio_file('https://www.youtube.com/watch?v=tDNp4mC12WE')
    assert Path(result).is_file() == True

@pytest.mark.asyncio
async def test_reply_commands_start_and_help():
    '''test: testing commands start and help when sending the bot'''
    text_reply = '"Приветствую \U0001F64B\n\n*Что умеет бот* \n\nПревращать видео в _подкасты_ или _музыку_\n\n" \
                + "Пришли ссылку с [Youtube](https://www.youtube.com/) и получи обратно аудиофайл который можно слушать где удобно"'
    message_mock = AsyncMock(text=text_reply)
    await command_start(message=message_mock)
    message_mock.send_message.assert_called_with(text_reply)
