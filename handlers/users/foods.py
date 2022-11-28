from aiogram import types
from keyboards.inline.burgerorder import burg
from keyboards.inline.kfcord import kfc
from keyboards.inline.hotdogorder import hot
from keyboards.inline.pizzaord import piz
from keyboards.inline.lavashbut import lavas
from loader import dp, bot


@dp.message_handler(text='Lavash')
async def fastfoodg(message:types.Message):
    rasm = open("pict/big.jpg", 'rb')
    await bot.send_photo(message.chat.id, rasm, caption='Lavash\n\nPrice: 30.000som', reply_markup=lavas)


@dp.message_handler(text='Hamburger')
async def fastfoodf(message:types.Message):
    rasm = open("pict/bigburger.jpeg", 'rb')
    await bot.send_photo(message.chat.id, rasm, caption='Hamburger\n\nPrice: 28.000som', reply_markup=burg)


@dp.message_handler(text='Pizza')
async def fastfoodd(message:types.Message):
    rasm = open('pict/pitsa.jpg', 'rb')
    await bot.send_photo(message.chat.id, rasm, caption='Pizza\n\nPrice: 32.000som', reply_markup=piz)


@dp.message_handler(text='KFC')
async def fastfoods(message:types.Message):
    rasm = open("pict/kfc.jpg", 'rb')
    await bot.send_photo(message.chat.id, rasm, caption='KFC\n\nPrice: 24.000som', reply_markup=kfc)


@dp.message_handler(text='Hot-dog')
async def fastfoodas(message:types.Message):
    rasm = open("pict/charred-hot-dogs-with-spicy-mayonnaise-106466-1.jpeg", 'rb')
    await bot.send_photo(message.chat.id, rasm, caption='Hot-dog\n\nPrice: 23.000som', reply_markup=hot)