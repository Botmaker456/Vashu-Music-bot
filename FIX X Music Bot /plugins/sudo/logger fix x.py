from pyrogram import filters

from FIXXMUSIC import app
from FIXXMUSIC.misc import SUDOERS
from FIXXMUSIC.utils.database import add_off, add_on
from FIXXMUSIC.utils.decorators.language import language


@app.on_message(filters.command(["vlogger" , "vashulogger"]) & SUDOERS)
@language
async def vlogger(client, message, _):
    usage = _["log_1"]
    if len(message.command) != 2:
        return await message.reply_text(usage)
    state = message.text.split(None, 1)[1].strip().lower()
    if state == "enable":
        await add_on(2)
        await message.reply_text(_["log_2"])
    elif state == "disable":
        await add_off(2)
        await message.reply_text(_["log_3"])
    else:
        await message.reply_text(usage)
