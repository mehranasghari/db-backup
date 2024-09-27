from telegram import Bot
import asyncio
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path='.env', override=True)

BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
CHANNEL_ID = os.getenv('TELEGRAM_CHANNEL_ID')
bot = Bot(token=BOT_TOKEN)

asyncio.run(bot.send_message(chat_id=CHANNEL_ID, text="Hello, this is a message from my Python app!"))
