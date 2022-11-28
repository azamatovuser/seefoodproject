from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils import callback_data

napo = InlineKeyboardMarkup(row_width=2)
n1 = InlineKeyboardButton("Buy ✅", callback_data='buy8')
n2 = InlineKeyboardButton("Dont buy 🚫", callback_data='dont8')
napo.add(n1,n2)