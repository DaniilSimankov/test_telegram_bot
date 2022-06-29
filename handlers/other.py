from aiogram import types, Dispatcher
from create_bot import dp
import json, string

#@dp.message_handler()
async def search_bad_words(message : types.Message):
    if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split(' ')}\
        .intersection(set(json.load(open('bad_word.json')))):
        await message.reply('Маты запрещены')
        await message.delete()


def register_handles_other(dp: Dispatcher):
    dp.register_message_handler(search_bad_words)