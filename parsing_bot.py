from aiogram import Bot, Dispatcher, types, F
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from bs4 import BeautifulSoup
import requests, logging, asyncio
from config import token

bot = Bot(token=token)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)

logging.basicConfig()