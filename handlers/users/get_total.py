from aiogram import types
from aiogram.dispatcher.filters import Command

from loader import dp, dm


@dp.message_handler(Command('total'))
async def total_output(message: types.Message):
    total_list = dm.select_stats(tg_id=message.from_user.id)
    msg = ''
    sum_food = 0
    sum_transport = 0
    msg_dict = {}

    for entry in total_list:
        category = entry[1]
        value = entry[2]
        if category in msg_dict:
            msg_dict[category] += value
        else:
            msg_dict.update({category: value})

    total = 0

    for key, value in msg_dict.items():
        msg += f"{key}: {value}\n"
        total += value

    msg += f"Итог: {total}"

    await message.answer(msg)
