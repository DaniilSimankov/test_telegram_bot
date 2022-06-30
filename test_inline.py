from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.dispatcher.filters import Text
import os

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot)

answ = dict()

#кнопка ссылка
url_kb = InlineKeyboardMarkup(row_width=2)
url_button = InlineKeyboardButton(text='YT', url='https://www.youtube.com')
url_button2 = InlineKeyboardButton(text='VK', url='https://vk.com/im')
x = [InlineKeyboardButton(text='NYC', url='https://www.youtube.com/watch?v=F8MN0o6RS9o&list=WL&index=6&t=3915s&ab_channel=NomadicAmbience'),\
     InlineKeyboardButton(text='Chicago', url='https://www.youtube.com/watch?v=KXkkKm4AwBg&list=WL&index=5&ab_channel=NomadicAmbience'),\
     InlineKeyboardButton(text='YTBot', url='https://www.youtube.com/watch?v=gpCIfQUbYlY&ab_channel=PythonHubStudio')]
url_kb.add(url_button, url_button2).row(*x).insert(InlineKeyboardButton(text='YTB', url='https://www.youtube.com/watch?v=gpCIfQUbYlY&ab_channel=PythonHubStudio'))

@dp.message_handler(commands='ссылки')
async def url_command(message: types.Message):
    await message.answer('Ссылочки: ', reply_markup=url_kb)

inkb = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='Like', callback_data='like_1'),\
                                             InlineKeyboardButton(text='Dislike', callback_data='like_-1'))

@dp.message_handler(commands='test')
async def test_commands(message: types.Message):
    await message.answer('За видео про деплой бота', reply_markup=inkb)

@dp.callback_query_handler(Text(startswith='like_'))
async def www_call(callback: types.CallbackQuery):
    res = int(callback.data.split('_')[1])
    if f'{callback.from_user.id}' not in answ:
        answ[f'{callback.from_user.id}'] = res
        await callback.answer('Вы проголосовали')
    else:
        await callback.answer('Вы уже проголосовали', show_alert=True)

executor.start_polling(dp, skip_updates=True)




