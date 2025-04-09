from aiogram import Bot, Dispatcher, types, F
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

courses_buttons = [
    [types.KeyboardButton(text="Backend"), types.KeyboardButton(text="Frontend")],
    [types.KeyboardButton(text="Android"), types.KeyboardButton(text="UX/UI")],
    [types.KeyboardButton(text="Оставить заявку"), types.KeyboardButton(text="Назад")]
]

couses_keyboard = types.ReplyKeyboardMarkup(keyboard=courses_buttons, resize_keyboard=True)


# ReplyKeyboardMarkup – клавиатура, которая показывается вместо основной
# и не привязана ни к какому сообщению. Представляет собой шаблоны сообщений
# (варианты ответа), которые выбираются путем нажатия на готовую кнопку.

@dp.message(Command("start"))
async def start(message:Message):
    await message.answer(f"Здравствуйте {message.from_user.full_name}", reply_markup=start_keyboard)


@dp.message(F.text == "О нас")
async def about_us(message:Message):
    await message.reply("Geeks - это IT курсы в Оше , Кара-Балте, Бишкеке основанное в 2018 году")


@dp.message(F.text == "Адрес")
async def location(message:Message):
    await message.reply_location(latitude=40.51931846586533, longitude=72.80297788183063)


@dp.message(F.text == "Контакты")
async def contact(message: Message):
    await message.reply_contact(phone_number='+996505666038', first_name='Vladislav', last_name='Tropezonov')


@dp.message(F.text == "Курсы")
async def courses(message:Message):
    await message.reply("Вот наши курсы:", reply_markup=couses_keyboard)


@dp.message(F.text == "Backend")
async def backend(message:Message):
    await message.reply("Backend-разработчик\nСтань Backend-разработчиком с нуля за 5 месяцев и получи доступ к стажировке + помощь в трудоустройстве!")


@dp.message(F.text == "Frontend")
async def backend(message: Message):
    await message.reply("Frontend-разработчик\nСтань Frontend-разработчиком с нуля за 5 месяцев и получи доступ к стажировке + помощь в трудоустройстве!")


@dp.message(F.text == "Android")
async def backend(message: Message):
    await message.reply("Android-разработчик\nСтань Android-разработчиком с нуля за 7 месяцев и получи доступ к стажировке + помощь в трудоустройстве!")


@dp.message(F.text == "UX/UI")
async def backend(message: Message):
    await message.reply("UX/UI-дизайнер\nСтань UX/UI-дизайнером с нуля за 4 месяца и получи доступ к стажировке + помощь в трудоустройстве!")


@dp.message(F.text == "Назад")
async def back_to_menu(message:Message):
    await message.reply("Вы вернулись в главное меню", reply_markup=start_keyboard)

async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
