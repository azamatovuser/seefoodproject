from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils import callback_data

apple = InlineKeyboardMarkup(row_width=2)
a1 = InlineKeyboardButton("Buy ✅", callback_data='buy10')
a2 = InlineKeyboardButton("Dont buy 🚫", callback_data='dont10')
apple.add(a1,a2)