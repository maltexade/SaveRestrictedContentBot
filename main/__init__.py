#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 5072447
API_HASH = "0868ddd7eea45fada738581d03fbfe4c"
BOT_TOKEN = "5711820837:AAHDHYkQy8QOxBABBA1_m_Mx4LBAMmL8mvw"
SESSION = "BQBqOLTAFJKA12k6Qx5sWenbV2Q4cIF44310BV7Lqv0d6nKqG-CWUKK7
FORCESUB = "maltexade_tv"
AUTH = 690195791

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client(
    session_name=SESSION, 
    api_hash=API_HASH, 
    api_id=API_ID)

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
