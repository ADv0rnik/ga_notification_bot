import os
import requests
import asyncio
from dotenv import load_dotenv
from configs import ENV_PATH, BASE_URL
from aiogram import Bot, Dispatcher


load_dotenv(ENV_PATH)
bot_token = os.getenv("BOT_TOKEN")
chat_id = os.getenv("CHAT_ID")
uri = f"bot{bot_token}/sendMessage"
test_msg = "Hello!"

bot = Bot(bot_token)


def send_message_to_telegram(msg: str, parse_mode: str = "HTML") -> bool:
    payload = {
        "chat_id": chat_id,
        "text": msg,
        "parse_mode": parse_mode
    }

    try:
        response = requests.post(BASE_URL+uri, data=payload)
        if response.ok:
            return True
        return False
    except requests.RequestException:
        return False
    except Exception:
        return False


if __name__ == "__main__":
    if send_message_to_telegram(test_msg):
        print("Success")
    else:
        print("Failed")