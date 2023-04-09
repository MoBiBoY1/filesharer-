#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>➰️ 𝐓𝐡𝐢𝐬 𝐢𝐬 𝐓𝐡𝐞 𝐌𝐞𝐦𝐞 𝐁𝐨𝐭 𝐓𝐡𝐚𝐭 𝐏𝐫𝐨𝐯𝐢𝐝𝐞𝐬 𝐃𝐚𝐢𝐥𝐲 𝐌𝐞𝐦𝐞𝐬😂 𝐓𝐨 𝐘𝐨𝐮 | Jᴏɪɴ ᴍᴀɪɴ ᴄʜᴀɴɴᴇʟ @Loki_BoTs\n\n○ Creator : <a href='tg://user?id={OWNER_ID}'>This Person</a>\n○ Language : <code>Python3</code>\n○ Library : <a href='https://docs.pyrogram.org/'>Pyrogram asyncio {__version__}</a>\n○ Source Code : <a href='https://github.com/MoBiBoY1'>Click here</a>\n○ Channel : @Loki_BoTs\n○ leech groups: @loki_leech_updates</b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🗑 Close", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
