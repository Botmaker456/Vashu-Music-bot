from pyrogram import Client, filters
from pyrogram.types import Message
from FIXXMUSIC import app
from config import OWNER_ID


# vc on
@app.on_message(filters.video_chat_started)
async def brah(_, msg):
    await msg.reply(
        "ᴠᴏɪᴄᴇ ᴄʜᴀᴛ sᴛᴀʀᴛᴇᴅ / 𝙃𝙀𝙇𝙇𝙊 𝘼𝙅𝘼𝙊 𝙎𝘼𝘽 𝙑𝙊𝙄𝘾𝙀 𝘾𝙃𝘼𝙏 𝙋𝙀 𝘽𝘼𝘼𝙏 𝙆𝘼𝙍𝙀𝙉𝙂𝙀 𝙋𝙇𝙀𝘼𝙎𝙀 𝘼𝙅𝘼𝙊 𝙅𝙄 𝙈𝘼𝙔 𝘼𝙆𝙀𝙇𝙄 𝙃𝙐")


# vc off
@app.on_message(filters.video_chat_ended)
async def brah2(_, msg):
    await msg.reply("**ᴠᴏɪᴄᴇ ᴄʜᴀᴛ ᴇɴᴅᴇᴅ**/ 𝐂𝐇𝐀𝐋𝐎 𝐀𝐁 𝐂𝐇𝐀𝐋𝐓𝐈 𝐇𝐔 𝐊𝐀𝐀𝐌 𝐇 𝐁𝐀𝐀𝐃 𝐌𝐄 𝐀𝐔𝐍𝐆𝐈")


# invite members on vc
@app.on_message(filters.video_chat_members_invited)
async def brah3(app: app, message: Message):
    text = f"{message.from_user.mention} ɪɴᴠɪᴛᴇᴅ "
    x = 0
    for user in message.video_chat_members_invited.users:
        try:
            text += f"[{user.first_name}](tg://user?id={user.id}) "
            x += 1
        except Exception:
            pass
    try:
        await message.reply(f"{text} 😉")
    except:
        pass


####

@app.on_message(filters.command("vashumath", prefixes="/"))
def calculate_math(client, message):
    expression = message.text.split("/math ", 1)[1]
    try:
        result = eval(expression)
        response = f"ᴛʜᴇ ʀᴇsᴜʟᴛ ɪs : {result}"
    except:
        response = "ɪɴᴠᴀʟɪᴅ ᴇxᴘʀᴇssɪᴏɴ"
    message.reply(response)


###
@app.on_message(filters.command("vleavegroup") & filters.user(OWNER_ID))
async def bot_leave(_, message):
    chat_id = message.chat.id
    text = f"sᴜᴄᴄᴇssғᴜʟʟʏ   ʟᴇғᴛ  !!."
    await message.reply_text(text)
    await app.leave_chat(chat_id=chat_id, delete=True)


####


@app.on_message(filters.command(["vspg"], ["/", "!", "."]))
async def search(event):
    msg = await event.respond("Searching...")
    async with aiohttp.ClientSession() as session:
        start = 1
        async with session.get(
                f"https://content-customsearch.googleapis.com/customsearch/v1?cx=ec8db9e1f9e41e65e&q={event.text.split()[1]}&key=AIzaSyAa8yy0GdcGPHdtD083HiGGx_S0vMPScDM&start={start}",
                headers={"x-referer": "https://explorer.apis.google.com"}) as r:
            response = await r.json()
            result = ""

            if not response.get("items"):
                return await msg.edit("No results found!")
            for item in response["items"]:
                title = item["title"]
                link = item["link"]
                if "/s" in item["link"]:
                    link = item["link"].replace("/s", "")
                elif re.search(r'\/\d', item["link"]):
                    link = re.sub(r'\/\d', "", item["link"])
                if "?" in link:
                    link = link.split("?")[0]
                if link in result:
                    # remove duplicates
                    continue
                result += f"{title}\n{link}\n\n"
            prev_and_next_btns = [Button.inline("▶️Next▶️", data=f"next {start + 10} {event.text.split()[1]}")]
            await msg.edit(result, link_preview=False, buttons=prev_and_next_btns)
            await session.close()
