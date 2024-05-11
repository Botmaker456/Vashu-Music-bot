from traceback import format_exc
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from search_engine_parser.core.engines.google import Search as GoogleSearch
from search_engine_parser.core.engines.stackoverflow import \
    Search as StackSearch
from search_engine_parser.core.exceptions import NoResultsFound, NoResultsOrTrafficError
from FIXXMUSIC import app
from pyrogram import filters




gsearch = GoogleSearch()
stsearch = StackSearch()



def ikb(rows=None, back=False, todo="start_back"):
    """
    rows = pass the rows
    back - if want to make back button
    todo - callback data of back button
    """
    if rows is None:
        rows = []
    lines = []
    try:
        for row in rows:
            line = []
            for button in row:
                btn_text = button.split(".")[1].capitalize()
                button = btn(btn_text, button)
                line.append(button)
            lines.append(line)
    except AttributeError:
        for row in rows:
            line = []
            for button in row:
                button = btn(*button)
                line.append(button)
            lines.append(line)
    except TypeError:
        # make a code to handel that error
        line = []
        for button in rows:
            button = btn(*button)  # InlineKeyboardButton
            line.append(button)
        lines.append(line)
    if back:
        back_btn = [(btn("ʙᴀᴄᴋ", todo))]
        lines.append(back_btn)
    return InlineKeyboardMarkup(inline_keyboard=lines)


def btn(text, value, type="callback_data"):
    return InlineKeyboardButton(text, **{type: value})






@app.on_message(filters.command('vgoogle'))
async def search_(app: app, msg: Message):
    split = msg.text.split(None, 1)
    if len(split) == 1:
        return await msg.reply_text("**ɢɪᴠᴇ ǫᴜᴇʀʏ ᴛᴏ sᴇᴀʀᴄʜ**/ 𝙆𝙊𝙄 𝙌𝙐𝙀𝙍𝙔 𝘿𝙊 𝙅𝘼𝘽𝙃𝙄 𝙏𝙊 𝙎𝙀𝘼𝙍𝘾𝙃 𝙆𝘼𝙍𝙐𝙉𝙂𝙄")
    to_del = await msg.reply_text("**sᴇᴀʀᴄʜɪɴɢ ᴏɴ ɢᴏᴏɢʟᴇ...**/ 𝙍𝙐𝙆𝙊 𝘼𝘽 𝙎𝙀𝘼𝙍𝘾𝙃𝙄𝙉𝙂 𝙃𝙊 𝙍𝘼𝙃𝘼 𝙃")
    query = split[1]
    try:
        result = await gsearch.async_search(query)
        keyboard = ikb(
            [
                [
                    (
                        f"{result[0]['titles']}",
                        f"{result[0]['links']}",
                        "url",
                    ),
                ],
                [
                    (
                        f"{result[1]['titles']}",
                        f"{result[1]['links']}",
                        "url",
                    ),
                ],
                [
                    (
                        f"{result[2]['titles']}",
                        f"{result[2]['links']}",
                        "url",
                    ),
                ],
                [
                    (
                        f"{result[3]['titles']}",
                        f"{result[3]['links']}",
                        "url",
                    ),
                ],
                [
                    (
                        f"{result[4]['titles']}",
                        f"{result[4]['links']}",
                        "url",
                    ),
                ],
            ]
        )

        txt = f"**ʜᴇʀᴇ ᴀʀᴇ ᴛʜᴇ ʀᴇsᴜʟᴛs ᴏғ ʀǫᴜᴇsᴛᴇᴅ : {query.title()}**"
        await to_del.delete()
        await msg.reply_text(txt, reply_markup=keyboard)
        return
    except NoResultsFound:
        await to_del.delete()
        await msg.reply_text("**ɴᴏ ʀᴇsᴜʟᴛ ғᴏᴜɴᴅ ᴄᴏʀʀᴇsᴘᴏɴᴅɪɴɢ ᴛᴏ ʏᴏᴜʀ ǫᴜᴇʀʏ**")
        return
    except NoResultsOrTrafficError:
        await to_del.delete()
        await msg.reply_text("****ɴᴏ ʀᴇsᴜʟᴛ ғᴏᴜɴᴅ ᴅᴜᴇ ᴛᴏ ᴛᴏᴏ ᴍᴀɴʏ ᴛʀᴀғғɪᴄ**")
        return
    except Exception as e:
        await to_del.delete()
        await msg.reply_text(f"**sᴏᴍᴇᴛʜɪɴɢ ᴡᴇɴᴛ ᴡʀᴏɴɢ 𝘼𝙋 𝙉𝙀 𝙆𝙐𝘾𝙃 𝙂𝘼𝙇𝘼𝙏 𝙄𝙉𝙋𝙐𝙏 𝘿𝙄𝙔𝘼 𝙃 𝙈𝘼𝙔 𝙉𝘼𝙃𝙄 𝙆𝘼𝙍 𝙋𝘼 𝙍𝘼𝙃𝙄 𝙃𝙐 𝙁𝙄𝙍 𝙎𝙀 𝙆𝘼𝙍𝙊 𝙊𝙍 𝙎𝘼𝙃𝙄 𝙄𝙉𝙋𝙐𝙏 𝘿𝙊 𝙅𝘼𝘽𝙃𝙄 𝙆𝘼𝙍𝙋𝘼𝙐𝙉𝙂𝙄:\nʀᴇᴘᴏʀᴛ ᴀᴛ ɪᴛ** @iam_fixx")
        print(f"error : {e}")
        return



@app.on_message(filters.command('stack'))
async def stack_search_(app: app, msg: Message):
    split = msg.text.split(None, 1)
    if len(split) == 1:
        return await msg.reply_text("**ɢɪᴠᴇ ǫᴜᴇʀʏ ᴛᴏ sᴇᴀʀᴄʜ**/ 𝙆𝙊𝙄 𝙌𝙐𝙀𝙍𝙔 𝘿𝙊 𝙅𝘼𝘽𝙃𝙄 𝙏𝙊 𝙎𝙀𝘼𝙍𝘾𝙃 𝙆𝘼𝙍𝙐𝙉𝙂𝙄")
    to_del = await msg.reply_text("**sᴇᴀʀᴄʜɪɴɢ ᴏɴ ɢᴏᴏɢʟᴇ.../ 𝙍𝙐𝙆𝙊 𝘼𝘽 𝙎𝙀𝘼𝙍𝘾𝙃𝙄𝙉𝙂 𝙃𝙊 𝙍𝘼𝙃𝘼 𝙃**")
    query = split[1]
    try:
        result = await stsearch.async_search(query)
        keyboard = ikb(
            [
                [
                    (
                        f"{result[0]['titles']}",
                        f"{result[0]['links']}",
                        "url",
                    ),
                ],
                [
                    (
                        f"{result[1]['titles']}",
                        f"{result[1]['links']}",
                        "url",
                    ),
                ],
                [
                    (
                        f"{result[2]['titles']}",
                        f"{result[2]['links']}",
                        "url",
                    ),
                ],
                [
                    (
                        f"{result[3]['titles']}",
                        f"{result[3]['links']}",
                        "url",
                    ),
                ],
                [
                    (
                        f"{result[4]['titles']}",
                        f"{result[4]['links']}",
                        "url",
                    ),
                ],
            ]
        )

        txt = f"**ʜᴇʀᴇ ᴀʀᴇ ᴛʜᴇ ʀᴇsᴜʟᴛs ᴏғ ʀǫᴜᴇsᴛᴇᴅ : {query.title()}**"
        await to_del.delete()
        await msg.reply_text(txt, reply_markup=keyboard)
        return
    except NoResultsFound:
        await to_del.delete()
        await msg.reply_text("**ɴᴏ ʀᴇsᴜʟᴛ ғᴏᴜɴᴅ ᴄᴏʀʀᴇsᴘᴏɴᴅɪɴɢ ᴛᴏ ʏᴏᴜʀ ǫᴜᴇʀʏ**")
        return
    except NoResultsOrTrafficError:
        await to_del.delete()
        await msg.reply_text("****ɴᴏ ʀᴇsᴜʟᴛ ғᴏᴜɴᴅ ᴅᴜᴇ ᴛᴏ ᴛᴏᴏ ᴍᴀɴʏ ᴛʀᴀғғɪᴄ**")
        return
    except Exception as e:
        await to_del.delete()
        await msg.reply_text(f"**sᴏᴍᴇᴛʜɪɴɢ ᴡᴇɴᴛ ᴡʀᴏɴɢ :\nʀᴇᴘᴏʀᴛ ᴀᴛ ɪᴛ** @DevsOops")
        print(f"error : {e}")
        return




