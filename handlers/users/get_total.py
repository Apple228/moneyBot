from aiogram import types
from aiogram.dispatcher.filters import Command

from loader import dp, dm


@dp.message_handler(Command('total'))
async def total_output(message: types.Message):
    total_list = dm.select_stats(tg_id=message.from_user.id)
    msg = ''
    sum_food = 0
    sum_transport = 0
    for entry in total_list:
        #msg += f"Категория: {entry[1]}\n" \
        #       f"Сумма: {entry[2]}\n"
        if entry[1] == 'еда':
            sum_food += entry[2]
        elif entry[1] == 'транспорт':
            sum_transport += entry[2]
    msg = f"Еда🍔: {sum_food}\n" \
           f"Транспорт🚗: {sum_transport}\n"
    await message.answer(msg)