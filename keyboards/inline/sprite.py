from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils import callback_data

sprite = InlineKeyboardMarkup(row_width=2)
s1 = InlineKeyboardButton("Buy ✅", callback_data='buy7')
s2 = InlineKeyboardButton("Dont buy 🚫", callback_data='dont7')
sprite.add(s1,s2)