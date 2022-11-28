from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils import callback_data

roll = InlineKeyboardMarkup(row_width=2)
r1 = InlineKeyboardButton("Buy ✅", callback_data='buy9')
r2 = InlineKeyboardButton("Dont buy 🚫", callback_data='dont9')
roll.add(r1,r2)