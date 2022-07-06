from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

choice = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Купить грушу", callback_data='pear'),
        InlineKeyboardButton(text="Купить яблоко", callback_data='apple'),

    ]
])
pear_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='Купите груши тут', url='https://www.youtube.com/watch?v=dQw4w9WgXcQ')

    ]
])
apple_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='Купите яблоки тут', url='https://youtu.be/_ZJ7AAoDhu4')

    ]
])
