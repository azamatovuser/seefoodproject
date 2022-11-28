from aiogram import types
from keyboards.default.mainbtn import mainbtn
from loader import bot, dp


@dp.message_handler(text=['📤 Menu'])
async def menu(message: types.Message):
    await message.answer("You came back", reply_markup=mainbtn)