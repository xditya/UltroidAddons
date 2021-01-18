import asyncio
from . import *

@ultroid_cmd(pattern="type ?(.*)")
async def _(event):
    input_str = event.pattern_match.group(1)
    if not input_str:
        return await eor(event,'Give me something to type !')
    shiiinabot = "\u2060"
    for i in range(601):
        shiiinabot += "\u2060"
    try:
        okla=await eor(event,shiiinabot)
    except Exception as e:
        logger.warn(str(e))
    typing_symbol = "|"
    previous_text = ""
    await okla.edit(typing_symbol)
    await asyncio.sleep(0.4)
    for character in input_str:
        previous_text = previous_text + "" + character
        typing_text = previous_text + "" + typing_symbol
        try:
            await okla.edit(typing_text)
        except Exception as e:
            logger.warn(str(e))
            pass
        await asyncio.sleep(0.4)
        try:
            await okla.edit(previous_text)
        except Exception as e:
            logger.warn(str(e))
            pass
        await asyncio.sleep(0.4)
