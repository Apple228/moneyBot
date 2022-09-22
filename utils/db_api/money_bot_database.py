from typing import Union
import asyncpg
from asyncpg import Pool, Connection

from data import config


class MoneyDatabase:
    def __init__(self):
        self.pool: Union[Pool, None] = None

    async def connect(self):
        self.pool = await asyncpg.create_pool(
            user=config.DB_USER,
            password=config.DB_PASS,
            host=config.DB_HOST,
            database=config.DB_NAME
        )

    async def execute(self, command, *args,
        fetch: bool=True,
        fetchval: bool=False,
        fetchrow: bool=False,
        execute: bool=False
        ):
        async with self.pool.acquire() as connection:
            connection: Connection

            async with connection.transaction():
                if fetch:
                    result = await connection.fetch(command, *args)
                elif fetchval:
                    result = await connection.fetchval(command, *args)
                elif fetchrow:
                    result = await connection.fetchrow(command, *args)
                elif execute:
                    result = await connection.execute(command, *args)
            return result
    async def create_table_money(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Accounting (
        id SERIAL PRIMARY KEY,
        telegram_id BIGINT NOT NULL,
        category VARCHAR(55),
        summ INT NOT NULL,
        datetime VARCHAR(25)
        );
        """
        await self.execute(sql, execute=True)

    async def add_money_change(self, telegram_id, category, summ, datetime):
        sql = "INSERT INTO Accounting (telegram_id, category, summ, datetime) VALUES($1,$2,$3,$4);"
        return await self.execute(sql, telegram_id, category, summ, datetime, execute=True)

    async def history(self, telegram_id):
        sql = "SELECT category, summ, datetime FROM Accounting WHERE telegram_id=$1;"
        return await self.execute(sql, telegram_id, fetch=True)