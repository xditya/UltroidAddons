import os
from pyjokes import get_joke #import from library
from telethon import events
import requests
import json

@ultroid_cmd(pattern="joke")
async def _(ult): 
    await ult.edit(get_joke()) 

@ultroid_cmd(pattern="url ?(.*)")
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    sample_url = "https://da.gd/s?url={}".format(input_str)
    response_api = requests.get(sample_url).text
    if response_api:
        await event.edit("Shortened url==> {} for the given url==> {}.".format(response_api, input_str))
    else:
        await event.edit("something w3nt wrong. please try again later.")

