import asyncio
import aiogram
import pytest_asyncio
import os

from aiogram import Bot

@pytest_asyncio.fixture(name='bot')
async def bot_fixture():
    """Bot fixture."""
    TOKEN = os.getenv('TOKEN')
    bot = Bot(TOKEN)
    yield bot
    session = await bot.get_session()
    if session and not session.closed:
        await session.close()
        await asyncio.sleep(0.2)