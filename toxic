#create by Bagaskara
#Yang Copas Doang, Lu kontol

from time import sleep
from telethon.errors.rpcerrorlist import YouBlockedUserError


@ultroid_cmd(outgoing=True, pattern="tiktok(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    d_link = event.pattern_match.group(1)
    if ".com" not in d_link:
        await event.edit("`Mohon Maaf, Saya Membutuhkan Link Video Tiktok Untuk Mendownload Nya`")
    else:
        await event.edit("```Video Sedang Diproses.....```")
    chat = "@ttsavebot"
    async with bot.conversation(chat) as conv:
        try:
            msg_start = await conv.send_message("/start")
            r = await conv.get_response()
            msg = await conv.send_message(d_link)
            details = await conv.get_response()
            video = await conv.get_response()
            """ - don't spam notif - """
            await bot.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await event.edit("**Kesalahan:** `Mohon Buka Blokir` @ttsavebot `Dan Coba Lagi !`")
            return
        await bot.send_file(event.chat_id, video)
        await event.client.delete_messages(conv.chat_id,
                                           [msg_start.id, r.id, msg.id, details.id, video.id])
        await event.delete()


@ultroid_cmd(outgoing=True, pattern='w(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(2)
    await typew.edit("**Woi Jancok !**")
    sleep(2)
    await typew.edit("**Lu Tau ga ? Lu itu Djancok Gausah Sok Keras !**")
    sleep(2)
    await typew.edit("**Muka Lu Kayak Kontol**")


@ultroid_cmd(outgoing=True, pattern='e(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(2)
    await typew.edit("**Huek Cuih !**")
    sleep(2)
    await typew.edit("**Sempak Lu Kagak Pernah Ganti Ya !**")
    sleep(2)
    await typew.edit("**Pantes Kontol Lu Burik**")
    sleep(2)
    await typew.edit("**Order Vcs Aja Gaada Yang Mau Gblk !**")
    sleep(2)
    await typew.edit("**Makanya Jadi Orang Cakepan Dikit Kontol !**")
    sleep(2)
    await typew.edit("**Mending Lu Diem Unggas !!**")


@ultroid_cmd(outgoing=True, pattern='r(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(2)
    await typew.edit("**Jangan kek anjing lu pada !**")
    sleep(2)
    await typew.edit("**Djancok Lu !**")


@ultroid_cmd(outgoing=True, pattern='t(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("**Gua kasih tau nih buat lu bocah kontol !**")
    sleep(3)
    await typew.edit("**kalo ngomongin kasta ama anak WH !**")
    sleep(3)
    await typew.edit("**derajat lu tu ama anak WH beda jauh kontol**")
    sleep(3)
    await typew.edit("**nih ya bapak lu sama Mak lu itu babu gua !**")
    sleep(3)
    await typew.edit("**sering ngemut kontol gua, sering ngelap kaki gua !**")
    sleep(3)
    await typew.edit("**terus ni ya mending lu kerja sama gua !!**")
    sleep(3)
    await typew.edit("**kasiaan bego rumah lu tu dari kayu !!**")
    sleep(3)
    await typew.edit("**bocah micin goblok yg bisa nya main tiktok sama fb !!**")
    sleep(3)
    await typew.edit("**yg kadang kalo sange liat bokep trus coli !!**")
    sleep(3)
    await typew.edit("**gw kasih tau nih ya, keluarga lu udh gua kencingin 7 turunan !!**")
    sleep(3)
    await typew.edit("**emak lu aja pas sange minta ngentot ama gw !!**")
    sleep(3)
    await typew.edit("**bapaklu rela jadi banci demi ngidupin lu biar bisa makan !!**")
    sleep(3)
    await typew.edit("**sedih banget gw liat kehidupan lu yang hina itu !!**")
    sleep(3)
    await typew.edit("**mending sini abang ajarin jadi wibu yang berkelas dek !!**")
    sleep(3)
    await typew.edit("**dan ter keren sejagad telegram !!**")
    sleep(2)
    await typew.edit("**Wibu Human Nih Boss Senggol Dong !!**")
