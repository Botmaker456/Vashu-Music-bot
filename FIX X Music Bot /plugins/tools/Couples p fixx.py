import os
import random
from datetime import datetime
from telegraph import upload_file
from PIL import Image, ImageDraw
from pyrogram import *
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.enums import *

# BOT FILE NAME
from FIXXMUSIC import app as app
from FIXXMUSIC.mongo.couples_db import _get_image, get_couple

POLICE = [
    [
        InlineKeyboardButton(
            text="𓊈𒆜彡[𝙑𝘼𝙎𝙃𝙐 𝙁𝙄𝙓 𝙓 𝙈𝙐𝙎𝙄𝘾 ]彡𒆜𓊉",
            url=f"https://t.me/ALLTYPECC",
        ),
    ],
]


def dt():
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M")
    dt_list = dt_string.split(" ")
    return dt_list


def dt_tom():
    a = (
            str(int(dt()[0].split("/")[0]) + 1)
            + "/"
            + dt()[0].split("/")[1]
            + "/"
            + dt()[0].split("/")[2]
    )
    return a


tomorrow = str(dt_tom())
today = str(dt()[0])


@app.on_message(filters.command("vcouples", "vcls))
                async def ctest(_, message):
    cid = message.chat.id
    if message.chat.type == ChatType.PRIVATE:
        return await message.reply_text("ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴏɴʟʏ ᴡᴏʀᴋs ɪɴ ɢʀᴏᴜᴘs.")
    try:
        #  is_selected = await get_couple(cid, today)
        #  if not is_selected:
        msg = await message.reply_text(
            "ɢᴇɴᴇʀᴀᴛɪɴɢ ᴄᴏᴜᴘʟᴇs ɪᴍᴀɢᴇ.../ 𝙍𝙐𝙆 𝙅𝘼𝙊 𝙅𝙄 𝘾𝙊𝙐𝙋𝙇𝙀𝙎 𝘽𝘼𝙉𝘼 𝙍𝘼𝙃𝙄 𝙃𝙐 𝙎𝙊𝘾𝙃 𝙍𝘼𝙃𝙄 𝙃𝙐 𝙆𝙄 𝙇𝘼𝘿𝙆𝙄 𝙇𝘼𝘿𝙆𝙄 𝘽𝘼𝙉𝘼𝙐 𝙔𝘼 𝙇𝘼𝘿𝙆𝘼 𝙇𝘼𝘿𝙆𝘼😝😏")
        # GET LIST OF USERS
        list_of_users = []

        async for i in app.get_chat_members(message.chat.id, limit=50):
            if not i.user.is_bot:
                list_of_users.append(i.user.id)

        c1_id = random.choice(list_of_users)
        c2_id = random.choice(list_of_users)
        while c1_id == c2_id:
            c1_id = random.choice(list_of_users)

        photo1 = (await app.get_chat(c1_id)).photo
        photo2 = (await app.get_chat(c2_id)).photo

        N1 = (await app.get_users(c1_id)).mention
        N2 = (await app.get_users(c2_id)).mention

        try:
            p1 = await app.download_media(photo1.big_file_id, file_name="pfp.png")
        except Exception:
            p1 = "FIXXMUSIC/assets/upic.png"
        try:
            p2 = await app.download_media(photo2.big_file_id, file_name="pfp1.png")
        except Exception:
            p2 = "FIXXMUSIC/assets/upic.png"

        img1 = Image.open(f"{p1}")
        img2 = Image.open(f"{p2}")

        img = Image.open("FIXXMUSIC/assets/cppic.png")

        img1 = img1.resize((437, 437))
        img2 = img2.resize((437, 437))

        mask = Image.new('L', img1.size, 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0) + img1.size, fill=255)

        mask1 = Image.new('L', img2.size, 0)
        draw = ImageDraw.Draw(mask1)
        draw.ellipse((0, 0) + img2.size, fill=255)

        img1.putalpha(mask)
        img2.putalpha(mask1)

        draw = ImageDraw.Draw(img)

        img.paste(img1, (116, 160), img1)
        img.paste(img2, (789, 160), img2)

        img.save(f'test_{cid}.png')

        TXT = f"""
**ᴛᴏᴅᴀʏ's ᴄᴏᴜᴘʟᴇ ᴏғ ᴛʜᴇ ᴅᴀʏ is sᴇʟᴇᴄᴛᴇᴅ by VASHU :

{N1} + {N2} = 💚

ɴᴇxᴛ ᴄᴏᴜᴘʟᴇs ᴡɪʟʟ ʙᴇ sᴇʟᴇᴄᴛᴇᴅ ᴏɴ {tomorrow} by VASHU!!**
"""

        await message.reply_photo(f"test_{cid}.png", caption=TXT, reply_markup=InlineKeyboardMarkup(POLICE),
                                  )
        await msg.delete()
        a = upload_file(f"test_{cid}.png")
        for x in a:
            img = "https://graph.org/" + x
            couple = {"c1_id": c1_id, "c2_id": c2_id}
        # await save_couple(cid, today, couple, img)


    # elif is_selected:
    #   msg = await message.reply_text("𝐆ᴇᴛᴛɪɴɢ 𝐓ᴏᴅᴀʏs 𝐂ᴏᴜᴘʟᴇs 𝐈ᴍᴀɢᴇ.../ 𝙍𝙐𝙆 𝙅𝘼𝙊 𝙅𝙄 𝘾𝙊𝙐𝙋𝙇𝙀𝙎 𝘽𝘼𝙉𝘼 𝙍𝘼𝙃𝙄 𝙃𝙐 𝙎𝙊𝘾𝙃 𝙍𝘼𝙃𝙄 𝙃𝙐 𝙆𝙄 𝙇𝘼𝘿𝙆𝙄 𝙇𝘼𝘿𝙆𝙄 𝘽𝘼𝙉𝘼𝙐 𝙔𝘼 𝙇𝘼𝘿𝙆𝘼 𝙇𝘼𝘿𝙆𝘼😝😏")
    #   b = await _get_image(cid)
    #  c1_id = int(is_selected["c1_id"])
    #  c2_id = int(is_selected["c2_id"])
    #  c1_name = (await app.get_users(c1_id)).first_name
    # c2_name = (await app.get_users(c2_id)).first_name

    #   TXT = f"""
    # **𝐓ᴏᴅᴀʏ's 𝐒ᴇʟᴇᴄᴛᴇᴅ 𝐂ᴏᴜᴘʟᴇs By VASHU🎉 :
    # ➖➖➖➖➖➖➖➖➖➖➖➖
    # [{c1_name}](tg://openmessage?user_id={c1_id}) + [{c2_name}](tg://openmessage?user_id={c2_id}) = ❣️
    # ➖➖➖➖➖➖➖➖➖➖➖➖
    # 𝐍ᴇxᴛ 𝐂ᴏᴜᴘʟᴇs 𝐖ɪʟʟ 𝐁ᴇ 𝐒ᴇʟᴇᴄᴛᴇᴅ 𝐎ɴ {tomorrow} !!**
    # """
    #        await message.reply_photo(b, caption=TXT)
    # await msg.delete()
    except Exception as e:
        print(str(e))
    try:
        os.remove(f"./downloads/pfp1.png")
        os.remove(f"./downloads/pfp2.png")
        os.remove(f"test_{cid}.png")
    except Exception:
        pass


__mod__ = "COUPLES"
__help__ = """
**» /vcouples** - Get Todays Couples Of The Group In Interactive View
"""











