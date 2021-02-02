"""
✘ Commands Available

• `{i}joke`
    To get joke.

• `{i}url <long url>`
    To get a shorten link of long link.
    
• `{i}decide`
    Decide something.

• `{i}xoxo`
    Opens tic tac toe game only where using inline mode is allowed.


    
"""

import os, re, random
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

UNSAFE_CHARACTERS = re.compile(
    "["
    "\U0001F1E0-\U0001F1FF"  # flags (iOS)
    "\U0001F300-\U0001F5FF"  # symbols & pictographs
    "\U0001F600-\U0001F64F"  # emoticons
    "\U0001F680-\U0001F6FF"  # transport & map symbols
    "\U0001F700-\U0001F77F"  # alchemical symbols
    "\U0001F780-\U0001F7FF"  # Geometric Shapes Extended
    "\U0001F800-\U0001F8FF"  # Supplemental Arrows-C
    "\U0001F900-\U0001F9FF"  # Supplemental Symbols and Pictographs
    "\U0001FA00-\U0001FA6F"  # Chess Symbols
    "\U0001FA70-\U0001FAFF"  # Symbols and Pictographs Extended-A
    "\U00002702-\U000027B0"  # Dingbats 
    "]+")
def deEmojify(inputString: str) -> str:
    # Remove emojis and other unsafe characters from string
    return re.sub(UNSAFE_CHARACTERS, '', inputString)
@ultroid_cmd(pattern="xoxo")
async def nope(doit):
    ok = doit.pattern_match.group(1)
    if not ok:
        if doit.is_reply:
            wtf = (await doit.get_reply_message()).message
        
            return
    xoxoxo = await bot.inline_query(
        "xobot", f"{(deEmojify(ok))}")
    await xoxoxo[0].click(doit.chat_id,
                            reply_to=doit.reply_to_msg_id,
                            silent=True if doit.is_reply else False,
                            hide_via=True)
    await doit.delete()

    
HELP.update({f"{__name__.split('.')[2]}": f"{__doc__.format(i=Var.HNDLR)}"})
