from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils import callback_data

hot = InlineKeyboardMarkup(row_width=2)
h1 = InlineKeyboardButton("Buy ✅", callback_data='buy3')
h2 = InlineKeyboardButton("Dont buy 🚫", callback_data='dont3')
hot.add(h1,h2)