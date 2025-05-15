from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from bs4 import BeautifulSoup
import requests, logging, asyncio, threading, time
from config import token

bot = Bot(token=token)
dp = Dispatcher()

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)

logging.basicConfig(level=logging.INFO)

user_threads = {}  # хранит активные потоки
stop_flags = {}  # стоп флаги

def parse_loop(user_id):
    page = 1

    while not stop_flags.get(user_id, True):
        if page == 1:
            url = "https://24.kg"
        else:
            url = f"https://24.kg/page_{page}"

        try:
            response = requests.get(url=url)
            if response.status_code != 200:
                page = 1
                continue

            soup = BeautifulSoup(response.text, "lxml")
            all_news = soup.find_all('div', class_='title')

            if all_news:
                text = f"📄 Страница {page}\n\n" + "\n".join(
                    f"• {title.text.strip()}" for title in all_news
                )
                asyncio.run_coroutine_threadsafe(
                    bot.send_message(user_id, text),
                    loop
                )

            page += 1
            time.sleep(30)

        except Exception as e:
            print(f"Ошибка на странице {page}: {e}")
            time.sleep(3)
            continue

@dp.message(CommandStart())
async def start(message:Message):
    await message.answer("👋 Привет! Я новостной бот 24.kg.\n\n"
        "📰 Команды:\n"
        "/news — начать парсинг новостей\n"
        "/stop — остановить парсинг\n\n"
        "⚠️ Новости будут приходить каждые 30 секунд.\n"
        "❌ Парсинг остановится только по команде /stop.")

@dp.message(Command('news'))
async def start_parsing(message:Message):
    user_id = message.chat.id
    if user_id in user_threads:
        await message.answer("Парсинг уже запущен")
        return
    
    stop_flags[user_id] = False
    thread = threading.Thread(target=parse_loop, args=(user_id,))
    user_threads[user_id] = thread
    thread.start()
    await message.answer("Начинаю парсить все страницы сайта 24.kg...")

@dp.message(Command('stop'))
async def stop_parsing(message:Message):
    user_id = message.chat.id
    if user_id not in user_threads:
        await message.answer("Парсинг ещё не запущен")
        return

    stop_flags[user_id] = True
    user_threads[user_id].join()
    del user_threads[user_id]
    del stop_flags[user_id]
    await message.answer("🛑 Парсинг остановлен")

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    loop.run_until_complete(main())
