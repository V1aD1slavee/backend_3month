from aiogram import Bot, Dispatcher, types, F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from config import token
import logging, sqlite3, time, asyncio

bot = Bot(token=token)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)
logging.basicConfig(level=logging.INFO)


connect = sqlite3.connect("task.db")
cursor = connect.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS tasks(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               user_id INT,
               task TEXT
)""")

class AddTask(StatesGroup):
    waiting_for_task = State()


@dp.message(Command('start'))
async def start(message:Message):
    await message.answer(
        f"Здравствуйте {message.from_user.full_name}! Я бот для управления задачами.\nИспользуй комманду:\n/add - что бы добавить задачу\n/view - что бы просмотреть все задачи\n/delete - что бы удалить задачу"
    )


@dp.message(Command('add'))
async def add(message:Message, state:FSMContext):
    await message.answer("Отправьте свою задачу сюда, и мы её сохраним")
    await state.set_state(AddTask.waiting_for_task)


@dp.message(AddTask.waiting_for_task)
async def add_task(message:Message, state:FSMContext):
    if message.text.startswith("/"):
        await message.answer("Вы вышли из режима добавления задачи")
        await state.clear()
        return

    cursor.execute("INSERT INTO tasks (user_id, task) VALUES (?, ?)", (message.from_user.id, message.text))
    connect.commit()
    await message.reply("Задача сохрнена")
    await state.clear


@dp.message(Command('view'))
async def view_tasks(message:Message):
    cursor.execute("SELECT task FROM tasks WHERE user_id = ?", (message.from_user.id,))
    user_tasks = cursor.fetchall()
    if user_tasks:
        response = "\n".join(task[0] for task in user_tasks)
    else:
        response = "У вас нет задач на данный момент"

    await message.answer(F"Ваши задачи:\n{response}")

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
