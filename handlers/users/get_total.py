from aiogram import types
from aiogram.dispatcher.filters import Command

from loader import dp, dm


@dp.message_handler(Command('total'))
async def total_output(message: types.Message):
    total = dm.select_stats(624523030)
    print(total)