import datetime

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import message

from loader import dp, dm


@dp.message_handler()
async def money_change(message: types.Message, state: FSMContext):
    if message.text.lower() == "еда":
        await message.answer('Воду значит не пьете.')
        await state.update_data(category='еда')
    elif message.text.lower() == "транспорт":
        await message.answer('Не забывайте ходить пешком.')
        await state.update_data(category='транспорт')
    elif message.text.lower() == 'казино':
        await message.answer('Вы принимаете плохие финансовые решения.')
        await state.update_data(category='казино')
    else:
        await message.answer('Нет такой категории')
        await state.update_data(category='нет такой категории')

    await message.answer('Введите потраченную сумму')

    await state.set_state("Ввод суммы")

@dp.message_handler(state="Ввод суммы")
async def money_change_dm(message: types.Message, state: FSMContext):
    try:
        summ = int(message.text)
        data = await state.get_data()
        current_date = datetime.datetime.now()
        current_date_str = current_date.strftime('%H:%M:%S %d.%m.%y')
        dm.add_money_change(message.from_user.id, data.get('category'), summ, current_date_str)
        await message.answer('Данные обновлены')
        await state.reset_state()
    except ValueError:
        await message.answer("Было введено не целое число. Попробуйте еще раз.")
        await state.set_state("Ввод суммы")