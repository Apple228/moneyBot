from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

hist_keyboard = ReplyKeyboardMarkup(resize_keyboard=True,
                                       keyboard=[
                                           [
                                               KeyboardButton(text="Вся история")

                                               # KeyboardButton(text="Игнорируйте эту кнопку это тест")
                                           ]
                                       ])