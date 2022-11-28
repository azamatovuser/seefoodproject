from aiogram import types
from aiogram.utils import callback_data
from keyboards.default.fastfood import fastfood
from handlers.users.start import g
from loader import dp, bot


@dp.callback_query_handler(text=['buy'])
async def lez(call: types.CallbackQuery):
    g.append("Lavash")
    await call.message.answer("✅ Successfully added!", reply_markup=fastfood)


@dp.callback_query_handler(text=['dont'])
async def leza(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer("Choose what you would like to", reply_markup=fastfood)