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
        tg_id int NOT NULL,
        category varchar(255) NOT NULL,
        summ int NOT NULL
        );
        """
        self.execute(sql, commit=True)

    def add_money_change(self, tg_id: int, category: str, summ: int):
        sql = f"""
        INSERT INTO Money(tg_id, category, summ) VALUES(?,?,?)
        """

        self.execute(sql, parameters=(tg_id, category, summ), commit=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ?" for item in parameters
        ])
        return sql, tuple(parameters.values())

    def select_stats(self, **kwargs):
        sql = "SELECT * FROM Money WHERE "
        sql, parameters = self.format_args(sql, kwargs)
        return self.execute(sql, parameters=parameters, fetchone=True)