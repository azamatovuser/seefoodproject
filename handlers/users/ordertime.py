from aiogram import types
from aiogram.dispatcher.filters import Regexp
from handlers.users.start import g, final
from keyboards.default.mainbtn import mainbtn
from data.config import ADMINS
from loader import dp, db, bot


NUMBER = "^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$"


@dp.message_handler(text=['Clean all'])
async def cleaan(message: types.Message):
    g.clear()
    await message.answer("Successfully cleaned all products!\nNo products here", reply_markup=mainbtn)


@dp.message_handler(text=['Order'])
async def orda(message: types.Message):
    await message.answer(f"{message.from_user.full_name}, send your number 📞")


@dp.message_handler(Regexp(NUMBER))
async def num(message: types.Message):
    num = message.text
    msg = f"{message.from_user.full_name} ordered {g}. His number is {num}"
    await bot.send_message(chat_id=ADMINS[0], text=msg)
    await message.answer("Your order is aceepted, please wait untill we call you 👍", reply_markup=mainbtn)
    g.clear()