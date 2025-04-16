from aiogram import Bot, Dispatcher, types, F
from aiogram.types import Message
from aiogram.filters import Command

from config import token
import logging, sqlite3, time, asyncio

bot = Bot(token=token)
dp = Dispatcher()
logging.basicConfig(level=logging.INFO)

connect = sqlite3.connect("task.db")
cursor = connect.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS tasks(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               user_id INT,
               task TEXT
)""")