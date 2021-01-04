import os
from pyjokes import get_joke #import from library
@ultroid_cmd(pattern="joke")
async def _(ult): 
    await ult.edit(get_joke()) 
