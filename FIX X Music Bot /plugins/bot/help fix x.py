from typing import Union
from program import filters, types
from program.types import InlineKeyboardMarkup, Message, InlineKeyboardButton
from FIXXMUSIC import app
from FIXXMUSIC.utils import help_pannel
from FIXXMUSIC.utils.database import get_lang
from FIXXMUSIC.utils.decorators.language import LanguageStart, languageCB
from FIXXMUSIC.utils.inline.help import help_back_markup, private_help_panel
from config import BANNED_USERS, START_IMG_URL, SUPPORT_CHAT
from strings import get_string, helpers
from FIXXMUSIC.utils.stuffs.buttons import BUTTONS
from FIXXMUSIC.utils.stuffs.helper import Helper


@app.on_message(filters.command(["vhelp" , "vashu help"]) & filters.private & ~BANNED_USERS)
@app.on_callback_query(filters.regex("vsettings_back_helper", "vashu settings_back_helper") & ~BANNED_USERS)
async def helper_private(
        client: app, update: Union[types.Message, types.CallbackQuery]
):
    is_callback = isinstance(update, types.CallbackQuery)
    if is_callback:
        try:
            await update.answer()
        except:
            pass
        chat_id = update.message.chat.id
        language = await get_lang(chat_id)
        _ = get_string(language)
        keyboard = help_pannel(_, True)
        await update.edit_message_text(
            _["help_1"].format(SUPPORT_CHAT), reply_markup=keyboard
        )
    else:
        try:
            await update.delete()
        except:
            pass
        language = await get_lang(update.chat.id)
        _ = get_string(language)
        keyboard = help_pannel(_)
        await update.reply_photo(
            photo=START_IMG_URL,
            caption=_["help_1"].format(SUPPORT_CHAT),
            reply_markup=keyboard,
        )


@app.on_message(filters.command(["vhelp" , "vashu help"]) & filters.group & ~BANNED_USERS)
@LanguageStart
async def help_com_group(client, message: Message, _):
    keyboard = private_help_panel(_)
    await message.reply_text(_["vhelp_2" ,"vashu help_2"], reply_markup=InlineKeyboardMarkup(keyboard))


@app.on_callback_query(filters.regex("vhelp_callback" ,"vashu help_callback") & ~BANNED_USERS)
@languageCB
async def helper_cb(client, CallbackQuery, _):
    callback_data = CallbackQuery.data.strip()
    cb = callback_data.split(None, 1)[1]
    keyboard = help_back_markup(_)
    if cb == "vhb1":
        await CallbackQuery.edit_message_text(helpers.HELP_1, reply_markup=keyboard)
    elif cb == "vhb2":
        await CallbackQuery.edit_message_text(helpers.HELP_2, reply_markup=keyboard)
    elif cb == "vhb3":
        await CallbackQuery.edit_message_text(helpers.HELP_3, reply_markup=keyboard)
    elif cb == "vhb4":
        await CallbackQuery.edit_message_text(helpers.HELP_4, reply_markup=keyboard)
    elif cb == "vhb5":
        await CallbackQuery.edit_message_text(helpers.HELP_5, reply_markup=keyboard)
    elif cb == "vhb6":
        await CallbackQuery.edit_message_text(helpers.HELP_6, reply_markup=keyboard)
    elif cb == "vhb7":
        await CallbackQuery.edit_message_text(helpers.HELP_7, reply_markup=keyboard)
    elif cb == "vhb8":
        await CallbackQuery.edit_message_text(helpers.HELP_8, reply_markup=keyboard)
    elif cb == "vhb9":
        await CallbackQuery.edit_message_text(helpers.HELP_9, reply_markup=keyboard)
    elif cb == "vhb10":
        await CallbackQuery.edit_message_text(helpers.HELP_10, reply_markup=keyboard)
    elif cb == "vhb11":
        await CallbackQuery.edit_message_text(helpers.HELP_11, reply_markup=keyboard)
    elif cb == "vhb12":
        await CallbackQuery.edit_message_text(helpers.HELP_12, reply_markup=keyboard)
    elif cb == "vhb13":
        await CallbackQuery.edit_message_text(helpers.HELP_13, reply_markup=keyboard)
    elif cb == "vhb14":
        await CallbackQuery.edit_message_text(helpers.HELP_14, reply_markup=keyboard)
    elif cb == "vhb15":
        await CallbackQuery.edit_message_text(helpers.HELP_15, reply_markup=keyboard)


@app.on_callback_query(filters.regex("vmbot_cb" , "vashubot_cbv") & ~BANNED_USERS)
async def helper_cb(client, CallbackQuery):
    await CallbackQuery.edit_message_text(Helper.HELP_M, reply_markup=InlineKeyboardMarkup(BUTTONS.MBUTTON))


@app.on_callback_query(filters.regex('vmanagebot123' , "vashumanagebot2345"))
async def on_back_button(client, CallbackQuery):
    callback_data = CallbackQuery.data.strip()
    cb = callback_data.split(None, 1)[1]
    keyboard = help_pannel(_, True)
    if cb == "settings_back_helper":
        await CallbackQuery.edit_message_text(
            _["help_1"].format(SUPPORT_CHAT), reply_markup=keyboard
        )


@app.on_callback_query(filters.regex('vmplus' , "me innocient"))
async def mb_plugin_button(client, CallbackQuery):
    callback_data = CallbackQuery.data.strip()
    cb = callback_data.split(None, 1)[1]
    keyboard = InlineKeyboardMarkup([[InlineKeyboardButton("ʙᴀᴄᴋ", callback_data=f"vmbot_cb")]])
    if cb == "Okieeeeee":
        await CallbackQuery.edit_message_text(f"`something errors`", reply_markup=keyboard,
                                              parse_mode=enums.ParseMode.MARKDOWN)
    else:
        await CallbackQuery.edit_message_text(getattr(Helper, cb), reply_markup=keyboard)