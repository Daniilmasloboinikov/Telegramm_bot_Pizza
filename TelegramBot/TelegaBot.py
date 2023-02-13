from aiogram.utils import executor
from creatBot import dp
from Data_base import sqliteDB

async def OnStartup(_):
    print('Бот онлайн')
    sqliteDB.sql_start()


from handlers import client, admin, other

client.registerHandlersClient(dp)
other.registerHandlersOther(dp)
# admin.registerHandlersAdmin(dp)

executor.start_polling(dp, skip_updates=True, on_startup=OnStartup)

