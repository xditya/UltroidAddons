"""
✘ Commands Available

• `{i}joke`
    To get joke.

• `{i}url <long url>`
    To get a shorten link of long link.
    
• `{i}decide`
    Decide something.
    
"""

import os
from pyjokes import get_joke
import requests
import json
from . import *
from telethon.errors import ChatSendMediaForbiddenError

@ultroid_cmd(pattern="joke")
async def _(ult): 
    await eor(ult, get_joke()) 

@ultroid_cmd(pattern="url ?(.*)")
async def _(event):
    input_str = event.pattern_match.group(1)
    sample_url = "https://da.gd/s?url={}".format(input_str)
    response_api = requests.get(sample_url).text
    if response_api:
        await eor(event, "Shortened url==> {} for the given url==> {}.".format(response_api, input_str))
    else:
        await eor(event, "something w3nt wrong. please try again later.")
                  
@ultroid_cmd(pattern="decide")
async def _(event):
    message_id = event.message.id
    if event.reply_to_msg_id:
        message_id = event.reply_to_msg_id
    r = requests.get("https://yesno.wtf/api").json()
    try:
        await ultroid_bot.send_message(
        event.chat_id, r["answer"], reply_to=message_id, file=r["image"])
    except ChatSendMediaForbiddenError:
        await eor(event,r['answer'])
    
HELP.update({f"{__name__.split('.')[2]}": f"{__doc__.format(i=Var.HNDLR)}"})
