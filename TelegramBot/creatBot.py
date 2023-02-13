from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import os

storage = MemoryStorage()

bot = Bot(token=os.getenv('TOKEN', "5959710084:AAFHIrEAji1z5V5-WeWnCzFQPskX5DiH_tw"))
dp = Dispatcher(bot, storage=storage)