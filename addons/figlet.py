import pyfiglet

CMD_SET = {
    "slant": "slant",
    "3D": "3-d",
    "5line": "5lineoblique",
    "alpha": "alphabet",
    "banner": "banner3-D",
    "doh": "doh",
    "iso": "isometric1",
    "letter": "letters",
    "allig": "alligator",
    "dotm": "dotmatrix",
    "bubble": "bubble",
    "bulb": "bulbhead",
    "digi": "digital",
}

@ultroid_cmd(pattern="figlet ?(.*)")
async def figlet(event):
    input_str = event.pattern_match.group(1)
    if "|" in input_str:
        text, cmd = input_str.split("|", maxsplit=1)
    elif input_str is not None:
        cmd = None
        text = input_str
    else:
        await eod(event, "Please add some text to figlet", time=10)
        return
    if cmd is not None:
        try:
            font = CMD_SET[cmd]
        except KeyError:
            await eod(event, "Invalid selected font.", time=10)
            return
        result = pyfiglet.figlet_format(text, font=font)
    else:
        result = pyfiglet.figlet_format(text)
    await event.edit(f"‌‌‎`{result}`")
