from aiogram import Bot, Dispatcher, types
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from db import DataBase
from config import token
import logging

bot = Bot(token=token)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)
db = DataBase('users.db')
db.create_table()

logging.basicConfig(level=logging.INFO)

class Form(StatesGroup):
    username = State()

@dp.message(CommandStart())
async def start(message:Message, state:FSMContext):
    await state.set_state(Form.username)
    await message.reply("Привет! Как тебя зовут?")

@dp.message(Form.username)
async def process_username(message:Message, state:FSMContext):
    username = message.text
    db.add_user(message.from_user.id, username)
    await state.clear()
    await message.answer(f"Приятно пзнакомиться {username}!")