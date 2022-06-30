from aiogram.utils import executor
from create_bot import dp
#from test_inline import dp
#from test import dp
#from inline import dp


from data_base import sqlite_db


async def on_startup(_):
    print('the bot is working in online')
    sqlite_db.sql_start()
from handlers import client, admin, other

admin.register_handles_admin(dp)
client.register_handles_client(dp)
other.register_handles_other(dp)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)