import re
from pyrogram import filters
import random
from FIXXMUSIC import app


@app.on_message(filters.command(["vgn","vn","voodnight","vood Night","vashuood night"], prefixes=["/","g","G"]))
def vgoodnight_command_handler(_, message):
    sender = message.from_user.mention
    send_sticker = random.choice([True, False])
    if send_sticker:
        sticker_id = get_random_sticker()
        app.send_sticker(message.chat.id, sticker_id)
        message.reply_text(f"**Goodnight, {sender}! 𝐀𝐉𝐀𝐎 𝐉𝐈 𝐇𝐀𝐌 𝐃𝐎𝐍𝐎 𝐒𝐀𝐓𝐇 𝐌𝐀𝐘 𝐒𝐎𝐘𝐄𝐆𝐄. 🌙**")
    else:
        emoji = get_random_emoji()
        app.send_message(message.chat.id, emoji)
        message.reply_text(f"**Goodnight, {sender}! Sleep tight. {emoji}**")


def get_random_sticker():
    stickers = [
        "https://telegra.ph/file/32073cf9f49990d967bff.mp4", # Sticker 1
        "https://telegra.ph/file/61338a60856acedc1008e.jpg", # Sticker 2
        "https://telegra.ph/file/32073cf9f49990d967bff.mp4", # Sticker 3
        "https://telegra.ph/file/309910dd70a806fbac94c.jpg",
        "https://telegra.ph/file/81c49a9963246c9dfbc7a.mp4",
    ]
    return random.choice(stickers)


def get_random_emoji():
    emojis = [
        "😴",
        "😴",
        "💤",
        "🛌",
        "🛏️",
    ]
    return random.choice(emojis)
