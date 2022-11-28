from aiogram import types
from aiogram.utils import callback_data
from handlers.users.start import g
from keyboards.default.fastfood import fastfood
from loader import dp, bot


@dp.callback_query_handler(text=['buy3'])
async def leazs(call: types.CallbackQuery):
    g.append('Hot-dog')
    await call.message.answer("✅ Successfully added!", reply_markup=fastfood)


@dp.callback_query_handler(text=['dont3'])
async def leazdsa(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer("Choose what you would like to", reply_markup=fastfood)