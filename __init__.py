# Ultroid - UserBot
# Copyright (C) 2020 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.

import time

from .. import *
from ..dB.core import *
from ..functions import *
from ..functions.all import *
from ..utils import *
from . import *

OWNER_NAME = ultroid_bot.me.first_name
OWNER_ID = ultroid_bot.me.id

# sudo
ok = udB.get("SUDOS")
if ok:
    SUDO_USERS = set(int(x) for x in ok.split())
else:
    SUDO_USERS = ""

if SUDO_USERS:
    sudos = list(SUDO_USERS)
else:
    sudos = ""

on = Var.SUDO

sed = [ultroid_bot.uid, *sudos]
