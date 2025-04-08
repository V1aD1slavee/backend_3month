from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.filters import Command
import logging, asyncio
from config import token

bot = Bot(token=token)
dp = Dispatcher()

logging.basicConfig(level=logging.INFO)

start_buttons = [
    [types.KeyboardButton(text="О нас"), types.KeyboardButton(text="Курсы")],
    [types.KeyboardButton(text="Адрес"), types.KeyboardButton(text="Контакты")],
]

start_keyboard = types.ReplyKeyboardMarkup(keyboard=start_buttons, resize_keyboard=True)
# ReplyKeyboardMarkup – клавиатура, которая показывается вместо основной
# и не привязана ни к какому сообщению. Представляет собой шаблоны сообщений
# (варианты ответа), которые выбираются путем нажатия на готовую кнопку.

@dp.message(Command("start"))
async def start(message:Message):
    await message.answer(f"Здравствуйте {message.from_user.full_name}", reply_markup=start_keyboard)

async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
