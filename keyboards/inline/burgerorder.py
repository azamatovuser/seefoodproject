from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils import callback_data

burg = InlineKeyboardMarkup(row_width=2)
b1 = InlineKeyboardButton("Buy ✅", callback_data='buy1')
b2 = InlineKeyboardButton("Dont buy 🚫", callback_data='dont1')
burg.add(b1,b2)