from aiogram import types
from aiogram.types import message

from loader import dp


@dp.message_handler()
async def food(message: types.Message):
    if message.text.lower() == "еда":
        await message.answer('Вы выбрали еду')