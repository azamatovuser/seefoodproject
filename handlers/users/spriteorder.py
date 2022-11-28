from aiogram import types
from aiogram.utils import callback_data
from handlers.users.start import g
from keyboards.default.drink import drink
from loader import dp, bot


@dp.callback_query_handler(text=['buy6'])
async def lesasfdfsazs(call: types.CallbackQuery):
    g.append('Sprite')
    await call.message.answer("✅ Successfully added!", reply_markup=drink)


@dp.callback_query_handler(text=['dont6'])
async def sasdfff(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer("Choose what you would like to", reply_markup=drink)