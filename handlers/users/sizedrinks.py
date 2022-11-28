from aiogram import types
from keyboards.inline.cocaord import cola
from keyboards.inline.tropic import tropic
from keyboards.inline.sprite import sprite
from loader import dp


@dp.message_handler(text=['Coca-cola'])
async def colaads(message: types.Message):
    await message.answer("Do you want add this product to bucket?", reply_markup=cola)


@dp.message_handler(text=['Tropic'])
async def tropicdf(message: types.Message):
    await message.answer("Do you want add this product to bucket?", reply_markup=tropic)


@dp.message_handler(text=['Sprite'])
async def spritedf(message: types.Message):
    await message.answer("Do you want add this product to bucket?", reply_markup=sprite)