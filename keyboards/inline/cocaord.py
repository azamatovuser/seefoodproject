from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils import callback_data

cola = InlineKeyboardMarkup(row_width=2)
c1 = InlineKeyboardButton("Buy ✅", callback_data='buy5')
c2 = InlineKeyboardButton("Dont buy 🚫", callback_data='dont5')
cola.add(c1,c2)