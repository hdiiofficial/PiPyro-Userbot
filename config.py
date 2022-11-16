# Credits: @sshdiiofficial
# Copyright (C) 2022 hdiiofficial
#
# This file is a part of < https://github.com/hdiiofficial/PiPyro-Userbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/hdiiofficial/PiPyro-Userbot/blob/main/LICENSE/>.
#
# t.me/SharingUserbot & t.me/hdiiofficial

from base64 import b64decode
from os import getenv

from dotenv import load_dotenv

load_dotenv("config.env")


API_HASH = getenv("API_HASH")
API_ID = int(getenv("API_ID", ""))
BLACKLIST_CHAT = getenv("BLACKLIST_CHAT", None)
if not BLACKLIST_CHAT:
    BLACKLIST_CHAT = [-1001473548283]
BLACKLIST_GCAST = {int(x) for x in getenv("BLACKLIST_GCAST", "").split()}
BOTLOG_CHATID = int(getenv("BOTLOG_CHATID") or 0)
BOT_VER = "0.0.1@main"
BRANCH = "main"
CHANNEL = getenv("CHANNEL", "hdiiofficial")
CMD_HANDLER = getenv("CMD_HANDLER", ".")
DB_URL = getenv("DATABASE_URL", "")
GROUP = getenv("GROUP", "SharingUserbot")
PMPERMIT_PIC = getenv("PMPERMIT_PIC", None)

STRING_SESSION = getenv("STRING_SESSION", "")
# STRING_SESSION1 = getenv("STRING_SESSION1", "")
# STRING_SESSION2 = getenv("STRING_SESSION2", "")
# STRING_SESSION3 = getenv("STRING_SESSION3", "")
# STRING_SESSION4 = getenv("STRING_SESSION4", "")
# STRING_SESSION5 = getenv("STRING_SESSION5", "")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
