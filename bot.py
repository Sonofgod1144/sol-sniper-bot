import os
import time
import requests
from telegram import Bot

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")
USER_ID = os.getenv("USER_ID")

bot = Bot(token=BOT_TOKEN)

def send_alert(message):
    bot.send_message(chat_id=CHANNEL_ID, text=message)
    bot.send_message(chat_id=USER_ID, text=message)

def monitor_tokens():
    while True:
        # Placeholder: you’ll later add token scanner logic here
        send_alert("🚨 New token launched on Solana!")
        time.sleep(120)

if __name__ == "__main__":
    monitor_tokens()
