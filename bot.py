import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command

bot = Bot(token="7607531279:AAGkOcXC2p3KMj2ak3Ojr5lCaRjJej1nJg8")
dp = Dispatcher()

@dp.message(Command('start'))
async def start(message:Message):
    await message.answer("Hello world")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())