from aiogram import Bot, Dispatcher, types, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage
import logging, asyncio
from config import token

bot = Bot(token=token)
storage = MemoryStorage
dp = Dispatcher(storage=storage)

logging.basicConfig(level=logging.INFO)
