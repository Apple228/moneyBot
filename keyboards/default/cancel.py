from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

cancel_keyboard = ReplyKeyboardMarkup(resize_keyboard=True,
                                        keyboard=[
                                        [
                                            KeyboardButton(text="отмена")
                                        ]
                                    ]

                                )
