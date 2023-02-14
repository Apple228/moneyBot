import os

from dotenv import load_dotenv

from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")
admins = env.list("ADMINS")

ip = os.getenv("ip")

# DB_USER = env.str("DB_USER")
# DB_NAME = env.str("DB_NAME")
# DB_HOST = env.str("DB_HOST")
# DB_PASS = env.str("DB_PASS")

aiogram_redis = {
    'host': ip,
}

redis = {
    'address': (ip, 6379),
    'encoding': 'utf8'
}
