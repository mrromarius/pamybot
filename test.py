import unittest
from pathlib import Path

from bot import get_audio_file

class LocalSaveTestCase(unittest.TestCase):

    def setUp(self):
        pass
    
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

if __name__ == '__main__':
    unittest.main()