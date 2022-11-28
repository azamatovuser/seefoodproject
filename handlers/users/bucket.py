from aiogram import types
from aiogram.types import ReplyKeyboardRemove
from keyboards.default.bucketbtn import bucketbtn
from handlers.users.start import g
from loader import dp, bot


@dp.message_handler(text=['🧺 Basket'])
async def bucket(message: types.Message):
    await message.answer("Here is the basket :)", reply_markup=ReplyKeyboardRemove())
    await message.answer(f"Your orders: {g}", reply_markup=bucketbtn)