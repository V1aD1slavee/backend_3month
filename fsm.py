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
    await message.answer("Сколько тебе лет?")


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())