from aiogram import types
from keyboards.default.drink import drink
from loader import dp


@dp.message_handler(text=['🥤 Drinks'])
async def drinkss(message: types.Message):
    await message.answer("What drink do you prefer?", reply_markup=drink)