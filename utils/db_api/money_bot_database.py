import sqlite3

class MoneyDatabase:
    def __init__(self, path_to_db="money.db"):
        self.path_to_db = path_to_db

    @property
