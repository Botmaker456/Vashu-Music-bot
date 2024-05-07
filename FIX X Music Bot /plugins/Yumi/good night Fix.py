import re
from dotenv import load_dotenv
from pyrogram import filters
import random
from pyrogram.types import Message
from pyrogram import Client, filters
from FIXXMUSIC import app


# "/gn" command ka handler
@app.on_message(filters.command("oodnight", prefixes="g"))
def goodnight_command_handler(client: Client, message: Message):
    # Randomly decide whether to send a sticker or an emoji
    send_sticker = random.choice([True, False])

    # Send a sticker or an emoji based on the random choice
    if send_sticker:
        client.send_sticker(message.chat.id, get_random_sticker())
    else:
        client.send_message(message.chat.id, get_random_emoji())


# Function to get a random sticker
def get_random_sticker():
    stickers = [
        "https://telegra.ph/file/438c6f207a3d0736f6f82.mp4",
        "https://telegra.ph/file/42b7516aca41dbd9736a1.gif",
        "https://telegra.ph/file/c9b5bc8e18d69cb045209.mp4",
        "https://telegra.ph/file/0cb0db98045fe292ee231.mp4",
        "https://telegra.ph/file/fdf8775a9879585087e6a.gif",
    ]
    return random.choice(stickers)


# Function to get a random emoji
def get_random_emoji():
    emojis = [
        "😴",
        "😪",
        "💤",
        "🛌"
         "🫂"
         "🥺"
    ]
    return random.choice(emojis)