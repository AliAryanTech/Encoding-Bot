#    This file is part of the CompressorQueue distribution.
#    Copyright (c) 2021 Danish_00
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, version 3.
#
#    This program is distributed in the hope that it will be useful, but
#    WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#    General Public License for more details.
#
# License can be found in <
# https://github.com/1Danish-00/CompressorQueue/blob/main/License> .

from .worker import *


async def up(event):
    if not event.is_private:
        return
    stt = dt.now()
    ed = dt.now()
    v = ts(int((ed - uptime).seconds) * 1000)
    ms = (ed - stt).microseconds / 1000
    p = f"📊Pɪɴɢ = {ms}ms"
    await event.reply(v + "\n" + p)


async def start(event):
    await event.reply(
        f"Hi `{event.sender.first_name}`\nThis is A Compressor Bot Which Can Encode Videos.\nReduce Size of Videos With Negligible Quality Change\nAlso you can Generate Screenshots too.",
        buttons=[
            [Button.inline("Checkout Help Menu 📑", data="ihelp")],
            [
                Button.url("Aɴιмє Grσυρ 💬", url="t.me/AnimeListChat"),
                Button.url("Anime Channel 🔥", url="t.me/AnimeListUp"),
            ],
        ],
    )


async def help(event):
    await event.reply(
        "**🤖 A Quality Compressor Bot**\n\n • This Bot Compress Videos With Negligible Quality Change.\n • Generate Sample Compressed Video\n • Easy to Use\n • Due to Quality Settings Bot Takes Time To Compress.\n • So Be patience Nd Send videos One By One After Completing.\n • Dont Spam Bot.\n\nJust Forward Video To Get Options"
    )


async def ihelp(event):
    await event.edit(
        "**🤖 A Quality Compressor Bot**\n\n • This Bot Compress Videos With Negligible Quality Change.\n • Generate Sample Compressed Video\n • Screenshots Too\n • Easy to Use\n • Due to Quality Settings Bot Takes Time To Compress.\n • So Be patience Nd Send videos One By One After Completing.\n • Dont Spam Bot.\n\n • Just Forward Video To Get Options",
        buttons=[Button.inline("BACK", data="beck")],
    )


async def beck(event):
    await event.edit(
        f"Hi `{event.sender.first_name}`\n • This is A CompressorQueue Which Can Encode Videos.\n • Reduce Size of Videos With Negligible Quality Change\n • You can Generate Screenshots too.",
        buttons=[
            [Button.inline("Checkout Help Menu 📑", data="ihelp")],
            [
                Button.url("Aɴιмє Grσυρ 💬", url="t.me/AnimeListChat"),
                Button.url("Anime Channel 🔥", url="t.me/AnimeListUp"),
            ],
        ],
    )
