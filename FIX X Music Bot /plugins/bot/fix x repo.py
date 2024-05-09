from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from FIXXMUSIC import app
from config import BOT_USERNAME
from FIXXMUSIC.utils.errors import capture_err
import httpx
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_txt = """**
♡︎ ωεℓ¢σмє ƒσя ˹𝙁𝙄𝙓 ✘ 𝙈𝙐𝙎𝙄𝘾 𝘽𝙊𝙏˼ ♡︎

 ✯ ᴀʟʟ ʀᴇᴘᴏ ᴇᴀsɪʟʏ ᴅᴇᴘʟᴏʏ ᴏɴ ʜᴇʀᴏᴋᴜ ᴡɪᴛʜᴏᴜᴛ ᴀɴʏ ᴇʀʀᴏʀ ✯

 ✯ ɴᴏ ʜᴇʀᴏᴋᴜ ʙᴀɴ ɪssᴜᴇ ✯

 ✯ ɴᴏ ɪᴅ ʙᴀɴ ɪssᴜᴇ ✯

 ✯ᴜɴʟɪᴍɪᴛᴇᴅ ᴅʏɴᴏs ✯

 ✯ ʀᴜɴ 24x7 ʟᴀɢ ғʀᴇᴇ ᴡɪᴛʜᴏᴜᴛ sᴛᴏᴘ ✯

 ✯ ɪғ ʏᴏᴜ ғᴀᴄᴇ ᴀɴʏ ᴘʀᴏʙʟᴇᴍ ᴛʜᴇɴ sᴇɴᴅ ss 𝙄𝙉 𝙈𝙔 𝙏𝙀𝙇𝙀𝙂𝙍𝘼𝙈 𝙄𝘿𝙀 - @𝙑𝙖𝙨𝙝𝙪23456
**"""


@app.on_message(filters.command("vrepo" , "vashu repo link nahi dena" , "vrepo_link"))
async def start(_, msg):
    buttons = [
        [
            InlineKeyboardButton("𝐊ɪᴅɴᴀᴘ 𝐌ᴇ 𝘽𝘼𝘽𝘼𝙔 𝙄𝙉 𝙔𝙊𝙐𝙍 𝙂𝙍𝙊𝙐𝙋 𝘼𝙉𝘿 𝘾𝙃𝘼𝙉𝙉𝙀𝙇 ❤️‍🩹🍃", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
            InlineKeyboardButton("❥︎ Gʀᴏᴜᴘ 1 💗😇", url="https://t.me/Vashu123vg"),
            InlineKeyboardButton("❥︎ Gʀᴏᴜᴘ 2 💗🍃", url="https://t.me/Vashu2345"),
        ],
        [
            InlineKeyboardButton("💗 ᴄʜᴀɴɴᴇʟ 💗", url="https://t.me/Vashu123vg"),
            InlineKeyboardButton("💗 ᴅᴘᴢ ᴄʜᴀɴɴᴇʟ 💗", url="https://t.me/Vashu123vg"),
        ],
        [
            InlineKeyboardButton("˹𝙁𝙄𝙓 ✘ 𝙈𝙐𝙎𝙄𝘾 𝘽𝙊𝙏 ˼ 💗", url=f"@FIX_X_MUSIC_BOT"),
            InlineKeyboardButton("︎˹𝙆𝙃𝙐𝙎𝙃𝙄 𝘾𝙃𝘼𝙏 𝘽𝙊𝙏 ˼ 💗", url=f"@CHAT_KHUSHI_VASHU_BF_BOT"),
        ],
        [
            InlineKeyboardButton("𝐎ᴡɴᴇʀ ♕︎", url=f"@Vashu23456"),

        ]]

    reply_markup = InlineKeyboardMarkup(buttons)

    await msg.reply_photo(
        photo="https://telegra.ph/file/3cb9195d05b7bcbf1bcf5.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )


# --------------


@app.on_message(filters.command("vrepo",  "#vrepo" 'prefixes="#"))
@capture_err
async def repo(_, message):
    async with httpx.AsyncClient() as client:
        response = await client.get("https://github.com/Vashu2456/Vashu-Music-bot")

    if response.status_code == 200:
        users = response.json()
        list_of_users = ""
        count = 1
        for user in users:
            list_of_users += f"{count}. [{user['login']}]({user['html_url']})\n"
            count += 1

        text = f"""[𝖱𝖤𝖯𝖮 𝖫𝖨𝖭𝖪](https://github.com/Vashu2456/Vashu-Music-bot) | [𝖦𝖱𝖮𝖴𝖯](https://t.me/Vashu123vg)
| 𝖢𝖮𝖭𝖳𝖱𝖨𝖡𝖴𝖳𝖮𝖱𝖲 |
----------------
{list_of_users}"""
        await app.send_message(message.chat.id, text=text, disable_web_page_preview=True)
    else:
        await app.send_message(message.chat.id, text="Failed to fetch contributors.")

        "FIXXMUSIC END CODING"