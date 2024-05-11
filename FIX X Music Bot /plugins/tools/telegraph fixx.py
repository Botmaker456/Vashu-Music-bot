from telegraph import upload_file
from pyrogram import filters
from FIXXMUSIC import app
from pyrogram.types import InputMediaPhoto


@app.on_message(filters.command(["vtgm" , "vtelegraph" , "vashutgm"]))
def ul(_, message):
    reply = message.reply_to_message
    if reply.media:
        i = message.reply("𝙈𝘼𝙆𝙀𝙄𝙉𝙂 𝘼 𝙇𝙄𝙉𝙆 𝘽𝙔 𝙍𝙀𝙌𝙐𝙀𝙎𝙏𝙀𝘿 𝙐𝙎𝙀𝙍...")
        path = reply.download()
        fk = upload_file(path)
        for x in fk:
            url = "https://telegra.ph" + x

        i.edit(f'Yᴏᴜʀ ʟɪɴᴋ sᴜᴄᴄᴇssғᴜʟ 𝙂𝙀𝙉 𝘽𝙔 𝙑𝘼𝙎𝙃𝙐 {url}')

########____________________________________________________________######

@app.on_message(filters.command(["vgraph" , "vgrf"]))
def ul(_, message):
    reply = message.reply_to_message
    if reply.media:
        i = message.reply("𝙈𝘼𝙆𝙀𝙄𝙉𝙂 𝘼 𝙇𝙄𝙉𝙆 𝘽𝙔 𝙍𝙀𝙌𝙐𝙀𝙎𝙏𝙀𝘿 𝙐𝙎𝙀𝙍...")
        path = reply.download()
        fk = upload_file(path)
        for x in fk:
            url = "https://graph.org" + x

        i.edit(f'Yᴏᴜʀ ʟɪɴᴋ sᴜᴄᴄᴇssғᴜʟ  𝙂𝙀𝙉 𝘽𝙔 𝙑𝘼𝙎𝙃𝙐  {url}')
