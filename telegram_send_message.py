''' importing os to get environment variables '''
from os import getenv
from asyncio import run
from telegram import Bot
from dotenv import load_dotenv

def send_message(message='default message'):
    ''' get a message and send it to the telegram channel '''
    load_dotenv(dotenv_path='.env', override=True)

    bot_token = getenv('TELEGRAM_BOT_TOKEN')
    channel_id = getenv('TELEGRAM_CHANNEL_ID')
    bot = Bot(token=bot_token)

    run(bot.send_message(chat_id=channel_id, text=message))
