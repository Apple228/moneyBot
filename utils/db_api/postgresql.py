from typing import Union

import asyncpg
from asyncpg import Pool, Connection

from data import config


class Database:
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
                      fetch: bool=False, #берем все
                      fetchval:bool=False, #берем одно значение
                      fetchrow: bool=False, #берем значения в 1 строке
                      execute: bool=False #не берем значения
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

    async def create_table_users(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Users (
        id SERIAL PRIMARY KEY,
        full_name VARCHAR(55) NOT NULL,
        username varchar(55) NULL,
        telegram_id BIGINT NOT NULL UNIQUE,
        phone_number VARCHAR(15)
        );
        """
        await self.execute(sql, execute=True)

    async def add_user(self, full_name, username, telegram_id):
        sql = "INSERT INTO users (full_name, username, telegram_id) VALUES($1,$2,$3) returning *;"
        return await self.execute(sql, full_name, username, telegram_id, fetchrow=True)

    async def select_all_users(self):
        sql = "SELECT * FROM users;"
        return await self.execute(sql, fetch=True)

    async def count_users(self):
        sql = "SELECT COUNT(*) FROM users;"
        return await self.execute(sql, fetchval=True)

    async def update_user_number(self, phone_number, telegram_id):
        sql = "UPDATE users SET phone_number=$1 WHERE telegram_id=$2"
        return await self.execute(sql, phone_number, telegram_id, execute=True)

    async def select_user(self, telegram_id):
        sql = "SELECT * FROM users WHERE telegram_id=$1"
        return await self.execute(sql, telegram_id, fetchrow=True)


# написать update_user_number и select_user
