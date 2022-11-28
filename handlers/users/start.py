import sqlite3

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.mainbtn import mainbtn

from data.config import ADMINS
from loader import dp, bot, db

g = []
final = []


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    name = message.from_user.full_name
    try:
        db.add_user(id=message.from_user.id, name=name)
    except sqlite3.IntegrityError as err:
        pass
    await message.answer(f" Dear {message.from_user.full_name}!, we're glad to see you 🥪", reply_markup=mainbtn)
    count = db.count_users()[0]
    msg = f"{name} is with us now. All people - {count}"
    await bot.send_message(chat_id=ADMINS[0], text=msg)