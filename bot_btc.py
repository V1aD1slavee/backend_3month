from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, BotCommand

from config import token
import requests, time, asyncio, aioschedule, logging

bot = Bot(token=token)
dp = Dispatcher()
logging.basicConfig(level=logging.INFO)

def get_btc_price():
    url = "https://api.binance.com/api/v3/avgPrice?symbol=BTCUSDT"
    response = requests.get(url=url).json()
    price = response.get('price')
    if price:
        return f"Стоимость биткоина на {time.ctime()}, {price} долларов"
    else:
        return "Не удалось получить цену биткоина"

async def schedule():
    while monitoring:
        message = await get_btc_price()
        await bot.send_message(chat_id, message)
        await asyncio.sleep(1)

@dp.message(CommandStart())
async def start(message:Message):
    await message.answer(f"Привет, {message.from_user.full_name}")
    await message.answer("")

@dp.message(Command('btc'))
async def btc(message:Message):
    global chat_id, monitoring
    chat_id = message.chat.id
    monitoring = True