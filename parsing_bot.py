from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from bs4 import BeautifulSoup
import requests, logging, asyncio, threading, time
from config import token

bot = Bot(token=token)
dp = Dispatcher()

logging.basicConfig(level=logging.INFO)

user_threading = {}  # хранит активные потоки
stop_flags = {}  # стоп флаги

def get_news():
    url = ''
