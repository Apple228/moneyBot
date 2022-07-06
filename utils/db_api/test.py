from sqlite import Database

def test():
    db = Database()
    # db.create_table_users()
    # db.add_user(1, "name", "number")
    # db.add_user(2, "name2", "number2")
    users = db.select_all_users()
    print(f"Все пользователи: {users}")
    user = db.select_user(number = "number2")
    print(f"Пользователь: {user}")
    db.delete_users()

test()