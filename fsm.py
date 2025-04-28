from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage
import logging, asyncio
from config import token

bot = Bot(token=token)
storage = MemoryStorage
dp = Dispatcher(storage=storage)

logging.basicConfig(level=logging.INFO)

class Form(StatesGroup):
    name = State()
    age = State()
    photo = State()


@dp.message(Command('start'))
async def start(message:Message, state:FSMContext):
    await state.set_state(Form.name)
    await message.reply("Привет , как тебя зовут?")

@dp.message(Form.age)
async def age(message:Message, state:FSMContext):
    await state.update_data(name = message.text)
    await state.set_state(Form.age)
    await message.answer("Сколько тебе лет?")

@dp.message(Form.age)
async def process_age(message:Message , state:FSMContext)
    if not message.text.isdigit():
        await message.answer("Пожалуйста введите корректный возраст")
        return
    
    age = int(message.text)
    if age < 18:
        await state.clear()
        await message.answer("Извените, этот бот доступен только лицам достигшим 18 лет!")
        return
    
    await state.update_data(age = age)
    await state.set_state(Form.photo)
    await message.answer("Пожалуйста отправьте мне свою фотографию")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())