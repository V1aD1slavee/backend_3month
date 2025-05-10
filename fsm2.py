from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage
import logging, asyncio
from config import token

bot = Bot(token=token)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)

logging.basicConfig(level=logging.INFO)

class Form(StatesGroup):
    name = State()
    direction = State()

@dp.message(Command('start'))
async def start(message:Message, state:FSMContext):
    await state.set_state(Form.name)
    await message.answer("Привет , как тебя зовут?")

@dp.message(Form.name)
async def direction(message:Message, state:FSMContext):
    await state.update_data(name = message.text)
    await message.reply(f"Приятно познакомиться {message.text}!")
    await state.set_state(Form.direction)
    await message.answer("На каком направлении ты учишься?")

@dp.message(Form.direction)
async def process_direction(message:Message, state:FSMContext):
    await state.update_data(direction = message.text)
    data = await state.get_data()
    name = data.get('name')
    direction = data.get('direction')
    send_to_group = f"Имя:{name}\nНаправление:{direction}"

    await bot.send_message(chat_id=-1002307634503,text=send_to_group)
    await message.answer("Ваши данные были отправлены в группу")
    await state.clear()

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
