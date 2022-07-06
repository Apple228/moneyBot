import sqlite3

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import CommandStart
from re import compile

from aiogram.types import ReplyKeyboardRemove

from filters import IsPrivate
from keyboards.default import contact
from loader import dp, db

from data.config import users


@dp.message_handler(CommandStart(deep_link="connect_user"))
async def connect_user(message:types.Message):
    users[message.from_user.id] = message.from_user.full_name
    await message.answer("Вы подключены")

@dp.message_handler(CommandStart(deep_link=compile(r"\d\d\d")))
async def bot_start_deeplink(message: types.Message):
    await message.answer(f'Привет, ты перешел по ссылке')
    users[message.from_user.id] = message.from_user.full_name


# @dp.message_handler(CommandStart(), IsPrivate())
# async def bot_start(message: types.Message):
#     await message.answer(f'Привет {message.from_user.full_name} {message.from_user.id}')
#     await message.answer('Хотите ли вы получать ежедневное напоминание с количеством дней до конца лета?', reply_markup=menu)
#     await Test.Q1.set()

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    name = message.from_user.full_name
    try:
        db.add_user(id=message.from_user.id,name=name)
    except sqlite3.IntegrityError as err:
        print(err)
    count = db.count_users()[0]
    await message.answer(
        "\n".join(
            [
                f"Приветствую, {message.from_user.full_name}!",
                f"Ты был занесен в базу",
                f"В базе <b>{count}</b> пользователей",
            ]
        )
    )
    await message.answer('Нажмите на кнопку ниже чтобы добавить свой номер телефона.',
                         reply_markup=contact.contact_keyboard)