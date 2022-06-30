from aiogram.utils import executor
from create_bot import dp



async def on_startup(_):
    print('the bot is working in online')

from handlers import client, admin, other

client.register_handles_client(dp)
admin.register_handles_admin(dp)
other.register_handles_other(dp)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)