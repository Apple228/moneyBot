import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = str(os.getenv("BOT_TOKEN"))
admins = [
    1875756936
]

ip = os.getenv("ip")

aiogram_redis = {
    'host': ip,
}

redis = {
    'address': (ip, 6379),
    'encoding': 'utf8'
}

users = {}

memes = {
    1: 'https://i.imgflip.com/2r3rxh.jpg',
    2: 'https://i.kym-cdn.com/photos/images/facebook/001/713/926/969.png',
    3: 'https://media.makeameme.org/created/oh-boy-i-acd5acd1b4.jpg',
}
