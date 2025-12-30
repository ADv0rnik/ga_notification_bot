import os
from dotenv import load_dotenv
from configs import ENV_PATH
from aiogram import Bot, Dispatcher



load_dotenv(ENV_PATH)
bot_token = os.getenv("BOT_TOKEN")

bot = Bot(bot_token)

