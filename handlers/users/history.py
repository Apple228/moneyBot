from aiogram import types
from keyboards.default.history_keyboard import hist_keyboard
from loader import dp, dm
from keyboards.default.category import category_keyboard


@dp.message_handler(text="история⏰")
async def history_keyboard(message: types.Message):
    await message.answer('Какую историю вы хотите посмотреть?', reply_markup=hist_keyboard)

@dp.message_handler(text="Вся история")
async def print_all_history(message: types.Message):
    history_msg = ''
    history = await dm.history(message.from_user.id)
    for category, summ, datetime in history:
        history_msg += f"Категория: {category}. Сумма: {summ}. Дата: {datetime}.\n"
    await message.answer(history_msg, reply_markup=category_keyboard)