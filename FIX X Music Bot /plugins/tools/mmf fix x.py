import os
import textwrap
from PIL import fImage, ImageDraw, ImageFont
from pyrogram import filters
from pyrogram.types import Message
from FIXXMUSIC import app

@app.on_message(filters.command("vmmf"))
async def mmf(_, message: Message):
    chat_id = message.chat.id
    reply_message = message.reply_to_message

    if len(message.text.split()) < 2:
        await message.reply_text("**Give me text after /mmf to memify.**/ 𝘼𝙍𝙀𝙀 𝙋𝘼𝙃𝙇𝙀 𝙇𝙀𝙆𝙃𝙊 /𝙢𝙢𝙛 𝙐𝙎𝙆𝙀 𝘽𝘼𝘼𝘿 𝐈𝐌𝐀𝐆𝐄 𝙈𝙀 𝙅𝙊 𝙇𝙀𝙆𝙃𝙑𝘼𝙉𝘼 𝘾𝙃𝘼𝙃𝙏𝙀 𝙃𝙊 𝙑𝙊 𝙈𝙐𝙅𝙃𝙀 𝙇𝙀𝙆𝙃 𝙆𝙀 𝘿𝙊 /𝙢𝙢𝙛 𝙆𝙀 𝘽𝘼𝘼𝘿 𝙈𝘼𝙔 𝘽𝘼𝙉𝘼𝘿𝙐𝙉𝙂𝙄")
        return

    msg = await message.reply_text("**Memifying this image! 👀/ 𝘼𝘽 𝘽𝘼𝙉𝘼 𝙍𝘼𝙃𝙄 𝙃𝙐 𝙍𝙐𝙆𝙊 20 𝙎𝙀𝘾𝙊𝙉𝘿𝙎**")
    text = message.text.split(None, 1)[1]
    file = await app.download_media(reply_message)

    meme = await drawText(file, text)
    await app.send_document(chat_id, document=meme)

    await msg.delete()

    os.remove(meme)


async def drawText(image_path, text):
    img = Image.open(image_path)

    os.remove(image_path)

    i_width, i_height = img.size

    if os.name == "nt":
        fnt = "arial.ttf"
    else:
        fnt = "./FIXXMUSIC/assets/default.ttf"

    m_font = ImageFont.truetype(fnt, int((70 / 640) * i_width))

    if ";" in text:
        upper_text, lower_text = text.split(";")
    else:
        upper_text = text
        lower_text = ""

    draw = ImageDraw.Draw(img)

    current_h, pad = 10, 5

    if upper_text:
        for u_text in textwrap.wrap(upper_text, width=15):
            u_width, u_height = draw.textsize(u_text, font=m_font)

            draw.text(
                xy=(((i_width - u_width) / 2) - 2, int((current_h / 640) * i_width)),
                text=u_text,
                font=m_font,
                fill=(0, 0, 0),
            )

            draw.text(
                xy=(((i_width - u_width) / 2) + 2, int((current_h / 640) * i_width)),
                text=u_text,
                font=m_font,
                fill=(0, 0, 0),
            )

            draw.text(
                xy=((i_width - u_width) / 2, int(((current_h / 640) * i_width)) - 2),
                text=u_text,
                font=m_font,
                fill=(0, 0, 0),
            )

            draw.text(
                xy=(((i_width - u_width) / 2), int(((current_h / 640) * i_width)) + 2),
                text=u_text,
                font=m_font,
                fill=(0, 0, 0),
            )

            draw.text(
                xy=((i_width - u_width) / 2, int((current_h / 640) * i_width)),
                text=u_text,
                font=m_font,
                fill=(255, 255, 255),
            )

            current_h += u_height + pad

    if lower_text:
        for l_text in textwrap.wrap(lower_text, width=15):
            u_width, u_height = draw.textsize(l_text, font=m_font)

            draw.text(
                xy=(
                    ((i_width - u_width) / 2) - 2,
                    i_height - u_height - int((20 / 640) * i_width),
                ),
                text=l_text,
                font=m_font,
                fill=(0, 0, 0),
            )

            draw.text(
                xy=(
                    ((i_width - u_width) / 2) + 2,
                    i_height - u_height - int((20 / 640) * i_width),
                ),
                text=l_text,
                font=m_font,
                fill=(0, 0, 0),
            )

            draw.text(
                xy=(
                    (i_width - u_width) / 2,
                    (i_height - u_height - int((20 / 640) * i_width)) - 2,
                ),
                text=l_text,
                font=m_font,
                fill=(0, 0, 0),
            )

            draw.text(
                xy=(
                    (i_width - u_width) / 2,
                    (i_height - u_height - int((20 / 640) * i_width)) + 2,
                ),
                text=l_text,
                font=m_font,
                fill=(0, 0, 0),
            )

            draw.text(
                xy=(
                    (i_width - u_width) / 2,
                    i_height - u_height - int((20 / 640) * i_width),
                ),
                text=l_text,
                font=m_font,
                fill=(255, 255, 255),
            )

            current_h += u_height + pad

    image_name = "vashumemify.webp"

    webp_file = os.path.join(image_name)

    img.save(webp_file, "vwebp")

    return webp_file
