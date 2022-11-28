from aiogram import types
from keyboards.default.desert import desert
from loader import dp


@dp.message_handler(text=['🍩 Desserts'])
async def dese(message: types.Message):
    await message.answer("What desert do you prefer?", reply_markup=desert)