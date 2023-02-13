from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from creatBot import dp,bot
from aiogram.dispatcher.filters import Text
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from Data_base import sqliteDB

ID = None
storage = MemoryStorage()

class FSMAdmin(StatesGroup):
    photo = State()
    name = State()
    description = State()
    price = State()


@dp.message_handler(commands=['moderator'], is_chat_admin = True)
async def makeChangesCommand(message : types.Message):
    global ID
    ID = message.from_user.id
    await bot.send_message(message.from_user.id, 'Что хозяин надо???')
    await message.delete()


@dp.message_handler(commands='download', state = None)
async def cm_start(message : types.Message):
    if message.from_user.id == ID:
        await FSMAdmin.photo.set()
        await message.reply("Загрузи фото")

@dp.message_handler(commands='cancel', state = "*")
@dp.message_handler(Text(equals='cancel', ignore_case = True), state = "*")
async def cancelHandler(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        current_state = await state.get_state()
        if current_state is None:
            return
        await state.finish()
        await message.reply('OK')


@dp.message_handler(content_types=["photo"], state = FSMAdmin.photo)
async def loadPhoto(message : types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data["photo"] = message.photo[0].file_id
        await FSMAdmin.next()
        await message.reply("Теперь введи название")

@dp.message_handler(state = FSMAdmin.name)
async def loadName(message : types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data["name"] = message.text
        await FSMAdmin.next()
        await message.reply("Введите описание")

@dp.message_handler(state = FSMAdmin.description)
async def loadDescription(message : types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data["description"] = message.text
        await FSMAdmin.next()
        await message.reply("Теперь укажи цену")

@dp.message_handler(state = FSMAdmin.price)
async def loadPrice(message : types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data["price"] = message.text
        await sqliteDB.sql_add_command(state)
        await state.finish()



# def registerHandlersAdmin(dp : Dispatcher):
#     dp.register_message_handler(cm_start, commands=['download'], state=None)
#     dp.register_message_handler(loadPhoto, content_types=["photo"], state=FSMAdmin.photo)
#     dp.register_message_handler(loadName, state=FSMAdmin.name)
#     dp.register_message_handler(loadDescription,state=FSMAdmin.description)
#     dp.register_message_handler(loadPrice, state=FSMAdmin.price)
#     dp.register_message_handler(cancelHandler,commands = ['cancel'], state="*")
#     dp.register_message_handler(cancelHandler,Text(equals='cancel', ignore_case=True), state="*")
#     dp.register_message_handler(makeChangesCommand,commands=['moderator'], is_chat_admin = True)

