import asyncio
from datetime import datetime

from ..core.managers import edit_or_reply
from . import hmention, kanjeng

plugin_category = "tools"


@kanjeng.alfareza_cmd(
    pattern="ping( -a|$)",
    command=("ping", plugin_category),
    info={
        "header": "check how long it takes to ping your userbot",
        "flags": {"-a": "average ping"},
        "usage": ["{tr}ping", "{tr}ping -a"],
    },
)
async def _(event):
    "To check ping"
    flag = event.pattern_match.group(1)
    start = datetime.now()
    if flag == " -a":
        kanjengevent = await edit_or_reply(event, "`!....`")
        await asyncio.sleep(0.3)
        await kanjengevent.edit("`..!..`")
        await asyncio.sleep(0.3)
        await kanjengevent.edit("`....!`")
        end = datetime.now()
        tms = (end - start).microseconds / 1000
        ms = round((tms - 0.6) / 3, 3)
        await kanjengevent.edit(f"**☞ Average Pong!**\n➥ {ms} ms")
    else:
        kanjengevent = await edit_or_reply(event, "<b><i>☞ Pong!</b></i>", "html")
        end = datetime.now()
        ms = (end - start).microseconds / 1000
        await kanjengevent.edit(
            f"<b><i>☞ Alpha 🤖</b></i>\n➥ Pong {ms} <b><i>ms\n➥ Bot of {hmention}</b></i>",
            parse_mode="html",
        )


@kanjeng.alfareza_cmd(
    pattern="fping$",
    command=("fping", plugin_category),
    info={"header": "Shows the server ping with extra animation", "usage": "{tr}fping"},
)
async def _(event):
    "To check ping with animation"
    start = datetime.now()
    animation_interval = 0.3
    animation_ttl = range(26)
    event = await edit_or_reply(event, "ping....")
    animation_chars = [
        "⬛⬛⬛⬛⬛⬛⬛⬛⬛",
        "⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛",
        "⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛",
        "⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ ",
        "⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ ",
        "⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛‎📶‎📶⬛⬛",
        "⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛‎📶‎📶⬛⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛",
        "⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛‎📶‎📶⬛⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛",
        "⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛‎📶‎📶⬛⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛",
        "⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛‎📶‎📶⬛⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛",
        "⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛‎📶‎📶⬛⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛",
        "⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛‎📶‎📶⬛⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛",
        "⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛‎📶‎📶⬛⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛⬛⬛‎📶⬛⬛",
        "⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛‎📶‎📶⬛⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛⬛⬛‎📶⬛⬛ \n⬛⬛⬛⬛⬛‎📶⬛⬛⬛",
        "⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛‎📶‎📶⬛⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛⬛⬛‎📶⬛⬛ \n⬛⬛⬛⬛⬛‎📶⬛⬛⬛ \n⬛⬛⬛⬛‎📶⬛⬛⬛⬛",
        "⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛‎📶‎📶⬛⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛⬛⬛‎📶⬛⬛ \n⬛⬛⬛⬛⬛‎📶⬛⬛⬛ \n⬛⬛⬛⬛‎📶⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛",
        "⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛‎📶‎📶⬛⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛⬛⬛‎📶⬛⬛ \n⬛⬛⬛⬛⬛‎📶⬛⬛⬛ \n⬛⬛⬛⬛‎📶⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛",
        "⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛‎📶‎📶⬛⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛⬛⬛‎📶⬛⬛ \n⬛⬛⬛⬛⬛‎📶⬛⬛⬛ \n⬛⬛⬛⬛‎📶⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛⬛‎📶‎📶‎📶‎📶‎📶⬛⬛",
        "⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛‎📶‎📶⬛⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛⬛⬛‎📶⬛⬛ \n⬛⬛⬛⬛⬛‎📶⬛⬛⬛ \n⬛⬛⬛⬛‎📶⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛⬛‎📶‎📶‎📶‎📶‎📶⬛⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛",
        "⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛‎📶‎📶⬛⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛⬛⬛‎📶⬛⬛ \n⬛⬛⬛⬛⬛‎📶⬛⬛⬛ \n⬛⬛⬛⬛‎📶⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛⬛‎📶‎📶‎📶‎📶‎📶⬛⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛",
        "⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛‎📶‎📶⬛⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛⬛⬛‎📶⬛⬛ \n⬛⬛⬛⬛⬛‎📶⬛⬛⬛ \n⬛⬛⬛⬛‎📶⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛⬛‎📶‎📶‎📶‎📶‎📶⬛⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛‎📶⬛‎📶⬛⬛⬛‎📶⬛",
        "⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛‎📶‎📶⬛⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛⬛⬛‎📶⬛⬛ \n⬛⬛⬛⬛⬛‎📶⬛⬛⬛ \n⬛⬛⬛⬛‎📶⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛⬛‎📶‎📶‎📶‎📶‎📶⬛⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛‎📶⬛‎📶⬛⬛⬛‎📶⬛ \n⬛⬛‎📶‎📶⬛⬛‎📶⬛⬛",
        "⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛‎📶‎📶⬛⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛⬛⬛‎📶⬛⬛ \n⬛⬛⬛⬛⬛‎📶⬛⬛⬛ \n⬛⬛⬛⬛‎📶⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛⬛‎📶‎📶‎📶‎📶‎📶⬛⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛‎📶⬛‎📶⬛⬛⬛‎📶⬛ \n⬛⬛‎📶‎📶⬛⬛‎📶⬛⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛",
        "⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛‎📶‎📶⬛⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛⬛⬛‎📶⬛⬛ \n⬛⬛⬛⬛⬛‎📶⬛⬛⬛ \n⬛⬛⬛⬛‎📶⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛⬛‎📶‎📶‎📶‎📶‎📶⬛⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛‎📶⬛‎📶⬛⬛⬛‎📶⬛ \n⬛⬛‎📶‎📶⬛⬛‎📶⬛⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶⬛‎📶‎📶‎📶‎📶‎📶⬛",
        "⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛‎📶‎📶⬛⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛⬛⬛‎📶⬛⬛ \n⬛⬛⬛⬛⬛‎📶⬛⬛⬛ \n⬛⬛⬛⬛‎📶⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛⬛‎📶‎📶‎📶‎📶‎📶⬛⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛‎📶⬛‎📶⬛⬛⬛‎📶⬛ \n⬛⬛‎📶‎📶⬛⬛‎📶⬛⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶⬛‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛",
        "⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛‎📶‎📶⬛⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛⬛⬛‎📶⬛⬛ \n⬛⬛⬛⬛⬛‎📶⬛⬛⬛ \n⬛⬛⬛⬛‎📶⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛⬛‎📶‎📶‎📶‎📶‎📶⬛⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛‎📶⬛‎📶⬛⬛⬛‎📶⬛ \n⬛⬛‎📶‎📶⬛⬛‎📶⬛⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶⬛‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n \n My 🇵 🇮 🇳 🇬  Is : Calculating...",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 26])
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    await event.edit(
        f"‎‎‎‎‎‎‎‎‎⬛⬛⬛⬛⬛⬛⬛⬛⬛\n⬛📶📶📶📶📶📶📶⬛\n⬛⬛⬛⬛📶⬛⬛📶⬛\n⬛⬛⬛⬛📶⬛⬛📶⬛\n⬛⬛⬛⬛📶⬛⬛📶⬛\n⬛⬛⬛⬛⬛📶📶⬛⬛\n⬛⬛⬛⬛⬛⬛⬛⬛⬛\n⬛⬛📶📶📶📶📶⬛⬛\n⬛📶⬛⬛⬛⬛⬛📶⬛\n⬛📶⬛⬛⬛⬛⬛📶⬛\n⬛📶⬛⬛⬛⬛⬛📶⬛\n⬛⬛📶📶📶📶📶⬛⬛\n⬛⬛⬛⬛⬛⬛⬛⬛⬛\n⬛📶📶📶📶📶📶📶⬛\n⬛⬛⬛⬛⬛⬛📶⬛⬛\n⬛⬛⬛⬛⬛📶⬛⬛⬛\n⬛⬛⬛⬛📶⬛⬛⬛⬛\n⬛📶📶📶📶📶📶📶⬛\n⬛⬛⬛⬛⬛⬛⬛⬛⬛\n⬛⬛📶📶📶📶📶⬛⬛\n⬛📶⬛⬛⬛⬛⬛📶⬛\n⬛📶⬛⬛⬛⬛⬛📶⬛\n⬛📶⬛📶⬛⬛⬛📶⬛\n⬛⬛📶📶⬛⬛📶⬛⬛\n⬛⬛⬛⬛⬛⬛⬛⬛⬛\n⬛📶⬛📶📶📶📶📶⬛\n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n‎‎‎‎‎‎‎‎‎ \n \n My 🇵 🇮 🇳 🇬  Is : {ms} ms"
    )
