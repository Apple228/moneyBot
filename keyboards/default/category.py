from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

category_keyboard = ReplyKeyboardMarkup(resize_keyboard=True,
                                        keyboard=[
                                            [
                                                KeyboardButton(text="транспорт🚗"),

                                                KeyboardButton(text="еда🍔"),

                                                KeyboardButton(text="хобби🗿")
                                            ],
                                            [
                                                KeyboardButton(text="коммуналка💡"),

                                                KeyboardButton(text="подарки мне🎁"),

                                                KeyboardButton(text="подарки другим🎁")
                                            ],
                                            [
                                                KeyboardButton(text="зарплата💰"),

                                                KeyboardButton(text="история⏰")
                                            ],
                                        ]

                                        )
