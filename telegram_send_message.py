from os import get_env
from asyncio import run
from telegram import Bot
''' import telegram library for sending status message to the telegram channel '''
from dotenv import load_dotenv

def send_message(message='default message'):
    ''' get a message and send it to the telegram channel '''
    load_dotenv(dotenv_path='.env', override=True)

    bot_token = getenv('TELEGRAM_BOT_TOKEN')
    channel_id = getenv('TELEGRAM_CHANNEL_ID')
    bot = Bot(token=bot_token)

    run(bot.send_message(chat_id=channel_id, text=message))
