'''******************CLIENT******************'''
from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards_bottom import kb_client
from aiogram.types import ReplyKeyboardRemove


#@dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Привет, это Brooklin Pizza!\nПриятного аппетита!', reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply('Общение с ботом через ЛС, напишите ему:\n https://t.me/Pizza_ProjectBot')

#@dp.message_handler(commands=['mode_of_operation'])
async def pizza_open_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'Пн-Вс с 12:00 до 00:00')
    await message.delete()

#@dp.message_handler(commands=['location'])
async def pizza_place_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'Казань, ул. Кремлевская, 27')#, reply_markup=ReplyKeyboardRemove())
    await message.delete()

def register_handles_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(pizza_open_command, commands=['mode_of_operation'])
    dp.register_message_handler(pizza_place_command, commands=['location'])
