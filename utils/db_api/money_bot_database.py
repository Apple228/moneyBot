import sqlite3

from utils.db_api.sqlite import logger

class MoneyDatabase:
    def __init__(self, path_to_db="money.db"):
        self.path_to_db = path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql: str, parameters: tuple=None, fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters = ()
        connection = self.connection
        connection.set_trace_callback(logger)
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)

        if commit:
            connection.commit()
        if fetchall:
            data = cursor.fetchall()
        if fetchone:
            data = cursor.fetchone()
        connection.close()
        return data

    def create_table_money(self):
        sql = """
        CREATE TABLE Money(
        id int NOT NULL,
        Name varchar(255) NOT NULL,
        sum int NOT NULL,
        PRIMARY KEY(id)
        );
        """
        self.execute(sql, commit=True)

    def add_money_change(self, sum: int, id: int):
        sql = f"""
        INSERT INTO Money(id, sum) VALUES(?,?)
        """

        self.execute(sql, parameters=(id, sum), commit=True)
