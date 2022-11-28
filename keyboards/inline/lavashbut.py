from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils import callback_data

lavas = InlineKeyboardMarkup(row_width=2)
l1 = InlineKeyboardButton("Buy ✅", callback_data='buy')
l2 = InlineKeyboardButton("Dont buy 🚫", callback_data='dont')
lavas.add(l1,l2)