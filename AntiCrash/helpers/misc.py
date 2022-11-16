#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.
# Recode By hdiiofficial

import asyncio
import shlex
import socket
from typing import Tuple
from AntiCrash import LOGGER
import dotenv

HAPP = None

def install_req(cmd: str) -> Tuple[str, str, int, int]:
    async def install_requirements():
        args = shlex.split(cmd)
        process = await asyncio.create_subprocess_exec(
            *args,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await process.communicate()
        return (
            stdout.decode("utf-8", "replace").strip(),
            stderr.decode("utf-8", "replace").strip(),
            process.returncode,
            process.pid,
        )

    return asyncio.get_event_loop().run_until_complete(install_requirements())

async def create_botlog(client):
    if HAPP is None:
        return
    LOGGER("PiPyro").info(
        "TUNGGU SEBENTAR. SEDANG MEMBUAT GROUP LOG USERBOT UNTUK ANDA"
    )
    desc = "Group Log untuk PiPyro-UserBot.\n\nHARAP JANGAN KELUAR DARI GROUP INI.\n\n✨ Powered By ~ @hdiiofficial ✨"
    try:
        gruplog = await client.create_supergroup("Log UserBot", desc)
        path = dotenv.find_dotenv("config.env")
        dotenv.set_key(path, "BOTLOG_CHATID", gruplog.id)
    except Exception:
        LOGGER("PiPyro").warning(
            "var BOTLOG_CHATID kamu belum di isi. Buatlah grup telegram dan masukan bot @MissRose_bot lalu ketik /id Masukan id grup nya di var BOTLOG_CHATID"
        )
