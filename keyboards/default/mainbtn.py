from aiogram.types import ReplyKeyboardMarkup

mainbtn = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
mainbtn.add("🍟 Fast-food", "🥤 Drinks", "🍩 Desserts", "🧺 Basket")