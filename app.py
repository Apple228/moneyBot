from loader import db, dm
from utils.set_bot_commands import set_default_commands


async def on_startup(dp):
    import filters
    import middlewares
    # filters.setup(dp)
    # middlewares.setup(dp)

    from utils.notify_admins import on_startup_notify
    # await db.connect()
    # await dm.connect()

    try:
        print("пытаюсь создать таблицу")
        await db.create_table_users()
        print("всё норм")
    except Exception as err:
        print("что-то пошло не так, но я поймал ошибку и обработал её.")
        print(err)
    #db.delete_users()

    try:
        await dm.create_table_money()
        print('таблица создана')
    except Exception as err:
        print('случилась непредвиденная ошибка, вот она:')
        print(err)

    # print(await db.select_all_users())
    await on_startup_notify(dp)
    await set_default_commands(dp)


if __name__ == '__main__':
    from aiogram import executor
    from handlers import dp

    executor.start_polling(dp, on_startup=on_startup)