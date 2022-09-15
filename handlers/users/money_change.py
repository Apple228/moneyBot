import datetime

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import message

from keyboards.default.cancel import cancel_keyboard
from loader import dp, dm


@dp.message_handler()
async def money_change(message: types.Message, state: FSMContext):
    if message.text.lower() == "еда🍔":
        await message.answer('Воду значит не пьете.')
        await state.update_data(category='еда🍔')

    elif message.text.lower() == "транспорт🚗" or message.text.lower() == "транспорт":
        await message.answer('Не забывайте ходить пешком.')
        await state.update_data(category='транспорт🚗')

    elif message.text.lower() == 'казино':
        await message.answer('Вы принимаете плохие финансовые решения.')
        await state.update_data(category='казино')

    elif message.text.lower() == 'продукты':
        await message.answer('Зашел в магазин за молоком, вышел со всем кроме молока.')
        await state.update_data(category='продукты')

    elif message.text.lower() == 'подарки мне🎁':
        await message.answer('Не тратьте все сразу, дождитесь распродажи в стиме.')
        await state.update_data(category='подарки мне🎁')

    elif message.text.lower() == 'подарки другим🎁':
        await message.answer('Ну хотя бы есть кому дарить, и то хорошо.')
        await state.update_data(category='подарки другим🎁')

    elif message.text.lower() == 'коммуналка💡':
        await message.answer('Экономьте электроэнергию (воду тоже)')
        await state.update_data(category='коммуналка💡')

    elif message.text.lower() == 'хобби🗿':
        await message.answer('🗿')
        await state.update_data(category='хобби🗿')

    else:
        await message.answer('Нет такой категории, поэтому сейчас добавим.')
        await state.update_data(category=message.text)

    await message.answer('Введите потраченную сумму',reply_markup=cancel_keyboard)

    await state.set_state("Ввод суммы")

@dp.message_handler(state="Ввод суммы")
async def money_change_dm(message: types.Message, state: FSMContext):
    try:
        summ = int(message.text)
        data = await state.get_data()
        current_date = datetime.datetime.now()
        current_date_str = current_date.strftime('%H:%M:%S %d.%m.%y')
        await dm.add_money_change(message.from_user.id, data.get('category'), summ, current_date_str)
        await message.answer('Данные обновлены')
        await state.reset_state()
    except ValueError:
        await message.answer("Было введено не целое число. Попробуйте еще раз.")
        await state.set_state("Ввод суммы")