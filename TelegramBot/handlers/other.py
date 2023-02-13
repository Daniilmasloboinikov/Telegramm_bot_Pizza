from aiogram import types, Dispatcher
import json,string
from creatBot import dp, bot

# @dp.message_handler()
async def echo_send(message : types.message):
    if message.text == "Привет":
        await message.answer("Привет")
    if message.text == "Пошел нахуй":
        await bot.send_message(message.from_user.id,"Сам иди нахуй")
    if {i.lower().translate(str.maketrans('','',string.punctuation)) for i in message.text.split(' ')}\
        .intersection(set(json.load(open('cenz.json'))))!= set():
        await message.reply("Иди нахуй, быдло")
        # await message.reply("Маты запрещены!!!")
        await message.delete()

def registerHandlersOther(dp : Dispatcher):
    dp.register_message_handler(echo_send)
