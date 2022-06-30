from aiogram.types import ReplyKeyboardMarkup, KeyboardButton#, ReplyKeyboardRemove

button_load = KeyboardButton('/download')
button_delete = KeyboardButton('/delete')

button_case_admin = ReplyKeyboardMarkup (resize_keyboard=True).add(button_load)\
    .add(button_delete)