

from secrets import choice

from telethon.tl.types import InputMessagesFilterVideo, InputMessagesFilterVoice

from userbot.utils import edit_or_reply

@ultroid_cmd(pattern="desahcewe$")
async def _(event):
    xx = await edit_or_reply(event, "`Tunggu Sebentar...`")
    try:
        desahcewe = [
            desah
            async for desah in event.client.iter_messages(
                "@desahancewesangesange", filter=InputMessagesFilterVoice
            )
        ]
        await event.client.send_file(
            event.chat_id, file=choice(desahcewe), reply_to=event.reply_to_msg_id
        )
        await xx.delete()
    except Exception:
        await xx.edit("**Tidak bisa menemukan desahan cewe.**")


@ultroid_cmd(pattern="desahcowo$")
async def _(event):
    xx = await edit_or_reply(event, "`Tunggu Sebentar...`")
    try:
        desahcowo = [
            desah
            async for desah in event.client.iter_messages(
                "@desahancowokkkk", filter=InputMessagesFilterVoice
            )
        ]
        await event.client.send_file(
            event.chat_id, file=choice(desahcowo), reply_to=event.reply_to_msg_id
        )
        await xx.delete()
    except Exception:
        await xx.edit("**Tidak bisa menemukan desahan cowo.**")



@ultroid_cmd(pattern="asupan$")
async def _(event):
    xx = await edit_or_reply(event, "`Tunggu Sebentar...`")
    try:
        asupannya = [
            asupan
            async for asupan in event.client.iter_messages(
                "@tedeasupancache", filter=InputMessagesFilterVideo
            )
        ]
        await event.client.send_file(
            event.chat_id, file=choice(asupannya), reply_to=event.reply_to_msg_id
        )
        await xx.delete()
    except Exception:
        await xx.edit("**Tidak bisa menemukan video asupan.**")
        
@ultroid_cmd(pattern="bokep$")
             

async def _(event):
    xx = await edit_or_reply(event, "`Tunggu Sebentar...`")
    try:
        asupannya = [
            bokep
            async for bokep in event.client.iter_messages(
                "@fakyudurov", filter=InputMessagesFilterVideo
            )
        ]
        await event.client.send_file(
            event.chat_id, file=choice(asupannya), reply_to=event.reply_to_msg_id
        )
        await xx.delete()
    except Exception:
        await xx.edit("**Tidak bisa menemukan video asupan.**")
        
