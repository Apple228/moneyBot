# import sqlite3
#
# class Database:
#     def __init__(self, path_to_db="users.db"):
#         self.path_to_db = path_to_db
#
#     @property
#     def connection(self):
#         return sqlite3.connect(self.path_to_db)
#
#     def execute(self, sql: str, parameters: tuple=None, fetchone=False, fetchall=False, commit=False):
#         if not parameters:
#             parameters = ()
#         connection = self.connection
#         connection.set_trace_callback(logger)
#         cursor = connection.cursor()
#         data = None
#         cursor.execute(sql, parameters)
#
#         if commit:
#             connection.commit()
#         if fetchall:
#             data = cursor.fetchall()
#         if fetchone:
#             data = cursor.fetchone()
#         connection.close()
#         return data
#
#     def create_table_users(self):
#         sql = """
#         CREATE TABLE Users(
#         id int NOT NULL,
#         Name varchar(255) NOT NULL,
#         number varchar(30),
#         PRIMARY KEY(id)
#         );
#         """
#         self.execute(sql, commit=True)
#         #SQL_EXAMPLE = "INSERT INTO Users(id, name, number) VALUES(1, 'John', '88005553535')"
#
#     def add_user(self, id: int, name: str, number: str = None):
#         sql = """
#         INSERT INTO Users(id, name, number) VALUES(?,?,?)
#         """
#         self.execute(sql, parameters=(id, name, number), commit=True)
#
#     def select_all_users(self):
#         sql = """
#         SELECT * FROM Users
#         """
#         return self.execute(sql, fetchall=True)
#
#     @staticmethod
#     def format_args(sql, parameters: dict):
#         sql += " AND ".join([
#         f"{item} = ?" for item in parameters
#     ])
#         return sql, tuple(parameters.values())
#
#     def select_user(self, **kwargs):
#         #SQL_EXAMPLE = "SELECT * FROM Users where id=1 AND name='John'"
#         sql = "SELECT * FROM Users WHERE "
#         sql, parameters = self.format_args(sql, kwargs)
#         return self.execute(sql, parameters=parameters, fetchone = True)
#
#     def count_users(self):
#         return self.execute("SELECT COUNT(*) FROM Users;", fetchone=True)
#
#     def update_user_number(self, number, id):
#         #SQL_EXAMPLE = "UPDATE Users SET number=88888888888 WHERE id=12345"
#         sql = f"""
#         UPDATE Users SET number=? WHERE id=?
#         """
#         return self.execute(sql, parameters=(number, id), commit=True)
#
#     def delete_users(self):
#         self.execute("DELETE FROM Users WHERE TRUE", commit=True)
#
# def logger(statement):
#     print(f"""
# Выполняем {statement}...
# """)
#
