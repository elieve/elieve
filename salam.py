from time import sleep
import asyncio


@ultroid_cmd(pattern="p(?: |$)(.*)")
async def _(event):
    await event.client.send_message(
        event.chat_id,
        "**Assalamualaikum Dulu Biar Sopan**",
        reply_to=event.reply_to_msg_id,
    )
    await event.delete()





@ultroid_cmd(pattern="P(?: |$)(.*)")
async def _(event):
    me = await event.client.get_me()
    xx = await edit_or_reply(event, f"**Haii Salken Saya {me.first_name}**")
    await asyncio.sleep(2)
    await xx.edit("**Assalamualaikum...**")


@ultroid_cmd(pattern="l(?: |$)(.*)")
async def _(event):
    await event.client.send_message(
        event.chat_id, "**Wa'alaikumsalam**", reply_to=event.reply_to_msg_id
    )
    await event.delete()


@ultroid_cmd(pattern="i(?: |$)(.*)")
async def _(event):
    me = await event.client.get_me()
    xx = await edit_or_reply(event, f"**Haii Salken Saya {me.first_name}**")
    await asyncio.sleep(2)
    await xx.edit("**Assalamualaikum**")


@ultroid_cmd(pattern="j(?: |$)(.*)")
async def _(event):
    xx = await edit_or_reply(event, "**JAKA SEMBUNG BAWA GOLOK**")
    await asyncio.sleep(3)
    await xx.edit("**NIMBRUNG GOBLOKK!!!🔥**")


@ultroid_cmd(pattern="k(?: |$)(.*)")
async def _(event):
    me = await event.client.get_me()
    xx = await edit_or_reply(event, f"**Hallo KIMAAKK SAYA {me.first_name}**")
    await asyncio.sleep(2)
    await xx.edit("**LU SEMUA NGENTOT 🔥**")


@ultroid_cmd(pattern="s(?: |$)(.*)")
async def _(event):
    xx = await edit_or_reply(event, "**Salam Dulu Biar Sopan**")
    await asyncio.sleep(2)
    await xx.edit("**السَّلاَمُ عَلَيْكُمْ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ**")


