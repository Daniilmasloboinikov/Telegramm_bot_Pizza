from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

b1 = KeyboardButton("/time")
b2 = KeyboardButton("/address")
b3 = KeyboardButton("/привет")
b4 = KeyboardButton("Поделиться номером", request_contact=True)
b5 = KeyboardButton("Скажи где ты", request_location=True)
b6 = KeyboardButton("/download")
b7 = KeyboardButton("/cancel")

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)
kb_client1 = ReplyKeyboardMarkup(resize_keyboard=True)

kb_client.add(b1).add(b2,b3).row(b4,b5)
kb_client1.add(b6).add(b7)