from aiogram.types import ReplyKeyboardMarkup, KeyboardButton#, ReplyKeyboardRemove

b1 = KeyboardButton('/mode_of_operation')
b2 = KeyboardButton('/location')
b3 = KeyboardButton('/menu')
# b4 = KeyboardButton('Поделиться номером', request_contact=True)
# b5 = KeyboardButton('Отправить где я', request_location=True)

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)#, one_time_keyboard=True)

kb_client.add(b1).add(b2).add(b3)#.row(b4, b5)