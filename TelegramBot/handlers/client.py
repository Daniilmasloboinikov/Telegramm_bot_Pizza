from aiogram import types, Dispatcher
from creatBot import dp, bot
from keyboard import kb_client, kb_client1
from Data_base import sqliteDB

async def command_start(message : types.message):
    try:
        await bot.send_message(message.from_user.id, "Салам!", reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply("общение с ботом через ЛС https://t.me/supewizerbot")

async def SendMenu(message : types.message):
    await bot.send_message(message.from_user.id, "Секунду...", reply_markup=kb_client1)


async def commandStartTime(message : types.message):
    await bot.send_message(message.from_user.id, "ПН-ВС 24/7")

async def commandStarAddress(message : types.message):
    await bot.send_message(message.from_user.id, "Только для избранных")

@dp.message_handler(commands=["menu"])
async def PizzaMenuCommand(message : types.Message):
    await sqliteDB.sql_read(message)



def registerHandlersClient(dp : Dispatcher):
   dp.register_message_handler(command_start, commands=['start', 'help','привет'])
   dp.register_message_handler(commandStartTime, commands=['time'])
   dp.register_message_handler(commandStarAddress, commands=['address'])
   dp.register_message_handler(SendMenu, commands=['admin'])
