import os
os.system("pip install pyjokes") # for the package to be installed..
from pyjokes import get_joke #import from library
@ultroid_cmd(pattern="joke")
async def _(ult): 
    await ult.edit(get_joke()) 
