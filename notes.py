from aiogram import Bot, Dispatcher, types, F
from aiogram.types import Message
from aiogram.filters import Command

from config import token
import logging, sqlite3, time, asyncio

bot = Bot(token=token)
dp = Dispatcher()
logging.basicConfig(level=logging.INFO)

connect = sqlite3.connect("notes.db")
cursor = connect.cursor()

cursor.execute(
    """CREATE TABLE IF NOT EXISTS notes(
               id INT,                
               user_name VARCHAR(100),
               note TEXT
);"""
)

@dp.message(Command('start'))
async def start(message:Message):
    await message.answer(f'Привет {message.from_user.full_name}! Отправь мне заметку и я её сохраню')

@dp.message(Command('view'))
async def view_notes(message:Message):          # плейсхолдер (заместитель)
    cursor.execute("""SELECT note FROM notes WHERE id = ?""", (message.from_user.id,))
    notes = cursor.fetchall()
    if notes:
        response = '\n'.join([note[0] for note in notes])
    else:
        response = "У вас нет заметок"
    await message.answer(response)

@dp.message()
async def save_note(message:Message):
    cursor.execute(
        "INSERT INTO notes (id, user_name,note) VALUES (?, ?, ?)",
        (message.from_user.id, message.from_user.username, message.text),
    )
    connect.commit()
    await message.answer("Заметка сохранена!")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
