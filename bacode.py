# BarCode Generator
# Command .barcode (your text)
# By @snappy101
# Ported to Ultroid by @its_xditya

"""
✘ Commands Available -
• `{i}barcode <long text to include>`
    Create a barcode containing that text.
"""

from . import *
import asyncio
import os
from datetime import datetime
import barcode

TMP_DOWNLOAD_DIRECTORY = "./cache"

@ultroid_cmd(pattern="barcode ?(.*)")
async def _(event):
    x = await eor(event, "`Creating barcode...`")
    start = datetime.now()
    input_str = event.pattern_match.group(1)
    message = f"SYNTAX: `{hndlr}barcode <long text to include>`"
    reply_msg_id = event.message.id
    if input_str:
        message = input_str
    elif event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        reply_msg_id = previous_message.id
        if previous_message.media:
            downloaded_file_name = await ultroid_bot.download_media(
                previous_message,
                TMP_DOWNLOAD_DIRECTORY,
            )
            m_list = None
            with open(downloaded_file_name, "rb") as fd:
                m_list = fd.readlines()
            message = ""
            for m in m_list:
                message += m.decode("UTF-8") + "\r\n"
            os.remove(downloaded_file_name)
        else:
            message = previous_message.message
    else:
        message = f"SYNTAX: `{hndlr}barcode <long text to include>`"
    bar_code_type = "code128"
    try:
        bar_code_mode_f = barcode.get(bar_code_type, message, writer=ImageWriter())
        filename = bar_code_mode_f.save(bar_code_type)
        await ultroid_bot.send_file(
            event.chat_id,
            filename,
            caption=message,
            reply_to=reply_msg_id,
        )
        os.remove(filename)
    except Exception as e:
        await e.edit(str(e))
        return
    end = datetime.now()
    ms = (end - start).seconds
    await x.edit("Created BarCode in {} seconds".format(ms))
    await asyncio.sleep(5)
    await event.delete()


HELP.update({f"{__name__.split('.')[2]}": f"{__doc__.format(i=Var.HNDLR)}"})
