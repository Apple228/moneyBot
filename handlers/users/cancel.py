from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.default.category import category_keyboard
from loader import dp


@dp.message_handler(text="отмена", state="*")
async def cancel(message: types.Message, state: FSMContext):
    await message.answer("Отменено", reply_markup=category_keyboard)
    await state.reset_state()