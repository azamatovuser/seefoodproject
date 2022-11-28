from aiogram import types
from keyboards.inline.roll import roll
from keyboards.inline.applecake import apple
from keyboards.inline.napoleon import napo
from loader import dp, bot


@dp.message_handler(text='Napoleon')
async def fastfdfood(message:types.Message):
    rasm = open("pict/bignap.jpg", 'rb')
    await bot.send_photo(message.chat.id, rasm, caption='Napoleon\n\nPrice: 50.000som', reply_markup=napo)


@dp.message_handler(text='Apple cake')
async def fastafood(message:types.Message):
    rasm = open("pict/cake.jpg", 'rb')
    await bot.send_photo(message.chat.id, rasm, caption='Apple cake\n\nPrice: 40.000som', reply_markup=apple)


@dp.message_handler(text='Roll')
async def fastfoosdd(message:types.Message):
    rasm = open("pict/bigrulet.jpg", 'rb')
    await bot.send_photo(message.chat.id, rasm, caption='Roll\n\nPrice: 26.000som', reply_markup=roll)