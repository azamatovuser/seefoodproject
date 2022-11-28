from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils import callback_data

piz = InlineKeyboardMarkup(row_width=2)
p1 = InlineKeyboardButton("Buy ✅", callback_data='buy2')
p2 = InlineKeyboardButton("Dont buy 🚫", callback_data='dont2')
piz.add(p1,p2)