from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils import callback_data

kfc = InlineKeyboardMarkup(row_width=2)
k1 = InlineKeyboardButton("Buy ✅", callback_data='buy4')
k2 = InlineKeyboardButton("Dont buy 🚫", callback_data='dont4')
kfc.add(k1,k2)