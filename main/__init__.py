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
SESSION = "BAA_xs68E6dRriAySynXU8VBcHoti3DrNPJgcyw1WA-7KLD62IwYfajZesBDnMPGZlsREte8hWIIa7QHVh1E3Dfqyk3QbZyhc0qnP54ADrkYffRMmZuqmbHUGZUUTfSMRuWaizlwv5W2icOxQAYxjcGVNfRgbuktIQuDZcv7SK9EXgztdxR5A-DRssCeG7qMgrx7MDfpMAVOpucVW0RAjryYXTufza9bGX4xiKeh3C0Cfjtu9OAM_8VyNfFvoB6fdqfU_a9qA4Oj_pqWNsUl1POHKimjKAeazdpLGjfcrlMgufY-8fyN9UPhTC0dgibHOUVFJT7hThOs3suJJlkyQx3fKSONTwA"
FORCESUB = "maltexade_tv"
AUTH = 690195791

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

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
