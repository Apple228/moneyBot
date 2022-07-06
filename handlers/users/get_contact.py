from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import ReplyKeyboardRemove

from keyboards.default import contact
from loader import dp, db


@dp.message_handler(Command("contact"))
async def share_number(message: types.Message):
    await message.answer(f"Здравствуйте, {message.from_user.full_name}.\n"
                         f"Для того, чтобы вам перезвонили введите свой номер телефона"
                         f"нажав на кнопку ниже", reply_markup=contact.contact_keyboard)

@dp.message_handler(content_types=types.ContentType.CONTACT)
async def get_contact(message: types.Message):
    contact = message.contact
    await message.answer(f"Спасибо за ваш номер, {contact.full_name}.\n"
                         f"Ваш номер: {contact.phone_number}.\n"
                         f"Ожидайте", reply_markup=ReplyKeyboardRemove())
    db.update_user_number(contact.phone_number,contact.user_id)