

from secrets import choice

from telethon.tl.types import InputMessagesFilterVideo, InputMessagesFilterVoice_Note

from userbot.utils import edit_or_reply



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
     
     


@ultroid_cmd(pattern="desahan$")
async def _(event):
    xx = await edit_or_reply(event, "`Tunggu Sebentar...`")
    try:
        desahanya = [
            desahan
            async for desahan in event.client.iter_messages(
                "@desahancewesangesange", filter=InputMessagesFilterVoice_Note
            )
        ]
        await event.client.send_file(
            event.chat_id, file=choice(desahanya), reply_to=event.reply_to_msg_id
        )
        await xx.delete()
    except Exception:
        await xx.edit("**Tidak bisa menemukan vn desah.**")
        
        
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
        
