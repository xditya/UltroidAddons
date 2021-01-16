from . import *

@ultroid_cmd(pattern="gif ?(.*)")
async def gifs(event):
    get = event.pattern_match.group(1)
    if not get:
       await event.edit(".gif <text>")
       return
    gifs = await ultroid_bot.inline_query("gif", f"{get}")
    await gifs[0].click(event.chat.id, reply_to=event.reply_to_msg_id, silent=True ,hide_via=True)
    await event.delete()
