from telethon import events, Button, custom
import re, os
from Sophia.events import register
from Sophia import telethn as tbot
from Sophia import telethn as tgbot
PHOTO = "https://telegra.ph/file/24047dbb8187547305db6.jpg"
@register(pattern=("/alive"))
async def awake(event):
  PIKACHU = event.sender.first_name
  PIKACHU = "**♡ I,m Psylocke💖** \n\n"
  PIKACHU += "**♡ I'm Working Properly**\n\n"
  PIKACHU += "**♡ Psylocke : 2.0 LATEST**\n\n"
  PIKACHU += "**♡ My Master :** [Besty](t.me/besty_Braddock)\n\n"
  PIKACHU += "**♡ Telethon Version : 1.23.0**\n\n"
  BUTTON = [[Button.url("𝙎𝙐𝙋𝙋𝙊𝙍𝙏", "https://t.me/PigasusSupport"), Button.url("𝙐𝙋𝘿𝘼𝙏𝙀", "https://t.me/PigasusUpdates")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=PIKACHU,  buttons=BUTTON)
