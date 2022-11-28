from aiogram import types
from aiogram.utils import callback_data
from handlers.users.start import g
from keyboards.default.drink import drink
from loader import dp, bot


@dp.callback_query_handler(text=['buy7'])
async def lesassaaszs(call: types.CallbackQuery):
    g.append('Tropic')
    await call.message.answer("✅ Successfully added!", reply_markup=drink)


@dp.callback_query_handler(text=['dont7'])
async def sasdsdf(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer("Choose what you would like to", reply_markup=drink)