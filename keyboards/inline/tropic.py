from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils import callback_data

tropic = InlineKeyboardMarkup(row_width=2)
t1 = InlineKeyboardButton("Buy ✅", callback_data='buy6')
t2 = InlineKeyboardButton("Dont buy 🚫", callback_data='dont6')
tropic.add(t1,t2)