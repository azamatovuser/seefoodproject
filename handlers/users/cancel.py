from aiogram import types
from keyboards.default.drink import drink
from loader import bot, dp


@dp.message_handler(text=['Cancel'])
async def canc(message: types.Message):
    await message.answer("🙅 You cancelled the order", reply_markup=drink)