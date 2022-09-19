'''
Data for telegramm bot testing
'''

USER = {
    "id": 12345678,
    "is_bot": False,
    "first_name": "FirstName",
    "last_name": "LastName",
    "username": "username",
    "language_code": "ru",
}

CHAT = {
    "id": 12345678,
    "first_name": "FirstName",
    "last_name": "LastName",
    "username": "username",
    "type": "private",
}

MESSAGE = {
    "message_id": 11223,
    "from": USER,
    "chat": CHAT,
    "date": 1508709711,
    "text": "Hi, world!",
}
MESSAGE_START = {
    "message_id": 11223,
    "from": USER,
    "chat": CHAT,
    "date": 1508709711,
    "text": "Приветствую \U0001F64B\n\n*Что умеет бот* \n\nПревращать видео в _подкасты_ или _музыку_\n\n" \
            + "Пришли ссылку с [Youtube](https://www.youtube.com/) и получи обратно аудиофайл который можно слушать где удобно",
}
MESSAGE_HELP = {
    "message_id": 11223,
    "from": USER,
    "chat": CHAT,
    "date": 1508709711,
    "text": "Hi, world!",
}

LINK_DOWNLOAD = 'https://www.youtube.com/watch?v=tDNp4mC12WE'