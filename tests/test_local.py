from pathlib import Path

from bot import get_audio_file
from .types.dataset import LINK_DOWNLOAD

def teardown_function(test_save_download_file_from_YT):
    for file in Path('audio').glob('*'):
        try:
            file.unlink()
        except OSError as e:
            print(f'Error: {file} : {e.strerror}')

def test_save_download_file_from_YT():
    '''test: check download file from youtube'''
    result = get_audio_file(LINK_DOWNLOAD)
    assert Path(result).is_file() == True


