from aiogram import types
from aiogram.dispatcher.filters import Command

from keyboards.default.category import category_keyboard
from loader import dp


@dp.message_handler(Command('menu'))
async def menu(message: types.Message):
    await message.answer('Вывожу меню...', reply_markup=category_keyboard)