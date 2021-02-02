"""
✘ Commands Available

• `{i}joke`
    To get joke.

• `{i}url <long url>`
    To get a shorten link of long link.
    
• `{i}decide`
    Decide something.

• `{i}gif`
    .gif <your query>, sends the desired gif related to your query(not always).

• `{i}vtog`
    .vtog <in reply to a video>, converts any video to a gif with low time limit(takes time).

• `{i}g2t`
    .g2t text|font|size|color|coordinate(x);coordinate(y)|loop|duration

• `{i}xoxo`
    Opens tic tac toe game only where using inline mode is allowed.

• `{i}gps`
    .gps <name of place> , shows the desired place in the map(works where inline is allowed).

"""

import os, re, random, sys
from pyjokes import get_joke
import requests
import json
from . import *
from telethon.errors import ChatSendMediaForbiddenError
from PIL import Image, ImageDraw, ImageFont
import moviepy.editor as m

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

if not os.path.isdir("./ultpath/"):
    os.makedirs("./ultpath/")


@ultroid_cmd(pattern="gif")
async def gifs(ult):
    get = ult.pattern_match.group(1)
    if not get:
       await ult.edit("`.gif <query>`")
       return
    gifs = await ultroid_bot.inline_query("gif", f"{get}")
    await gifs[0].click(ult.chat.id, reply_to=ult.reply_to_msg_id, silent=True ,hide_via=True)
    await ult.delete()    

@ultroid_cmd(pattern="vtog")
async def vtog(ult):
    path = "ultroidd"
    reply = await ult.get_reply_message()
    lol = await ultroid_bot.download_media(reply.media, path)
    file_name = "ultroid.gif"
    clip = (m.VideoFileClip(lol).subclip((4.3),(5.8)).resize(0.3))
    clip.write_gif(file_name)
    hehe = path + "/" + file_name
    await ultroid_bot.send_file(ult.chat_id, file_name)
    for files in (hehe, lol):
        if files and os.path.exists(files):
            os.remove(files)        
    ultroied = await ult.delete()


@ultroid_cmd(pattern="g2t")
global hawkmoth
hawkmoth="I0Rvbm90IEthbmcgTUFERSBCWSBAVEhFX0JMX0FDS19IQVQgTU9ESUZJRUQgQlkgU2gxdmFtICNUZWFtIERDIA=="
async def lol(ult):
    await ult.delete()
    if not os.path.isdir("./imglol"):
        os.makedirs("./imglol")
    rasta = './imglol'
    reply = await ult.get_reply_message()
    me= await ultroid_bot.download_media(reply.media, rasta)
    lol = ult.text
    hui, font,size,color,align,loop,duration= lol[9:].split('|')
    loltext = hui

    
    
    x,y=align.split(";")
    
    size=int(size)


    def adi(text):
        img = Image.open(me)
        fonts = ImageFont.truetype(r"Fonts/{}".format(font),size)
        draw = ImageDraw.Draw(img)
        draw.text(((int(x), int(y))), text,fill=(color),font=fonts )
        
        return img

    # Create the frames
    frames = []

    def ruil(text):
        global c
        for i in range(len(text)+1):
            new_frame = adi(text[:i])
            frames.append(new_frame)
        c = 0

    all_text = f"{loltext}"
    ruil(all_text)


    # Save into a GIF file that loops forever
    frames[0].save('catnoiar.gif', format='GIF',
                   append_images=frames[1:], save_all=True, duration=int(duration), loop=int(loop))
    ukanger = "ultrooiidd.gif" 
    await ultroid_bot.send_file(event.chat_id, ukanger)
global miracul

if hawkmoth!=miracul :
		


           print("GREAT kanger Here")
           
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

@ultroid_cmd(pattern="gps")
async def nope(doit):
    ok = doit.pattern_match.group(1)
    if not ok:
        if doit.is_reply:
            what = (await doit.get_reply_message()).message
        
            return
    mappy = await ultroid_bot.inline_query(
        "openmap_bot", f"{(deEmojify(ok))}")
    await mappy[0].click(doit.chat_id,
                            reply_to=doit.reply_to_msg_id,
                            silent=True if doit.is_reply else False,
                            hide_via=True)
    await doit.delete()


    
HELP.update({f"{__name__.split('.')[2]}": f"{__doc__.format(i=Var.HNDLR)}"})
