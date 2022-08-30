from time import sleep
import unittest
import pytest
import asyncio

from pathlib import Path
from unittest.mock import AsyncMock

from bot import command_echo, get_audio_file
from bot import command_start, command_echo

class TestLocalSave(unittest.TestCase):
    '''TestClass testing local procedure '''    
    def tearDown(self):
        for file in Path('audio').glob('*'):
            try:
                file.unlink()
            except OSError as e:
                print(f'Error: {file} : {e.strerror}')

    def test_save_download_file_from_YT(self):
        '''test: check download file from youtube'''
        result = get_audio_file('https://www.youtube.com/watch?v=tDNp4mC12WE')
        self.assertEqual(True, Path(result).is_file())

class TestMessagesBot(unittest.TestCase):
    '''TestClass testing reply from bot'''

    @pytest.mark.asyncio
    async def test_reply_commands_start_and_help(self):
        '''test: testing commands start and help when sending the bot'''
        # text_reply = '"Приветствую \U0001F64B\n\n*Что умеет бот* \n\nПревращать видео в _подкасты_ или _музыку_\n\n" \
        #             + "Пришли ссылку с [Youtube](https://www.youtube.com/) и получи обратно аудиофайл который можно слушать где удобно"'
        text_reply = 'ghbdtn'
        message_mock = AsyncMock(text=text_reply)
        await command_echo(message=message_mock)
        message_mock.answer.assert_called_with(text_reply)


if __name__ == '__main__':
    unittest.main()