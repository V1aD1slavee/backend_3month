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


@dp.message(Command('start'))
async def start(message:Message):
    await message.answer(
        f"Здравствуйте {message.from_user.full_name}! Я бот для управления задачами.\nИспользуй комманду:\n/add - что бы добавить задачу\n/view - что бы просмотреть все задачи\n/delete - что бы удалить задачу"
    )

@dp.message(Command('add'))
async def add(message:Message):
    await message.answer("Отправьте свою задачу сюда, и мы её сохраним")


@dp.message()
async def add_task(message:Message):
    cursor.execute("INSERT INTO tasks (user_id, task) VALUES (?, ?)", (message.from_user.id, message.text))
    connect.commit()
    await message.reply("Задача сохрнена")



async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
