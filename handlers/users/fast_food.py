from aiogram import types
from keyboards.default.fastfood import fastfood
from loader import dp


@dp.message_handler(text=['🍟 Fast-food'])
async def fastf(message: types.Message):
    await message.answer("Choose what you would like to", reply_markup=fastfood)