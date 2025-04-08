from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.filters import Command
import logging, asyncio
from config import token

bot = Bot(token=token)
dp = Dispatcher()

logging.basicConfig(level=logging.INFO)

start_buttons = [
    types.KeyboardButton(text="О нас"),
    types.KeyboardButton(text="Курсы"),
    types.KeyboardButton(text="Адрес"),
    types.KeyboardButton(text="Контакты")
]

@dp.message(Command("start"))
async def start(message:Message):
    await message.answer(f"Здравствуйте {message.from_user.full_name}")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
