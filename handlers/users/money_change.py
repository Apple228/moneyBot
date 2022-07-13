from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import message

from loader import dp, dm


@dp.message_handler()
async def money_change(message: types.Message, state: FSMContext):
    if message.text.lower() == "еда":
        await message.answer('Вы выбрали еду')
    if message.text.lower() == "транспорт":
        await message.answer('Вы выбрали транспорт')

    await message.answer('Введите потраченную сумму')

    await state.set_state("Ввод суммы")

@dp.message_handler(state="Ввод суммы")
async def money_change_dm(message: types.Message, state: FSMContext):
    await dm.add_money_change(message.text, message.from_user.id)
    await message.answer('Данные обновлены')