import asyncio
import random
from . import *
from collections import deque
from telethon.tl.types import Channel, Chat, User
from telethon.tl import functions, types
from telethon.tl.functions.messages import  CheckChatInviteRequest, GetFullChatRequest
from telethon.errors import (ChannelInvalidError, ChannelPrivateError, ChannelPublicGroupNaError, InviteHashEmptyError, InviteHashExpiredError, InviteHashInvalidError)
from telethon.tl.functions.channels import GetFullChannelRequest, GetParticipantsRequest
from time import sleep
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
#create by Bagaskara
#Yang Copas Doang, Lu kontol

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


@ultroid_cmd(pattern="p(?: |$)(.*)")
async def _(event):
    await event.client.send_message(
        event.chat_id,
        "**Assalamualaikum Dulu Biar Sopan**"
    )
    await event.delete()


@ultroid_cmd(pattern="l(?: |$)(.*)")
async def _(event):
    await event.client.send_message(
        event.chat_id, "**Wa'alaikumsalam**"
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




@ultroid_cmd(pattern=r"limit(?: |$)(.*)")
async def _(event):
    await event.edit("`Proses Ngecek Limit akun, Gausah panik lah ngentot!...`")
    async with bot.conversation("@SpamBot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=178220800)
            )
            await conv.send_message("/start")
            response = await response
            await bot.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await event.edit("`Boss! Please Unblock @SpamBot`")
            return
        await event.edit(f"~ {response.message.message}")

@ultroid_cmd(outgoing=True, pattern='r1(?: |$)(.*)')
async def r1(xx):

    await xx.edit("**EH MANUSIA HARAM YANG KERJAANYA REBAHAN, GAUSAH SOK SOK MENILAI HIDUP ORANG DEH LO BANGSAT, LO SENDIRI AJA GA MAMPU BUAT MAKAN GOBLOK KARNA LU GEMBEL KERJA LO PASTI JADI MANUSIA SILVER YANG KAN, NAH MAKANYA DARIPADA KEBANYAKAN NGURUSIN HIDUP ORAMG, MENDING LU CAT BADAN LU BURUAN ABISTU KERJA DAH NGEMIS NGEMIS KALO GAK MATUNG DI PINGGIR JALAN, YAHAHA KAYA BOCAH GA PUNYA KREATIFITAS ATAU MEMANG LO PUNYA KELAINAN DISABILITAS, YANG KELIATAN IDIOT TUU, PASTI JUGA LU LULUSAN SLB YAKAN BAGIAN ORANG ORANG YG KENA GANGGUAN JIWA ATAU PUNYA KELAINAN TU YKANN YAHAHAHAH WAHYOUEEEE🤪🤪**")


@ultroid_cmd(outgoing=True, pattern='r2(?: |$)(.*)')
async def r1(xx):

    await xx.edit("**INI NI KALO ANAK LONTE BERHASIL DI LAHIRKAN ANJING, EMAK LO GABISA GUGURIN DAN LO LAHIR SEBAGAI ANAK HARAM, KASIAN BANGET LO ANJING DARI MASA KANDUNGAN LO DI EMAK LO, UDAH GADA BAPAK, YA IYALAH ANJING ORANG ANAK LONTE, TUBUH LO ITU ADALAH CAMPURAN DARI SEMUA PELANGGAN EMAK LO NGENTOD, NAH KEBETULAN PAS KEBABLASAN EMAK LO LUPA MINUM PIL KB, JADI HAMIL KAN, UDAH LA NGENTOD MENDING LO BUNUH DIRI AJA, GA PANTES BANGET LO DI DUNIA INI ANJING!!!**")


@ultroid_cmd(outgoing=True, pattern='r3(?: |$)(.*)')
async def r1(xx):

    await xx.edit("**WOI ALIANSI SAMPAH, NI DENGERIN YA, GC LO SEPI PASTI KAN, MAKANYA LO NGERUSUH DI GC ORANG TERUS NGAJAK WAR MANA PAKE CUAN LAGI, GUA TAU LU NGAJAK MAIN CUAN PASTI KARNA EKONOMI KELUARGALO LAGI RENDAH ANJING, YA IYALAH BAPAK LO PENGANGGURAN, EH GA DA BAPA KAYANYA, NAH EMAK LO LUMPUH KERJAAN NYA REBAHAN, MAU KEKAMAR MANDI AJA HARUS DI GOTONG KAN, YAHAHA CACAT BANGET ANJING, LO JUGA TERMASUK ORANG CACAT, MANA BIBIR SUMBING TANGAN TREMOR, UDAH COCOK BGT BUAT LO MATI BERDUA EMAK LO YAHAHAH NGENTOD ALIANSI SAMPAH!!!**")


@ultroid_cmd(outgoing=True, pattern='r4(?: |$)(.*)')
async def r1(xx):

    await xx.edit("**MASIH JAMAN NGERUSUH SANA SINI, TERUS PAS DI LADENIN MALAH LARI?, KALO BRANI NGAJAK WAR ORANG YA PAKE KONSEKUENSI LAH TOLOL, KALO CUMA NGATA NGATAIN BEGITU, BOCIL FF JUGA BISA TOLOL, DAN KALO NGAJAK WAR TAPI ALIBI MULU, DI AJAKIN PAKE KONSEKUENSI KAGAK MAO, DI TANTANG MAIN SESI KABUR KABURAN MULU, MENDING LO WAR AJA SAMA BOCAH TK TOLOL, BRANI WAR LGSG AJA KE ALFAM BEGO, ITU JUGA KALO LU BRANI YA, KALO CUPU MAH BUBARIN AJA TU ALIANSI LO YG GA BERGUNA ITU ANIJINGGGGG!!!!**")


@ultroid_cmd(outgoing=True, pattern='r5(?: |$)(.*)')

async def r1(xx):
    await xx.edit("**NIH YA ANAK BABI, GUA KASIH TAU KE LU NIH, LU ITU DISINI CUMA JADI KACUNG GUA NGENTOD, YANG SABAN HARI GUA INJEK INJEK TU BATANG LEHER LU, YG TIAP HARI GUA SURUH SURUH NGELAPIN KAKI GUA, GAUSAH SOK KERAS TOLOL, BAPAK LO LAGI MULUNG NOH DI PEREMPATAN, NUNGGUIN SAMPAH SAMPAH PLASTIK TOLOL, MANA PAKE BAJU PARTAI UDH DEKIL BAT KUMEL ANJING KAYA MASA DEPAN LO YG SURAM, JANGAN BELAGU APA, GUA TAU LO SKOLA CUMA SAMPE LULUSAN SD KAN? YAHAHA KETAWAN BANGET DARI NASIB LU YG MENGENASKAN.**")


@ultroid_cmd(outgoing=True, pattern='r6(?: |$)(.*)')
async def r1(xx):

    await xx.edit("**YA AMPUN, UMUR UDAH TUA MAO MATI UDAH BAU TANAH ANJING, MASIH AJA NYENGGOL SANA SINI, PIKIRIN AJA KISAH HIDUP LU YG KELAM SAMPEL SEKARANG TOLOL, BANTUIN KEK KELUARGA LU YG KEKURANG EKONOMI, NGAPAIN KEK JUAL DIRI KEK, BIAR ADA HASIL BEGO, GUA SEBENARNYA KASIHAN SAMA LU SIH, UDAH JELEK ITEM MUKA UDAH KEK LINTINGAN DAKI BEGITU, BANGSAT BANGET NAJIS DEH GUA AMA LU.**")


@ultroid_cmd(outgoing=True, pattern='r7(?: |$)(.*)')
async def r1(xx):

    await xx.edit("**UDAH LAH, MENDING LO CABUT AJA DARI SINI, SOAL NYA GUA GAMAU ANJING LIAT MANUSIA SAMPAH KAYAK LO ADA DI TELEGRAM, LEBIH TEPAT NYA MENDING LO DOWNLOAD MICHAT NAH ABIS TU LU NGELOTE ANJING, COCOK BANGET SOAL NYA BUAT LO ASU!!!!**")


@ultroid_cmd(outgoing=True, pattern='r8(?: |$)(.*)')
async def r1(xx):

    await xx.edit("**DARI PENILAIAN GUA NI YA, KEBANYAKAN DARI LO ITU CUMA JELEK NYA DOANG ANJING KAGA ADA BAGUS BAGUS NYA LO DI MATA GUA, KEK LIAT TAI BABI GUA KALO LIATIN MUKA LO, YA IYALAH ORANG TERLAHIR DARI EMAK YG PENYAKITAN, MEMEK NYA KENA RAJA SINGAN YAHAHA, TERLALU KASAR GUA, MAAF YA, EH TAPI EMG PANTES LO DI KATA KATAIN KAYA GITU, UDAH COCOK BANGET LO NYUSUL BAPAK LO SANA KE KUBURAN, MANA GA PERNAH DI DOAIN LAGI TU PASTI BAPAK LO YKAN, LAGI DI SIKSA MALAIKAT, GA ADA PENGAMPUNAN GARA GARA LO GA PERNAH DOA, YA GIMANA MAO DOA ORANG SELAMA LO HIDUP KERJAAN NYA CUMA MAEN TELEGRAM DOANG, NGEBACOT DOANG ANJINGG, GA PERNAH NGAJI GA PERNAH BELAJAR AGAMA PASTI, MAKANYA LO TUH MIS ATTITUDE, MIS AKHLAK PULA ADUHHHH ANAK NGENTOD.**")


@ultroid_cmd(outgoing=True, pattern='r9(?: |$)(.*)')
async def r1(xx):

    await xx.edit("**GAUSAH SOK SOK AN NYENGGOL GUA ANJING, TAR GUA AJAKIN SESI, LO LARI, GUA AJAKIN BIKIN KONSEKUENSI LO BANYAK ALIBI, YAHAHA SSMPAH BANGET LO NGENTOD, UDAH LAH MENDING LO PERGI JAUH JAUH DARI MATA GUA, JIJI BAT LIATNYA CUIHHKKKK.**")


@ultroid_cmd(outgoing=True, pattern='r10(?: |$)(.*)')
async def r1(xx):

    await xx.edit("**NIH NIH GUA KASIH BANSOS DEH BUAT LO, LO BELOM PERNAH NGERASAIN MAKAN SARDEN KAN? YAHAHA KASIAN BANGET HIDUP LU YG SABAN HARI MAKAN NASI SAMA GAREM DOANG ANJING, MAKANYA OTAK LO BEGOOO, MANA PASTI SKALINYA MAKAN ENAK, LO CUMA GORENG TELOR AJA KAN, PAKE MICIN YG BANYAK, EMG BOCAH MICIN ANJING, RADA TOLOL SI GUA KALO NGELADENIN LO YG CUMA BISA NGANG NGENG NGONG DOANG ANJING, YA IYA KARNA LO, EMG GA ADA BAKAT APA APA ANJING DI TELEGRAM, CABUT BURUAN CABUT TAR GUA GBAN AMA GUA LO NGENTOD.**")


@ultroid_cmd(outgoing=True, pattern='r11(?: |$)(.*)')
async def r1(xx):

    await xx.edit("**EH BOCAH TOLOL  YANG MUKANYE RATA KEK TEMBOK PENJARA YANG BANYAK KERAK DAKI NARAPIDANA, MULUT LU BAU JIGONG, KUPING CONGEAN KEPALA PITAKAN PANTAT KORENGAN KAKI BUDUKAN KONTOL LO JUGA BISULAN, KALO UDEH BEJAT GAUSAH BEGAJULAN, LU KEBANYAKAN NONTON APLIKASI SI MONTOK SAMBIL COLI DIPOJOKAN DASAR YOHI YOHI YANG OTAK CETEK SKILL PENDEK MUKA GAPTEK YANG KALO MALEM KONTOLNYE DIPAKEIN SOPTEK, EH BOCAH YOHI DEKIL MAKENYE JANGAN KEBANYAKAN LIAT PENTIL, KALO UDEH TOLOL SADAR DIRI, LIAT MUKA LU UDEH KEK KETUMBAR, KETEK LU LDR, DASAR ANAK ANJING PAKIR MISKIN YANG BADANNYE BAU KRIKIL, DASAR ANJING BOCAH INGUSAN YANG KALO LIAT MEMEK LANGSUNG MIMISAN, DIKASIH PAP MUKA LANGSUNG SANGEAN DASAR ABIDIN ANJ,  GINI NIH KLO UDH MISKIN WAWASAN MISKIN PENDIDIKAN MISKIN 7 TURUNAN, EH KONTOL MAKANNYA KLO DISURUH SKLH TUH SKLH TOLOL JGN NGEMIS TRUS, MAK BAPA LU CAPE² NGEMIS KERJAAN DIRUMAH GUA CUMA BUAT PENDIDIKAN LU TOLOL, LU DISURUH SKLH MALAH NGEMIS, NGEGEMBEL, MALAH JADI MANUSIA SILVER LAGI TOLOL, INGET KLO UDH GA BERGUNA DIDUNIA TUH AOWKWWKWIK.**")

@ultroid_cmd(outgoing=True, pattern='r12(?: |$)(.*)')
async def r1(xx):

    await xx.edit("**ini nih anak yang nyembah babi setiap hari yang kerjaan nya cuma makan kotoran gue, eh tolol malu napa udah juga nyembah babi gak punya emak malah sok sokan mau punya cewek, eh malu ama emak lu di neraka tolol, nih ye gue kasih tau ama lu anak hina yang lahir dari rahim anjing lu deger baik baik, orang tolol kek elu di dunia ini kaga di terima tolol wajah kontol yang beruntusan yang mana wajah nya aja kaga simetris kek pantat kuda, mending lu dirumah makan tai aja kerena apa bocah yang gak punya teman kek elu yang mana dakjal aja gak mau temanan ama lu malah di telegram mau sok kerasa tolol, ni ye gue kasih tau ama lu bocah hina nabi aja malu ada pegikut kek elu yang mana elu nya aja murtad malah jadi bocah tolol di telegram, dakjal aja gak mau temanan ama lu kerena lu itu hina tolol, malu kontol ett dah, ni ya orang miskin kek elu yang mana kerjaan nya cuma ngemis di kota Jakarta kota keras mana mampu lu idup di sana, kerena apa bocah kek elu itu di tabok sekali aja langsung mati tolol, ni lagi ye bocah kek elu yang hp aja hp mito malah sok keras kontol, suara lu aja masih kepedem ama suara gue sokakata masi ambrul aduk malah sok mau ngelawan gue, yang mana kodratnya gue itu tuhan lu tolol bocah kontol apa emak lu gua entotin sekalian yekan gua ijek ijek sekalian pepeknya yekan yehh pake sosoan ngtain org, de klo mau reply gua vn video muka jga ga ush vn yehh, najis bet najis gua goblok ngeladenin bocah bocah kek lu mah cwe jga hina bgt lu ngeladenin cwe kek lu mahapasi dek,dede dede ini masi apa pepeknya masi sempit kan jan sampe om entot yakan itu pepek lu itu yakan gua tau pepek lu itu masi sempit kalau gua masukin otong gua ntar berdarah ya ntar takutnya lu hamil yakan kalau ngga ini apa emak lu gua entotin sekalian yekan gua ijek ijek sekalian pepeknya yekan yehh pake sosoan ngtain org, de klo mau reply gua vn video muka jga ga ush vn yehh, najis bet najis gua goblok ngeladenin bocah bocah kek lu mah cwe jga hina bgt lu ngeladenin cwe kek lu mahapasi dek,dede dede ini masi apa pepeknya masi sempit kan jan sampe om entot yakan itu pepek lu itu yakan gua tau pepek lu itu masi sempit kalau gua masukin otong gua ntar berdarah ya ntar takutnya lu hamil yakan kalau ngga ini apa emak lu gua entotin sekalian yekan gua ijek ijek sekalian pepeknya yekan yehh pake sosoan ngtain org, de klo mau reply gua vn video muka jga ga ush vn yehh, najis bet najis gua goblok ngeladenin bocah bocah kek lu mah cwe jga hina bgt lu ngeladenin cwe kek lu mahapasi dek,dede dede ini masi apa pepeknya masi sempit kan jan sampe om entot yakan itu pepek lu itu yakan gua tau pepek lu itu masi sempit kalau gua masukin otong gua ntar berdarah ya ntar takutnya lu hamil yakan kalau ngga ini apa emak lu gua entotin sekalian yekan gua ijek ijek sekalian pepeknya yekan yehh pake sosoan ngtain org, de klo mau reply gua vn video muka jga ga ush vn yehh, najis bet najis gua goblok ngeladenin bocah bocah kek lu mah cwe jga hina bgt lu ngeladenin cwe kek lu mahapasi dek,dede dede ini masi apa pepeknya masi sempit kan jan sampe om entot yakan itu pepek lu itu yakan gua tau pepek lu itu masi sempit kalau gua masukin otong gua ntar berdarah ya ntar takutnya lu hamil yakan kalau ngga ini apa emak lu gua entotin sekalian yekan gua ijek ijek sekalian pepeknya yekan yehh pake sosoan ngtain org, de klo mau reply gua vn video muka jga ga ush vn yehh, najis bet najis gua goblok ngeladenin bocah bocah kek lu mah cwe jga hina bgt lu ngeladenin cwe kek lu mahapasi dek,dede dede ini masi apa pepeknya masi sempit kan jan sampe om entot yakan itu pepek lu itu yakan gua tau pepek lu itu masi sempit kalau gua masukin otong gua ntar berdarah ya ntar takutnya lu hamil yakan kalau ngga ini apa emak lu gua entotin sekalian yekan gua injek injek sekalian pepeknya yekan yehh pake sosoan ngtain org, de klo mau reply gua vn video muka jga ga ush vn yehh, najis bet najis gua goblok ngeladenin bocah bocah kek lu mah cwe jga hina bgt lu ngeladenin cwe kek lu mahapasi dek,dede dede ini masi apa pepeknya masi sempit kan jan sampe om entot yakan itu pepek lu itu yakan gua tau pepek lu itu masi sempit kalau gua masukin otong gua ntar berdarah ya ntar**")






@ultroid_cmd(pattern="o")
async def _(event):
 xx = await edit_or_reply(event, "**HAI JELEK!**")
 await asyncio.sleep(3)
 await xx.edit("**KENALIN NIH**")
 await asyncio.sleep(1)
 await xx.edit("**ORANG PALING CAKEP SE TELEGRAM**")
 await asyncio.sleep(1)
 await xx.edit("**GAK KEK ELU**")
 await asyncio.sleep(1)
 await xx.edit("HEHEHE")
 await asyncio.sleep(1)
 await xx.edit("**Run! Run! Runn!!!**")
 await asyncio.sleep(1)
 await xx.edit("""
 
┏━━┳┓╋╋┏┳━━━┓
┃┏┓┃┗┓┏┛┃┏━━┛
┃┗┛┗┓┗┛┏┫┗━━┓
┃┏━┓┣┓┏┛┃┏━━┛
┃┗━┛┃┃┃╋┃┗━━┓
┗━━━┛┗┛╋┗━━━┛
MWAHH
       
 """)
 await event.delete()

 





async def get_chatinfo(event):
    chat = event.pattern_match.group(1)
    chat_info = None
    if chat:
        try:
            chat = int(chat)
        except ValueError:
            pass
    if not chat:
        if event.reply_to_msg_id:
            replied_msg = await event.get_reply_message()
            if replied_msg.fwd_from and replied_msg.fwd_from.channel_id is not None:
                chat = replied_msg.fwd_from.channel_id
        else:
            chat = event.chat_id
    try:
        chat_info = await event.client(GetFullChatRequest(chat))
    except:
        try:
            chat_info = await event.client(GetFullChannelRequest(chat))
        except ChannelInvalidError:
            await event.reply("`Invalid channel/group`")
            return None
        except ChannelPrivateError:
            await event.reply("`This is a private channel/group or I am banned from there`")
            return None
        except ChannelPublicGroupNaError:
            await event.reply("`Channel or supergroup doesn't exist`")
            return None
        except (TypeError, ValueError) as err:
            await event.reply("`Invalid channel/group`")
            return None
    return chat_info


def make_mention(user):
    if user.username:
        return f"@{user.username}"
    else:
        return inline_mention(user)


def inline_mention(user):
    full_name = user_full_name(user) or "No Name"
    return f"[{full_name}](tg://user?id={user.id})"


def user_full_name(user):
    names = [user.first_name, user.last_name]
    names = [i for i in list(names) if i]
    full_name = ' '.join(names)
    return full_name
 






@borg.on(admin_cmd(pattern=r"inviteall ?(.*)"))
async def get_users(event):   
    sender = await event.get_sender() ; me = await event.client.get_me()
    if not sender.id == me.id:
        rkp = await event.reply("`processing...`")
    else:
     rkp = await event.edit("`processing...`")
    rk1 = await get_chatinfo(event) ; chat = await event.get_chat()
    if event.is_private:
              return await rkp.edit("`Sorry, Can add users here`")    
    s = 0 ; f = 0 ; error = 'None'   
  
    await rkp.edit("**TerminalStatus**\n\n`Collecting Users.......`")
    async for user in event.client.iter_participants(rk1.full_chat.id):
                try:
                    if error.startswith("Too"):
                        return await rkp.edit(f"**Terminal Finished With Error**\n(`May Got Limit Error from telethon Please try agin Later`)\n**Error** : \n`{error}`\n\n• Invited `{s}` people \n• Failed to Invite `{f}` people")
                    await event.client(functions.channels.InviteToChannelRequest(channel=chat,users=[user.id]))
                    s = s + 1                                                    
                    await rkp.edit(f"**Terminal Running...**\n\n• Invited `{s}` people \n• Failed to Invite `{f}` people\n\n**× LastError:** `{error}`")                
                except Exception as e:
                    error = str(e) ; f = f + 1             
    return await rkp.edit(f"**Terminal Finished** \n\n• Successfully Invited `{s}` people \n• failed to invite `{f}` people")

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
        
DEFAULTUSER = "ULTROID"

M = ("___________ \n"
"　　　　　| \n"
"　　　　　| \n"
"　　　　　| \n"
"　　　　　| \n"
"　　　　　| \n"
"　　　　　| \n"
"　／￣￣＼| \n"
"＜ ´･ 　　 |＼ \n"
"　|　３　 | 丶＼ \n"
"＜ 、･　　|　　＼ \n"
"　＼＿＿／∪ _ ∪) \n"
"　　　　　 Ｕ Ｕ\n")
    
C = ("_/﹋\_\n"
"(҂`_´)\n"
f"<,︻╦╤─ ҉ - - - 🤯\n"
"_/﹋\_\n")

A = ("▄███████▄\n"
"█▄█████▄█\n"
"█▼▼▼▼▼█\n"
"██________█▌\n"
"█▲▲▲▲▲█\n"
"█████████\n"
"_████\n")

B = ("┈┈┏━╮╭━┓┈╭━━━━╮\n"
"┈┈┃┏┗┛┓┃╭┫NGOK!!┃\n"
"┈┈╰┓▋▋┏╯╯╰━━━━╯\n"
"┈╭━┻╮╲┗━━━━╮╭╮┈\n"
"┈┃▎▎┃╲╲╲╲╲╲┣━╯┈\n"
"┈╰━┳┻▅╯╲╲╲╲┃┈┈┈\n"
"┈┈┈╰━┳┓┏┳┓┏╯┈┈┈\n"
"┈┈┈┈┈┗┻┛┗┻┛┈┈┈┈\n"
"BABI!!!\n"
"KONTOL!!!🖕🖕\n"
"MUKE LU KEK BABI\n")




D = ("░▐█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█▄\n"
"░███████████████████████ \n"
"░▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓▓◤ \n"
"░▀░▐▓▓▓▓▓▓▌▀█░░░█▀░\n"
"░░░▓▓▓▓▓▓█▄▄▄▄▄█▀░░\n"
"░░█▓▓▓▓▓▌░░░░░░░░░░\n"
"░▐█▓▓▓▓▓░░░░░░░░░░░\n"
"░▐██████▌░░░░░░░░░░\n")

E = ("╥━━━━━━━━╭━━╮━━┳\n"
"╢╭╮╭━━━━━┫┃▋▋━▅┣\n"
"╢┃╰┫┈┈┈┈┈┃┃┈┈╰┫┣\n"
"╢╰━┫┈┈┈┈┈╰╯╰┳━╯┣\n"
"╢┊┊┃┏┳┳━━┓┏┳┫┊┊┣\n"
"╨━━┗┛┗┛━━┗┛┗┛━━┻\n")
F = ("╔┓┏╦━╦┓╔┓╔━━╗\n" 
"║┗┛║┗╣┃║┃║X X║\n"
"║┏┓║┏╣┗╣┗╣╰╯║\n"
"╚┛┗╩━╩━╩━╩━━╝\n")
G = ("▬▬▬.◙.▬▬▬ \n"
"═▂▄▄▓▄▄▂ \n"
"◢◤ █▀▀████▄▄▄▄◢◤ \n"
"█▄ █ █▄ ███▀▀▀▀▀▀▀╬ \n"
"◥█████◤ \n"
"══╩══╩══ \n"
"╬═╬ \n"
"╬═╬ \n"
"╬═╬ \n"
"╬═╬ \n"
"╬═╬ \n"
"╬═╬ \n"
"╬═╬ Hello, My Friend :D \n"
"╬═╬☻/ \n"
"╬═╬/▌ \n"
"╬═╬/ \\n")

H = ("┳┻┳┻╭━━━━╮╱▔▔▔╲\n"
"┻┳┻┳┃╯╯╭━┫▏╰╰╰▕\n"
"┳┻┳┻┃╯╯┃▔╰┓▔▂▔▕╮\n"
"┻┳┻┳╰╮╯┃┈╰┫╰━╯┏╯\n"
"┳┻┳┻┏╯╯┃╭━╯┳━┳╯\n"
"┻┳┻┳╰━┳╯▔╲╱▔╭╮▔╲\n"
"┳┻┳┻┳┻┃┈╲┈╲╱╭╯╮▕\n"
"┻┳┻┳┻┳┃┈▕╲▂╱┈╭╯╱\n"
"┳┻┳┻┳┻┃'''┈┃┈┃┈'''╰╯\n"
"┻┳┻┳┻┏╯▔'''╰┓┣━┳┫\n"
"┳┻┳┻┳╰┳┳┳'''╯┃┈┃┃\n"
"┻┳┻┳┻┳┃┃┃┈'''┃┈┃┃\n"
"┳┻┳┻┳┻┃┃┃'''┊┃┈┃┃\n"
"┻┳┻┳┻┳┃┃┃┈'''┃┈┃┃.\n"
"┳┻┳┻┳┻┣╋┫'''┊┣━╋┫\n"
"┻┳┻┳┻╭╯╰╰-╭╯━╯.''╰╮\n"
"**I Love You 💕** \n")

I = ("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⡿⠋⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⠀⠀⣠⣾⣿⡿⠋⠀⠀⠉⠻⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⠀⠀⣿⣿⣿⠃⠀⠀⣀⡀⠀⢹⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⡄⠀⠙⠻⠋⠀⠀⣸⣿⣿⠀⠀⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⣰⣿⣿⠟⠀⢠⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⡿⠛⠛⠒⠶⠾⢿⣿⣿⣷⣄⣾⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⠀⢰⣿⣿⣷⣶⣦⣼⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⡀⠀⠙⠻⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⢿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⠀⠀⠀⠉⠉⠛⠛⠛⠶⢶⣤⣼⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣦⣤⣤⣄⡀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⠁⠀⣾⣿⣷⡄⠀⢼⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⠀⠀⢿⣿⣿⡿⠀⠈⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⣇⠀⠀⠉⠋⠁⠀⢠⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⠿⢷⣤⣀⣀⣀⣠⣾⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⠀⠀⠀⠈⠉⠉⠛⢻⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⣶⣦⣤⣤⣀⠀⠀⢸⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠹⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⡿⠛⠉⠉⠙⠻⣀⣀⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⠁⠀⣀⡀⠀⠀⠈⢿⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⠀⢸⣿⡇⠀⣷⡀⠘⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⡄⠈⢻⡇⠀⡿⠃⠀⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⣷⣄⢸⡇⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⠀⠉⠉⠑⠒⠲⠿⢿⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⣤⣄⣀⡀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⢺⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⠀⠀⠉⠉⠙⠋⠀⠀⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⣤⣤⣀⣀⡀⠀⠀⣰⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣷⠀⢹⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⠀⠀⠀⠉⠉⠉⠀⠀⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⣶⣤⣤⣀⣀⣀⣀⣰⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⡟⠉⠀⠀⠈⠙⢿⣿⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⠀⢀⣤⡄⠀⡀⠀⢹⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⠀⢸⣿⡇⠀⣿⡄⠈⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⡆⠀⢹⡇⠀⠟⠁⢀⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⣿⣦⣸⡇⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n")

J = ("⣿⣿⣿⣿⣿⣍⠀⠉⠻⠟⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⠓⠀⠀⢒⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⡿⠃⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⣿\n"
"⣿⡿⠋⠋⠀⠀⠀⠀⠀⠀⠈⠙⠻⢿⢿⣿⣿⡿⣿⣿⡟⠋⠀⢀⣩\n"
"⣿⣿⡄⠀⠀⠀⠀⠀⠁⡀⠀⠀⠀⠀⠈⠉⠛⢷⣭⠉⠁⠀⠀⣿⣿\n"
"⣇⣀. INDIA🇮🇳INDIA🇮🇳⠆⠠..⠘⢷⣿⣿⣛⠐⣶⣿⣿\n"
"⣿⣄⠀⣰⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⢀⣠⣿⣿⣿⣾⣿⣿⣿\n"
"⣿⣿⣿⣿⠀⠀⠀⠀⡠⠀⠀⠀⠀⠀⢀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠄⠀⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⣠⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⠀⠀⠂⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣇⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⡆⠀⢀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⣿⣦⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
"**🇮🇳PROUD TO BE AN INDIAN🇮🇳**\n")



K = ("───▄▀▀▀▄▄▄▄▄▄▄▀▀▀▄───\n"
"───█▒▒░░░░░░░░░▒▒█───\n"
"────█░░█░░░░░█░░█────\n"
"─▄▄──█░░░▀█▀░░░█──▄▄─\n"
"█░░█─▀▄░░░░░░░▄▀─█░░█\n"
"█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█\n"
"█░░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░░█\n"
"█░░║║║╠─║─║─║║║║║╠─░░█\n"
"█░░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░░█\n"
"█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n")

L = ("░░░░▓\n"
"░░░▓▓\n"
"░░█▓▓█\n"
"░██▓▓██\n"
"░░██▓▓██\n"
"░░░██▓▓██\n"
"░░░░██▓▓██\n"
"░░░░░██▓▓██\n"
"░░░░██▓▓██\n"
"░░░██▓▓██\n"
"░░██▓▓██\n"
"░██▓▓██\n"
"░░██▓▓██\n"
"░░░██▓▓██\n"
"░░░░██▓▓██\n"
"░░░░░██▓▓██\n"
"░░░░██▓▓██\n"
"░░░██▓▓██\n"
"░░██▓▓██\n"
"░██▓▓██\n"
"░░██▓▓██\n"
"░░░██▓▓██\n"
"░░░░██▓▓██\n"
"░░░░░██▓▓██\n"
"░░░░██▓▓██\n"
"░░░██▓▓██\n"
"░░██▓▓██\n"
"░██▓▓██\n"
"░░██▓▓██\n"
"░░░██▓▓██\n"
"░░░░██▓▓██\n"
"░░░░░██▓▓██\n"
"░░░░██▓▓██\n"
"░░░██▓▓██\n"
"░░██▓▓██\n"
"░██▓▓██\n"
"░░██▓▓██\n"
"░░░██▓▓██\n"
"░░░░██▓▓██\n"
"░░░░░██▓▓██\n"
"░░░░██▓▓██\n"
"░░░██▓▓██\n"
"░░██▓▓██\n"
"░██▓▓██\n"
"░░██▓▓██\n"
"░░░██▓▓██\n"
"░░░░██▓▓██\n"
"░░░░░██▓▓██\n"
"░░░░██▓▓██\n"
"░░░██▓▓██\n"
"░░██▓▓██\n"
"░██▓▓██\n"
"░░██▓▓██\n"
"░░░██▓▓██\n"
"░░░░██▓▓██\n"
"░░░░░██▓▓██\n"
"░░░░██▓▓██\n"
"░░░██▓▓██\n"
"░░██▓▓██\n"
"░██▓▓██\n"
"░░██▓▓██\n"
"░░░██▓▓██\n"
"░░░░██▓▓██\n"
"░░░░░██▓▓██\n"
"░░░░██▓▓██\n"
"░░░██▓▓██\n"
"░░██▓▓██\n"
"░░██▓▓██\n"
"░░██▓▓██\n"
"░░██▓▓██\n"
"░░██▓▓██\n"
"░░██▓▓██\n"
"░░░██▓▓███\n"
"░░░░██▓▓████\n"
"░░░░░██▓▓█████\n"
"░░░░░░██▓▓██████\n"
"░░░░░░███▓▓███████\n"
"░░░░░████▓▓████████\n"
"░░░░█████▓▓█████████\n"
"░░░█████░░░█████●███\n"
"░░████░░░░░░░███████\n"
"░░███░░░░░░░░░██████\n"
"░░██░Ab Mar Bsdk░████\n"
"░░░░░░░░░░░░░░░░███\n"
"░░░░░░░░░░░░░░░░░░░\n")


N = ("────██──────▀▀▀██\n"
"──▄▀█▄▄▄─────▄▀█▄▄▄\n"
"▄▀──█▄▄──────█─█▄▄\n"
"─▄▄▄▀──▀▄───▄▄▄▀──▀▄\n"
"─▀───────▀▀─▀───────▀▀\n🚶🏻‍♂️🚶🏻‍♂️ɮʏɛ ʄʀɨɛռɖֆ..")

O = ("╭━━━┳╮╱╱╭╮╱╭━━━┳━━━╮\n"
"┃╭━╮┃┃╱╭╯╰╮┃╭━╮┃╭━╮┃\n"
"┃╰━━┫╰━╋╮╭╯┃┃╱┃┃╰━━╮\n"
"╰━━╮┃╭╮┣┫┃╱┃┃╱┃┣━━╮┃\n"
"┃╰━╯┃┃┃┃┃╰╮┃╰━╯┃╰━╯┃\n"
"╰━━━┻╯╰┻┻━╯╰━━━┻━━━╯\n")


P = ("███████▄▄███████████▄\n"
"▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n"
"▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n"
"▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n"
"▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n"
"▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n"
"▓▓▓▓▓▓███░░░░░░░░░░░░█\n"
"██████▀░░█░░░░██████▀\n"
"░░░░░░░░░█░░░░█\n"
"░░░░░░░░░░█░░░█\n"
"░░░░░░░░░░░█░░█\n"
"░░░░░░░░░░░█░░█\n"
"░░░░░░░░░░░░▀▀\n")


@ultroid_cmd(pattern=r"monster")
async def bluedevilmonster(monster):
    await eor(monster, A)

@ultroid_cmd(pattern=r"babi")
async def bluedevilpig(pig):
    await eor(pig, B)

@ultroid_cmd(pattern=r"kill")
async def bluedevilkiller(killer):
    await eor(killer, C)

@ultroid_cmd(pattern=r"dor")
async def bluedevilgun(gun):
    await eor(gun, D)

@ultroid_cmd(pattern=r"ajg")
async def bluedevildog(dog):
    await eor(dog, E)    

@ultroid_cmd(pattern=r"hai")
async def bluedevilhello(hello):
    await eor(hello, F)

@ultroid_cmd(pattern=r"hmf")
async def bluedevilhmf(hmf):
    await eor(hmf, G)

@ultroid_cmd(pattern=r"mesum")
async def bluedevilcouple(couple):
    await eor(couple, H)

@ultroid_cmd(pattern=r"sup$")
async def bluedevilsupreme(supreme):
    await eor(supreme, l)

@ultroid_cmd(pattern=r"india")
async def bluedevilindia(india):
    await eor(india, J)

@ultroid_cmd(pattern=r"welkom")
async def bluedevilwelcome(welcome):
    await eor(welcome, K)

@ultroid_cmd(pattern=r"ulo")
async def bluedevilsnake(snake):
    await eor(snake, L) 

@ultroid_cmd(pattern=r"kucing")
async def bluedevilded(cat):
    await eor(cat, M)

@ultroid_cmd(pattern=r"bye")
async def bluedevilbye(e):
    await eor(e, N)

@ultroid_cmd(pattern=r"shitos")
async def bluedevilshitos(e):
    await eor(e, O)

@ultroid_cmd(pattern=r"hu")
async def bluedevildislike(e):
    await eor(e, P)

@ultroid_cmd(pattern="goblok$")
async def snku(ult):
    ult = await eor(ult, "`...`")
    animation_interval = 1
    animation_ttl = range(0, 14)
    await ult.edit("brain")
    animation_chars = [
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n🧠         <(^_^ <)🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n🧠       <(^_^ <)  🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n🧠     <(^_^ <)    🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n🧠   <(^_^ <)      🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n🧠 <(^_^ <)        🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n🧠<(^_^ <)         🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n(> ^_^)>🧠         🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n  (> ^_^)>🧠       🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n    (> ^_^)>🧠     🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n      (> ^_^)>🧠   🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n        (> ^_^)>🧠 🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n          (> ^_^)>🧠🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n           (> ^_^)>🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n           <(^_^ <)🗑",
        "GOOOOBBBBBBLLOOOOOOOOOOOK JANCKOK!!",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await ult.edit(animation_chars[i % 14])




@ultroid_cmd(pattern=f"bombs$")
async def snku(ult):
    ult = await eor(ult, "`...`")
    await ult.edit("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n")
    await asyncio.sleep(0.5)
    await ult.edit("💣💣💣💣 \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n")
    await asyncio.sleep(0.5)
    await ult.edit("▪️▪️▪️▪️ \n💣💣💣💣 \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n")
    await asyncio.sleep(0.5)
    await ult.edit("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n💣💣💣💣 \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n")
    await asyncio.sleep(0.5)
    await ult.edit("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n💣💣💣💣 \n▪️▪️▪️▪️ \n")
    await asyncio.sleep(0.5)
    await ult.edit("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n💣💣💣💣 \n")
    await asyncio.sleep(1)
    await ult.edit("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n💥💥💥💥 \n")
    await asyncio.sleep(0.5)
    await ult.edit("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n💥💥💥💥 \n💥💥💥💥 \n")
    await asyncio.sleep(0.5)
    await ult.edit("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n😵😵😵😵 \n")
    await asyncio.sleep(0.5)
    await ult.edit("`RIP PLOXXX......`")
    await asyncio.sleep(2)


@ultroid_cmd(pattern=r"durov$")
async def snku(ult):
    ult = await eor(ult, "`...`")
    animation_interval = 3
    animation_ttl = range(0, 18)
    await ult.edit("Calling Pavel Durov (ceo of telegram)......")
    animation_chars = [
        "`Connecting To Telegram Headquarters...`",
        "`Call Connected.`",
        "`Telegram: Hello This is Telegram HQ. Who is this?`",
        f"`Me: Yo this is` {DEFAULTUSER} ,`Please Connect me to my lil bro,Pavel Durov `",
        "`User Authorised.`",
        "`Calling Durov `  `At +916969696969`",
        "`Private  Call Connected...`",
        "`Me: Hello Sir, Please Ban This Telegram Account.`",
        "`Durov : May I Know Who Is This?`",
        f"`Me: Yo Brah, I Am` {DEFAULTUSER} ",
        "`Durov : OMG!!! Long time no see, Wassup {DEFAULTUSER}...\nI'll Make Sure That Guy Account Will Get Blocked Within 24Hrs.`",
        "`Me: Thanks, See You Later Brah.`",
        "`Durov : Please Don't Thank Brah, Telegram Is Our's. Just Gimme A Call When You Become Free.`",
        "`Me: Is There Any Issue/Emergency???`",
        "`Durov : Yes Sur, There Is A Bug In Telegram v69.6.9.\nI Am Not Able To Fix It. If Possible, Please Help Fix The Bug.`",
        "`Me: Send Me The App On My Telegram Account, I Will Fix The Bug & Send You.`",
        "`Durov : Sure Sur \nTC Bye Bye :)`",
        "`Private Call Disconnected.`",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await ult.edit(animation_chars[i % 18])


@ultroid_cmd(pattern="wtf$")
async def snku(ult):
    ult = await eor(ult, "`...`")
    animation_interval = 0.8
    animation_ttl = range(0, 5)
    await ult.edit("wtf")
    animation_chars = [
        "What",
        "What The",
        "What The F",
        "What The F Bruh",
        "What The F Bruh\nhttps://telegra.ph//file/f3b760e4a99340d331f9b.jpg",
    ]
    for i in animation_ttl:

        await asyncio.sleep(animation_interval)
        await ult.edit(animation_chars[i % 5])


@ultroid_cmd(pattern="ding$")
async def snku(ult):
    ult = await eor(ult, "`...`")
    animation_interval = 0.3
    animation_ttl = range(0, 30)
    animation_chars = [
        "🔴⬛⬛⬜⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜",
        "⬜⬜⬛⬜⬜\n⬜⬛⬜⬜⬜\n🔴⬜⬜⬜⬜",
        "⬜⬜⬛⬜⬜\n⬜⬜⬛⬜⬜\n⬜⬜🔴⬜⬜",
        "⬜⬜⬛⬜⬜\n⬜⬜⬜⬛⬜\n⬜⬜⬜⬜🔴",
        "⬜⬜⬛⬛🔴\n⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜",
        "⬜⬜⬛⬜⬜\n⬜⬜⬜⬛⬜\n⬜⬜⬜⬜🔴",
        "⬜⬜⬛⬜⬜\n⬜⬜⬛⬜⬜\n⬜⬜🔴⬜⬜",
        "⬜⬜⬛⬜⬜\n⬜⬛⬜⬜⬜\n🔴⬜⬜⬜⬜",
        "🔴⬛⬛⬜⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜",
        "⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜\n⬜  [ULTROID IS BEST](https://github.com/TeamUltroid/Ultroid) ⬜\n⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜",
    ]
    await ult.edit("ding..dong..ding..dong ...")
    await asyncio.sleep(4)
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await ult.edit(animation_chars[i % 10])        


@ultroid_cmd(pattern=f"hipno$")
async def snku(ult):
    ult = await eor(ult, "`>>>`")
    animation_interval = 0.3
    animation_ttl = range(0, 15)
    await ult.edit("hypo....")
    animation_chars = [
        "⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜",
        "⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬛⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜",
        "⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬛⬛⬛⬜⬜\n⬜⬜⬛⬜⬛⬜⬜\n⬜⬜⬛⬛⬛⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜",
        "⬜⬜⬜⬜⬜⬜⬜\n⬜⬛⬛⬛⬛⬛⬜\n⬜⬛⬜⬜⬜⬛⬜\n⬜⬛⬜⬜⬜⬛⬜\n⬜⬛⬜⬜⬜⬛⬜\n⬜⬛⬛⬛⬛⬛⬜\n⬜⬜⬜⬜⬜⬜⬜",
        "⬛⬛⬛⬛⬛⬛⬛\n⬛⬜⬜⬜⬜⬜⬛\n⬛⬜⬜⬜⬜⬜⬛\n⬛⬜⬜⬜⬜⬜⬛\n⬛⬜⬜⬜⬜⬜⬛\n⬛⬜⬜⬜⬜⬜⬛\n⬛⬛⬛⬛⬛⬛⬛",
        "⬛⬜⬛⬜⬛⬜⬛⬜\n⬜⬛⬜⬛⬜⬛⬜⬛\n⬛⬜⬛⬜⬛⬜⬛⬜\n⬜⬛⬜⬛⬜⬛⬜⬛\n⬛⬜⬛⬜⬛⬜⬛⬜\n⬜⬛⬜⬛⬜⬛⬜⬛\n⬛⬜⬛⬜⬛⬜⬛⬜\n⬜⬛⬜⬛⬜⬛⬜⬛",
        "⬜⬛⬜⬛⬜⬛⬜⬛\n⬛⬜⬛⬜⬛⬜⬛⬜\n⬜⬛⬜⬛⬜⬛⬜⬛\n⬛⬜⬛⬜⬛⬜⬛⬜\n⬜⬛⬜⬛⬜⬛⬜⬛\n⬛⬜⬛⬜⬛⬜⬛⬜\n⬜⬛⬜⬛⬜⬛⬜⬛\n⬛⬜⬛⬜⬛⬜⬛⬜",
        "⬜⬜⬜⬜⬜⬜⬜\n⬜⬛⬛⬛⬛⬛⬜\n⬜⬛⬜⬜⬜⬛⬜\n⬜⬛⬜⬛⬜⬛⬜\n⬜⬛⬜⬜⬜⬛⬜\n⬜⬛⬛⬛⬛⬛⬜\n⬜⬜⬜⬜⬜⬜⬜",
        "⬛⬛⬛⬛⬛⬛⬛\n⬛⬜⬜⬜⬜⬜⬛\n⬛⬜⬛⬛⬛⬜⬛\n⬛⬜⬛⬜⬛⬜⬛\n⬛⬜⬛⬛⬛⬜⬛\n⬛⬜⬜⬜⬜⬜⬛\n⬛⬛⬛⬛⬛⬛⬛",
        "⬜⬜⬜⬜⬜⬜⬜\n⬜⬛⬛⬛⬛⬛⬜\n⬜⬛⬜⬜⬜⬛⬜\n⬜⬛⬜⬛⬜⬛⬜\n⬜⬛⬜⬜⬜⬛⬜\n⬜⬛⬛⬛⬛⬛⬜\n⬜⬜⬜⬜⬜⬜⬜",
        "⬛⬛⬛⬛⬛⬛⬛\n⬛⬜⬜⬜⬜⬜⬛\n⬛⬜⬛⬛⬛⬜⬛\n⬛⬜⬛⬜⬛⬜⬛\n⬛⬜⬛⬛⬛⬜⬛\n⬛⬜⬜⬜⬜⬜⬛\n⬛⬛⬛⬛⬛⬛⬛",
        "⬜⬜⬜⬜⬜⬜⬜\n⬜⬛⬛⬛⬛⬛⬜\n⬜⬛⬜⬜⬜⬛⬜\n⬜⬛⬜⬛⬜⬛⬜\n⬜⬛⬜⬜⬜⬛⬜\n⬜⬛⬛⬛⬛⬛⬜\n⬜⬜⬜⬜⬜⬜⬜",
        "⬛⬛⬛⬛⬛\n⬛⬜⬜⬜⬛\n⬛⬜⬛⬜⬛\n⬛⬜⬜⬜⬛\n⬛⬛⬛⬛⬛",
        "⬜⬜⬜\n⬜⬛⬜\n⬜⬜⬜",
        "[👉🔴👈])",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await ult.edit(animation_chars[i % 15])

@ultroid_cmd(pattern="gangasta$")
async def snku(ult):
    ult = await eor(ult, "EVERyBOdy")
    await asyncio.sleep(0.3)
    await ult.edit("iZ")
    await asyncio.sleep(0.2)
    await ult.edit("GangSTur")
    await asyncio.sleep(0.5)
    await ult.edit("UNtIL ")
    await asyncio.sleep(0.2)
    await ult.edit("I")
    await asyncio.sleep(0.3)
    await ult.edit("ArRivE")
    await asyncio.sleep(0.3)
    await ult.edit("🔥🔥🔥")
    await asyncio.sleep(0.3)
    await ult.edit("EVERyBOdy iZ GangSTur UNtIL I ArRivE 🔥🔥🔥")


@ultroid_cmd(pattern=f"cas$")
async def snku(e):
    txt = (
        e.text[10:]
        + "\n\n`Tesla Wireless Charging (beta) Started...\nDevice Detected: Nokia 1100\nBattery Percentage:` "
    )
    e = await eor(e, "`===`")
    j = 10
    k = j
    for j in range(j):
        await e.edit(txt + str(k))
        k = k + 10
        await asyncio.sleep(1)
    await asyncio.sleep(1)
    await e.edit(
        "`Tesla Wireless Charging (beta) Completed...\nDevice Detected: Nokia 1100 (Space Grey Varient)\nBattery Percentage:` [100%](https://telegra.ph/file/a45aa7450c8eefed599d9.mp4) ",
        link_preview=True,
    )


@ultroid_cmd(pattern=r"lol$")
async def snku(ult):
    ult = await eor(ult, "`...`")
    deq = deque(list("😂🤣😂🤣😂🤣"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await ult.edit("".join(deq))
        deq.rotate(1)


@ultroid_cmd(pattern=r"sedih$")
async def snku(ult):
    ult = await eor(ult, "`...`")
    deq = deque(list("😁☹️😁☹️😁☹️😁"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await ult.edit("".join(deq))
        deq.rotate(1)


@ultroid_cmd(pattern="clock$")
async def snku(ult):
    ult = await eor(ult, "`...`")
    deq = deque(list("🕙🕘🕗🕖🕕🕔🕓🕒🕑🕐🕛"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await ult.edit("".join(deq))
        deq.rotate(1)


@ultroid_cmd(pattern=r"muah$")
async def snku(ult):
    ult = await eor(ult, "`=>>`")
    deq = deque(list("😗😙😚😚😘"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await ult.edit("".join(deq))
        deq.rotate(1)


@ultroid_cmd(pattern="love$")
async def snku(ult):
    ult = await eor(ult, "`...`")
    deq = deque(list("❤️🧡💛💚💙💜🖤"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await ult.edit("".join(deq))
        deq.rotate(1)


@ultroid_cmd(pattern="gym$")
async def snku(ult):
    ult = await eor(ult, "`...`")
    deq = deque(list("🏃‍🏋‍🤸‍🏃‍🏋‍🤸‍🏃‍🏋‍🤸‍"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await ult.edit("".join(deq))
        deq.rotate(1)


@ultroid_cmd(pattern="bumi$")
async def snku(ult):
    ult = await eor(ult, "~~~")
    deq = deque(list("🌏🌍🌎🌎🌍🌏🌍🌎"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await ult.edit("".join(deq))
        deq.rotate(1)


@ultroid_cmd(pattern="moon$")
async def snku(ult):
    ult = await eor(ult, "@_@")
    deq = deque(list("🌗🌘🌑🌒🌓🌔🌕🌖"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await ult.edit("".join(deq))
        deq.rotate(1)


@ultroid_cmd(pattern="permen$")
async def snku(ult):
    ult = await eor(ult, "...")
    deq = deque(list("🍦🍧🍩🍪🎂🍰🧁🍫🍬🍭"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await ult.edit("".join(deq))
        deq.rotate(1)


@ultroid_cmd(pattern="smoon$")
async def snku(ult):
    animation_interval = 0.1
    animation_ttl = range(0, 101)
    ult = await eor(ult, "smoon..")
    animation_chars = [
        "🌗🌗🌗🌗🌗\n🌓🌓🌓🌓🌓\n🌗🌗🌗🌗🌗\n🌓🌓🌓🌓🌓\n🌗🌗🌗🌗🌗",
        "🌘🌘🌘🌘🌘\n🌔🌔🌔🌔🌔\n🌘🌘🌘🌘🌘\n🌔🌔🌔🌔🌔\n🌘🌘🌘🌘🌘",
        "🌑🌑🌑🌑🌑\n🌕🌕🌕🌕🌕\n🌑🌑🌑🌑🌑\n🌕🌕🌕🌕🌕\n🌑🌑🌑🌑🌑",
        "🌒🌒🌒🌒🌒\n🌖🌖🌖🌖🌖\n🌒🌒🌒🌒🌒\n🌖🌖🌖🌖🌖\n🌒🌒🌒🌒🌒",
        "🌓🌓🌓🌓🌓\n🌗🌗🌗🌗🌗\n🌓🌓🌓🌓🌓\n🌗🌗🌗🌗🌗\n🌓🌓🌓🌓🌓",
        "🌔🌔🌔🌔🌔\n🌘🌘🌘🌘🌘\n🌔🌔🌔🌔🌔\n🌘🌘🌘🌘🌘\n🌔🌔🌔🌔🌔",
        "🌕🌕🌕🌕🌕\n🌑🌑🌑🌑🌑\n🌕🌕🌕🌕🌕\n🌑🌑🌑🌑🌑\n🌕🌕🌕🌕🌕",
        "🌖🌖🌖🌖🌖\n🌒🌒🌒🌒🌒\n🌖🌖🌖🌖🌖\n🌒🌒🌒🌒🌒\n🌖🌖🌖🌖🌖",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await ult.edit(animation_chars[i % 8])


@ultroid_cmd(pattern="tmoon$")
async def snku(ult):
    animation_interval = 0.1
    animation_ttl = range(0, 117)
    ult = await eor(ult, "tmoon")
    animation_chars = [
        "🌗",
        "🌘",
        "🌑",
        "🌒",
        "🌓",
        "🌔",
        "🌕",
        "🌖",
        "🌗",
        "🌘",
        "🌑",
        "🌒",
        "🌓",
        "🌔",
        "🌕",
        "🌖",
        "🌗",
        "🌘",
        "🌑",
        "🌒",
        "🌓",
        "🌔",
        "🌕",
        "🌖",
        "🌗",
        "🌘",
        "🌑",
        "🌒",
        "🌓",
        "🌔",
        "🌕",
        "🌖",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await ult.edit(animation_chars[i % 32])


@ultroid_cmd(pattern="badut$")
async def snku(ult):
    ult = await eor(ult, "....")
    animation_interval = 0.50
    animation_ttl = range(0, 16)
    animation_chars = [
        "🤡️",
        "🤡🤡",
        "🤡🤡🤡",
        "🤡🤡🤡🤡",
        "🤡🤡🤡🤡🤡",
        "🤡🤡🤡🤡🤡🤡",
        "🤡🤡🤡🤡🤡",
        "🤡🤡🤡🤡",
        "🤡🤡🤡",
        "🤡🤡",
        "🤡",
        "You",
        "You Are",
        "You Are A",
        "You Are A Clown 🤡",
    ]

    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await ult.edit(animation_chars[i % 16])


@ultroid_cmd(pattern="human$")
async def snku(ult):
    animation_interval = 0.5
    animation_ttl = range(16)
    ult = await eor(ult, "human...")
    animation_chars = [
        "⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n🔲🔲🔲🔲🔲🔲🔲",
        "⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛🚗\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n🔲🔲🔲🔲🔲🔲🔲",
        "⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛🚗⬛\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n🔲🔲🔲🔲🔲🔲🔲",
        "⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛🚗⬛⬛\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n🔲🔲🔲🔲🔲🔲🔲",
        "⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛🚗⬛⬛⬛\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n🔲🔲🔲🔲🔲🔲🔲",
        "⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛🚗⬛⬛⬛⬛\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n🔲🔲🔲🔲🔲🔲🔲",
        "⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛🚗⬛⬛⬛⬛⬛\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n🔲🔲🔲🔲🔲🔲🔲",
        "⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n🚗⬛⬛⬛⬛⬛⬛\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n🔲🔲🔲🔲🔲🔲🔲",
        "⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n🔲🔲🔲🔲🔲🔲🔲",
        "⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬜⬜⬜😊⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n🔲🔲🔲🔲🔲🔲🔲",
        "⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛😊⬛⬛⬛\n⬛⬜⬜⬜⬜⬜⬛\n⬛⬛⬛⬜⬛⬛⬛\n⬛⬛⬜⬛⬜⬛⬛\n⬛⬛⬜⬛⬜⬛⬛\n⬛⬛⬜⬛⬜⬛⬛\n🔲🔲🔲🔲🔲🔲🔲",
        "⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛😊⬛⬛⬛\n⬛⬜⬜⬜⬜⬜⬛\n⬛⬛⬛⬜⬛⬛⬛\n⬛⬛⬜⬛⬜⬛⬛\n⬛⬛⬜⬛⬛⬜⬛\n⬛⬛⬜⬛⬛⬛⬛\n🔲🔲🔲🔲🔲🔲🔲",
        "⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛😊⬛⬛⬛\n⬛⬜⬜⬜⬜⬜⬛\n⬛⬛⬛⬜⬛⬛⬛\n⬛⬛⬜⬛⬜⬛⬛\n⬛⬜⬛⬛⬛⬜⬛\n⬛⬛⬛⬛⬛⬛⬛\n🔲🔲🔲🔲🔲🔲🔲",
        "⬛⬛⬛⬛⬛⬛⬛\n⬛⬜⬛😊⬛⬜⬛\n⬛⬛⬜⬜⬜⬛⬛\n⬛⬛⬛⬜⬛⬛⬛\n⬛⬛⬜⬛⬜⬛⬛\n⬛⬜⬛⬛⬛⬜⬛\n⬛⬛⬛⬛⬛⬛⬛\n🔲🔲🔲🔲🔲🔲🔲",
        "⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛😊⬛⬛⬛\n⬛⬛⬜⬜⬜⬛⬛\n⬛⬜⬛⬜⬛⬜⬛\n⬛⬛⬜⬛⬜⬛⬛\n⬛⬛⬜⬛⬜⬛⬛\n⬛⬛⬜⬛⬜⬛⬛\n🔲🔲🔲🔲🔲🔲🔲",
        "⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬜⬜⬜😊⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n🔲🔲🔲🔲🔲🔲🔲",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await ult.edit(animation_chars[i % 16])


@ultroid_cmd(pattern=f"music$")
async def snku(ult):
    animation_interval = 1.5
    animation_ttl = range(11)
    ult = await eor(ult, "starting player...")
    animation_chars = [
        "⬤⬤⬤ 81% ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀`✖️`\n\n⠀⠀⠀⠀⠀[Music Player](t.me/TeamUltroid)\n\n⠀⠀⠀⠀**Now Playing:shape of u**\n\n**00:00** ▱▱▱▱▱▱▱▱▱▱ **00:10**\n\n⠀⠀⠀⠀⠀`🔂` `⏮️` `⏪️` `▶️` `⏩️` `⏭️`\n\n**⠀Next Song:** __Alan Walker - Alone.__\n\n⠀⠀⠀⠀**⠀Device: I Fone XXX**",
        "⬤⬤⬤ 81% ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀`✖️`\n\n⠀⠀⠀⠀⠀[Music Player](t.me/TeamUltroid)\n\n⠀⠀⠀⠀**Now Playing:shape of u**\n\n**00:01** ▰▱▱▱▱▱▱▱▱▱ **00:10**\n\n⠀⠀⠀⠀⠀`🔂` `⏮️` `⏪️` `⏸️` `⏩️` `⏭️`\n\n**⠀Next Song:** __Alan Walker - Alone.__\n\n⠀⠀⠀⠀**⠀Device: Ifone XXX**",
        "⬤⬤⬤ 81% ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀`✖️`\n\n⠀⠀⠀⠀⠀[Music Player](t.me/TeamUltroid)\n\n⠀⠀⠀⠀**Now Playing:shape of u**\n\n**00:02** ▰▰▱▱▱▱▱▱▱▱ **00:10**\n\n⠀⠀⠀⠀⠀`🔂` `⏮️` `⏪️` `⏸️` `⏩️` `⏭️`\n\n**⠀Next Song:** __Alan Walker - Alone.__\n\n⠀⠀⠀⠀**⠀Device: Ifone XXX**",
        "⬤⬤⬤ 81% ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀`✖️`\n\n⠀⠀⠀⠀⠀[Music Player](t.me/TeamUltroid)\n\n⠀⠀⠀⠀**Now Playing:shape of u**\n\n**00:03** ▰▰▰▱▱▱▱▱▱▱ **00:10**\n\n⠀⠀⠀⠀⠀`🔂` `⏮️` `⏪️` `⏸️` `⏩️` `⏭️`\n\n**⠀Next Song:** __Alan Walker - Alone.__\n\n⠀⠀⠀⠀**⠀Device: Ifone XXX**",
        "⬤⬤◯ 80% ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀`✖️`\n\n⠀⠀⠀⠀⠀[Music Player](t.me/TeamUltroid)\n\n⠀⠀⠀⠀**Now Playing:shape of u**\n\n**00:04** ▰▰▰▰▱▱▱▱▱▱ **00:10**\n\n⠀⠀⠀⠀⠀`🔂` `⏮️` `⏪️` `⏸️` `⏩️` `⏭️`\n\n**⠀Next Song:** __Alan Walker - Alone.__\n\n⠀⠀⠀⠀**⠀Device: Ifone XXX**",
        "⬤⬤◯ 80% ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀`✖️`\n\n⠀⠀⠀⠀⠀[Music Player](t.me/TeamUltroid)\n\n⠀⠀⠀⠀**Now Playing:shape of u**\n\n**00:05** ▰▰▰▰▱▱▱▱▱▱ **00:10**\n\n⠀⠀⠀⠀⠀`🔂` `⏮️` `⏪️` `⏸️` `⏩️` `⏭️`\n\n**⠀Next Song:** __Alan Walker - Alone.__\n\n⠀⠀⠀⠀**⠀Device: Ifone XXX**",
        "⬤⬤◯ 80% ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀`✖️`\n\n⠀⠀⠀⠀⠀[Music Player](t.me/TeamUltroid)\n\n⠀⠀⠀⠀**Now Playing:shape of u**\n\n**00:06** ▰▰▰▰▰▰▱▱▱▱ **00:10**\n\n⠀⠀⠀⠀⠀`🔂` `⏮️` `⏪️` `⏸️` `⏩️` `⏭️`\n\n**⠀Next Song:** __Alan Walker - Alone.__\n\n⠀⠀⠀⠀**⠀Device: Ifone XXX**",
        "⬤⬤◯ 80% ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀`✖️`\n\n⠀⠀⠀⠀⠀[Music Player](t.me/TeamUltroid)\n\n⠀⠀⠀⠀**Now Playing:shape of u**\n\n**00:07** ▰▰▰▰▰▰▰▱▱▱ **00:10**\n\n⠀⠀⠀⠀⠀`🔂` `⏮️` `⏪️` `⏸️` `⏩️` `⏭️`\n\n**⠀Next Song:** __Alan Walker - Alone.__\n\n⠀⠀⠀⠀**⠀Device: Ifone XXX**",
        "⬤⬤◯ 80% ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀`✖️`\n\n⠀⠀⠀⠀⠀[Music Player](t.me/TeamUltroid)\n\n⠀⠀⠀⠀**Now Playing:shape of u**\n\n**00:08** ▰▰▰▰▰▰▰▰▱▱ **00:10**\n\n⠀⠀⠀⠀⠀`🔂` `⏮️` `⏪️` `⏸️` `⏩️` `⏭️`\n\n**⠀Next Song:** __Alan Walker - Alone.__\n\n⠀⠀⠀⠀**⠀Device: Ifone XXX**",
        "⬤⬤◯ 80% ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀`✖️`\n\n⠀⠀⠀⠀⠀[Music Player](t.me/TeamUltroid)\n\n⠀⠀⠀⠀**Now Playing:shape of u**\n\n**00:09** ▰▰▰▰▰▰▰▰▰▱ **00:10**\n\n⠀⠀⠀⠀⠀`🔂` `⏮️` `⏪️` `⏸️` `⏩️` `⏭️`\n\n**⠀Next Song:** __Alan Walker - Alone.__\n\n⠀⠀⠀⠀**⠀Device: Ifone XXX**",
        "⬤⬤◯ 80% ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀`✖️`\n\n⠀⠀⠀⠀⠀[Music Player](t.me/TeamUltroid)\n\n⠀⠀⠀⠀**Now Playing:shape of u**\n\n**00:10** ▰▰▰▰▰▰▰▰▰▰ **00:10**\n\n⠀⠀⠀⠀⠀`🔂` `⏮️` `⏪️` `⏺️` `⏩️` `⏭️`\n\n**⠀Next Song:** __Alan Walker - Alone.__\n\n⠀⠀⠀⠀**⠀Device: Ifone XXX**",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await ult.edit(animation_chars[i % 11])


@ultroid_cmd(pattern=f"squ$")
async def snku(ult):
    ult = await eor(
        ult, "╔═══════════════════╗ \n  \n╚═══════════════════╝"
    )
    await asyncio.sleep(1)
    await ult.edit("╔═══════════════════╗ \n \t░ \n╚═══════════════════╝")
    await asyncio.sleep(1)
    await ult.edit("╔═══════════════════╗ \n ░ \t░ \n╚═══════════════════╝")
    await asyncio.sleep(1)
    await ult.edit("╔═══════════════════╗ \n ░ ░ ░ \n╚═══════════════════╝")
    await asyncio.sleep(1)
    await ult.edit("╔═══════════════════╗ \n ░ ░ ░ ░ \n╚═══════════════════╝")
    await asyncio.sleep(1)
    await ult.edit("╔═══════════════════╗ \n ░ ░ ░ ░ ░ \n╚═══════════════════╝")
    await asyncio.sleep(1)
    await ult.edit("╔═══════════════════╗ \n ░ ░ ░ ░ ░ ░ \n╚═══════════════════╝")
    await asyncio.sleep(1)
    await ult.edit("╔═══════════════════╗ \n ░ ░ ░ ░ ░ ░ ░ \n╚═══════════════════╝")
    await asyncio.sleep(1)
    await ult.edit("╔═══════════════════╗ \n ░ ░ ░ ░ ░ ░ ░ ░ \n╚═══════════════════╝")
    await asyncio.sleep(1)
    await ult.edit(
        "╔═══════════════════╗ \n ░ ░ ░ ░ ░ ░ ░ ░ ░ \n╚═══════════════════╝"
    )
    await asyncio.sleep(1)
    await ult.edit(
        "╔═══════════════════╗ \n ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ \n╚═══════════════════╝"
    )
    await asyncio.sleep(1)
    await ult.edit(
        "╔═══════════════════╗ \n ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ \n╚═══════════════════╝"
    )
    await asyncio.sleep(1)
    await ult.edit(
        "╔═══════════════════╗ \n ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ \n╚═══════════════════╝"
    )
    await asyncio.sleep(1)
    await ult.edit(
        "╔═══════════════════╗ \n ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ \n╚═══════════════════╝"
    )
    await asyncio.sleep(1)
    await ult.edit(
        "╔═══════════════════╗ \n ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ \n╚═══════════════════╝"
    )
    await asyncio.sleep(6)


@ultroid_cmd(pattern="kiler( (.*)|$)")
async def snku(ult):
    name = ult.pattern_match.group(1)
    if not name:
        name = "die"
    animation_interval = 0.7
    animation_ttl = range(8)
    ult = await eor(ult, f"**Ready Commando **__{DEFAULTUSER}....")
    animation_chars = [
        "Ｆｉｉｉｉｉｒｅ",
        f"__**Commando **__{DEFAULTUSER}          \n\n_/﹋\_\n (҂`_´)\n <,︻╦╤─ ҉ - \n _/﹋\_\n",
        f"__**Commando **__{DEFAULTUSER}          \n\n_/﹋\_\n (҂`_´)\n  <,︻╦╤─ ҉ - -\n _/﹋\_\n",
        f"__**Commando **__{DEFAULTUSER}          \n\n_/﹋\_\n (҂`_´)\n <,︻╦╤─ ҉ - - -\n _/﹋\_\n",
        f"__**Commando **__{DEFAULTUSER}          \n\n_/﹋\_\n (҂`_´)\n<,︻╦╤─ ҉ - -\n _/﹋\_\n",
        f"__**Commando **__{DEFAULTUSER}          \n\n_/﹋\_\n (҂`_´)\n <,︻╦╤─ ҉ - \n _/﹋\_\n",
        f"__**Commando **__{DEFAULTUSER}         \n\n_/﹋\_\n (҂`_´)\n  <,︻╦╤─ ҉ - -\n _/﹋\_\n",
        f"__**Commando **__{DEFAULTUSER}          \n\n_/﹋\_\n (҂`_´)\n <,︻╦╤─ ҉ - - - {name}\n _/﹋\_\n",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await ult.edit(animation_chars[i % 8])


@ultroid_cmd(pattern="star$")
async def snku(ult):
    ult = await eor(ult, "...")
    deq = deque(list("🦋✨🦋✨🦋✨🦋✨"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await ult.edit("".join(deq))
        deq.rotate(1)


@ultroid_cmd(pattern="boxs")
async def snku(ult):
    ult = await eor(ult, "...")
    deq = deque(list("🟥🟧🟨🟩🟦🟪🟫⬛⬜"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await ult.edit("".join(deq))
        deq.rotate(1)


@ultroid_cmd(pattern="rain$")
async def snku(ult):
    ult = await eor(ult, "...")
    deq = deque(list("🌬☁️🌩🌨🌧🌦🌥⛅🌤"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await ult.edit("".join(deq))
        deq.rotate(1)


@ultroid_cmd(pattern="clol$")
async def snku(ult):
    ult = await eor(ult, "...")
    deq = deque(list("🤔🧐🤨🤔🧐🤨"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await ult.edit("".join(deq))
        deq.rotate(1)


@ultroid_cmd(pattern="odra$")
async def snku(ult):
    ult = await eor(ult, "...")
    deq = deque(list("🚶🏃🚶🏃🚶🏃🚶🏃"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await ult.edit("".join(deq))
        deq.rotate(1)


@ultroid_cmd(pattern="dump ?(.*)")
async def snku(ult):
    message = await eor(ult, "...")
    try:
        obj = message.pattern_match.group(1)
        if len(obj) != 3:
            raise IndexError
        inp = " ".join(obj)
    except IndexError:
        inp = "🥞 🎂 🍫"
    u, t, g, o, s, n = inp.split(), "🗑", "<(^_^ <)", "(> ^_^)>", "⠀ ", "\n"
    h = [(u[0], u[1], u[2]), (u[0], u[1], ""), (u[0], "", "")]
    for something in reversed(
        [
            y
            for y in (
                [
                    "".join(x)
                    for x in (
                        f + (s, g, s + s * f.count(""), t),
                        f + (g, s * 2 + s * f.count(""), t),
                        f[:i] + (o, f[i], s * 2 + s * f.count(""), t),
                        f[:i] + (s + s * f.count(""), o, f[i], s, t),
                        f[:i] + (s * 2 + s * f.count(""), o, f[i], t),
                        f[:i] + (s * 3 + s * f.count(""), o, t),
                        f[:i] + (s * 3 + s * f.count(""), g, t),
                    )
                ]
                for i, f in enumerate(reversed(h))
            )
        ]
    ):
        for something_else in something:
            await asyncio.sleep(0.3)
            try:
                await message.edit(something_else)
            except errors.MessageIdInvalidError:
                return


@ultroid_cmd(pattern="fleaveme$")
async def snku(ult):
    animation_interval = 1
    animation_ttl = range(0, 10)
    animation_chars = [
        "⬛⬛⬛\n⬛⬛⬛\n⬛⬛⬛",
        "⬛⬛⬛\n⬛🔄⬛\n⬛⬛⬛",
        "⬛⬆️⬛\n⬛🔄⬛\n⬛⬛⬛",
        "⬛⬆️↗️\n⬛🔄⬛\n⬛⬛⬛",
        "⬛⬆️↗️\n⬛🔄➡️\n⬛⬛⬛",
        "⬛⬆️↗️\n⬛🔄➡️\n⬛⬛↘️",
        "⬛⬆️↗️\n⬛🔄➡️\n⬛⬇️↘️",
        "⬛⬆️↗️\n⬛🔄➡️\n↙️⬇️↘️",
        "⬛⬆️↗️\n⬅️🔄➡️\n↙️⬇️↘️",
        "↖️⬆️↗️\n⬅️🔄➡️\n↙️⬇️↘️",
    ]
    ult = await eor(ult, "fleaveme....")
    await asyncio.sleep(2)
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await ult.edit(animation_chars[i % 10])


@ultroid_cmd(pattern="lup")
async def snku(ult):
    animation_interval = 0.5
    animation_ttl = range(0, 70)
    ult = await eor(ult, "loveu")
    animation_chars = [
        "😀",
        "👩‍🎨",
        "😁",
        "😂",
        "🤣",
        "😃",
        "😄",
        "😅",
        "😊",
        "☺",
        "🙂",
        "🤔",
        "🤨",
        "😐",
        "😑",
        "😶",
        "😣",
        "😥",
        "😮",
        "🤐",
        "😯",
        "😴",
        "😔",
        "😕",
        "☹",
        "🙁",
        "😖",
        "😞",
        "😟",
        "😢",
        "😭",
        "🤯",
        "💔",
        "❤",
        "i Love You❤",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await ult.edit(animation_chars[i % 35])


@ultroid_cmd(pattern="pesawat")
async def snku(ult):
    ult = await eor(ult, "✈-------------")
    await ult.edit("-✈------------")
    await ult.edit("--✈-----------")
    await ult.edit("---✈----------")
    await ult.edit("----✈---------")
    await ult.edit("-----✈--------")
    await ult.edit("------✈-------")
    await ult.edit("-------✈------")
    await ult.edit("--------✈-----")
    await ult.edit("---------✈----")
    await ult.edit("----------✈---")
    await ult.edit("-----------✈--")
    await ult.edit("------------✈-")
    await ult.edit("-------------✈")
    await asyncio.sleep(3)
    await ult.delete()


@ultroid_cmd(pattern="police")
async def snku(ult):
    animation_interval = 0.3
    animation_ttl = range(0, 12)
    ult = await eor(ult, "Police")
    animation_chars = [
        "🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵",
        "🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴",
        "🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵",
        "🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴",
        "🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵",
        "🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴",
        "🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵",
        "🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴",
        "🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵",
        "🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴",
        "🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵",
        f"{DEFAULTUSER} **Police iz Here**",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await ult.edit(animation_chars[i % 12])


@ultroid_cmd(pattern=f"jio$")
async def snku(ult):
    animation_interval = 1
    animation_ttl = range(0, 19)
    ult = await eor(ult, "jio network boosting...")
    animation_chars = [
        "`Connecting To JIO NETWORK ....`",
        "`█ ▇ ▆ ▅ ▄ ▂ ▁`",
        "`▒ ▇ ▆ ▅ ▄ ▂ ▁`",
        "`▒ ▒ ▆ ▅ ▄ ▂ ▁`",
        "`▒ ▒ ▒ ▅ ▄ ▂ ▁`",
        "`▒ ▒ ▒ ▒ ▄ ▂ ▁`",
        "`▒ ▒ ▒ ▒ ▒ ▂ ▁`",
        "`▒ ▒ ▒ ▒ ▒ ▒ ▁`",
        "`▒ ▒ ▒ ▒ ▒ ▒ ▒`",
        "*Optimising JIO NETWORK...*",
        "`▒ ▒ ▒ ▒ ▒ ▒ ▒`",
        "`▁ ▒ ▒ ▒ ▒ ▒ ▒`",
        "`▁ ▂ ▒ ▒ ▒ ▒ ▒`",
        "`▁ ▂ ▄ ▒ ▒ ▒ ▒`",
        "`▁ ▂ ▄ ▅ ▒ ▒ ▒`",
        "`▁ ▂ ▄ ▅ ▆ ▒ ▒`",
        "`▁ ▂ ▄ ▅ ▆ ▇ ▒`",
        "`▁ ▂ ▄ ▅ ▆ ▇ █`",
        "**JIO NETWORK Boosted....**",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await ult.edit(animation_chars[i % 19])


@ultroid_cmd(pattern="solarsystem")
async def snku(ult):
    animation_interval = 0.1
    animation_ttl = range(0, 80)
    ult = await eor(ult, "solarsystem")
    animation_chars = [
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️🌎◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n🌕◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️☀\n◼️◼️◼️◼️◼️`",
        "`◼️🌕◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️☀◼️`",
        "`◼️◼️◼️🌕◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️☀◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️🌎◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️◼️◼️◼️`",
        "`◼️◼️◼️◼️◼️\n☀◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️🌕\n◼️◼️◼️◼️◼️`",
        "`◼️☀◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️🌕◼️`",
        "`◼️◼️◼️☀◼️\n◼️◼️◼️◼️◼️\n◼️◼️🌎◼️◼️\n◼️◼️◼️◼️◼️\n◼️🌕◼️◼️◼️`",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await ult.edit(animation_chars[i % 8])


@ultroid_cmd(pattern=f"snake$")
async def snku(ult):
    animation_interval = 0.3
    animation_ttl = range(0, 27)
    ult = await eor(ult, "snake..")
    animation_chars = [
        "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◻️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◻️◻️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◻️◻️◻️️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◻️◻️◻️◻️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "‎◻️◻️◻️◻️◻️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◻️◻️◻️◻️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◻️◻️◻️◻️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◻️◻️◻️◻️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◼️",
        "◻️◻️◻️◻️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️",
        "◻️◻️◻️◻️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◻️◻️",
        "◻️◻️◻️◻️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◻️◻️◻️",
        "◻️◻️◻️◻️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️\n◼️◻️◻️◻️◻️",
        "◻️◻️◻️◻️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️\n◻️◻️◻️◻️◻️",
        "◻️◻️◻️◻️◻️\n◼️◼️◼️◼️◻️\n◼️◼️◼️◼️◻️\n◻️◼️◼️◼️◻️\n◻️◻️◻️◻️◻️",
        "◻️◻️◻️◻️◻️\n◼️◼️◼️◼️◻️\n◻️◼️◼️◼️◻️\n◻️◼️◼️◼️◻️\n◻️◻️◻️◻️◻️",
        "◻️◻️◻️◻️◻️\n◻️◼️◼️◼️◻️\n◻️◼️◼️◼️◻️\n◻️◼️◼️◼️◻️\n◻️◻️◻️◻️◻️",
        "◻️◻️◻️◻️◻️\n◻️◻️◼️◼️◻️\n◻️◼️◼️◼️◻️\n◻️◼️◼️◼️◻️\n◻️◻️◻️◻️◻️",
        "◻️◻️◻️◻️◻️\n◻️◻️◻️◼️◻️\n◻️◼️◼️◼️◻️\n◻️◼️◼️◼️◻️\n◻️◻️◻️◻️◻️",
        "◻️◻️◻️◻️◻️\n◻️◻️◻️◻️◻️\n◻️◼️◼️◼️◻️\n◻️◼️◼️◼️◻️\n◻️◻️◻️◻️◻️",
        "◻️◻️◻️◻️◻️\n◻️◻️◻️◻️◻️\n◻️◼️◼️◻️◻️\n◻️◼️◼️◼️◻️\n◻️◻️◻️◻️◻️",
        "◻️◻️◻️◻️◻️\n◻️◻️◻️◻️◻️\n◻️◼️◼️◻️◻️\n◻️◼️◼️◻️◻️\n◻️◻️◻️◻️◻️",
        "◻️◻️◻️◻️◻️\n◻️◻️◻️◻️◻️\n◻️◼️◼️◻️◻️\n◻️◼️◻️◻️◻️\n◻️◻️◻️◻️◻️",
        "◻️◻️◻️◻️◻️\n◻️◻️◻️◻️◻️\n◻️◼️◼️◻️◻️\n◻️◻️◻️◻️◻️\n◻️◻️◻️◻️◻️",
        "◻️◻️◻️◻️◻️\n◻️◻️◻️◻️◻️\n◻️◻️◼️◻️◻️\n◻️◻️◻️◻️◻️\n◻️◻️◻️◻️◻️",
        "◻️◻️◻️◻️◻️\n◻️◻️◻️◻️◻️\n◻️◻️◻️◻️◻️\n◻️◻️◻️◻️◻️\n◻️◻️◻️◻️◻️",
        "◻️◻️◻️◻️◻️\n◻️◼️◻️◼️◻️\n◻️◻️◻️◻️◻️\n◻️◼️◼️◼️◻️\n◻️◻️◻️◻️◻️",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await ult.edit(animation_chars[i % 27])


@ultroid_cmd(pattern="virus$")
async def snku(ult):
    animation_interval = 1
    animation_ttl = range(0, 30)
    ult = await eor(ult, "Injecting virus....")
    animation_chars = [
        "🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎",
        "◼️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎",
        "◼️◼️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎",
        "◼️◼️◼️️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎",
        "◼️◼️◼️◼️🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎",
        "‎◼️◼️◼️◼️◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎",
        "◼️◼️◼️◼️◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎",
        "◼️◼️◼️◼️◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎",
        "◼️◼️◼️◼️◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎",
        "◼️◼️◼️◼️◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️",
        "◼️◼️◼️◼️◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️◼️",
        "◼️◼️◼️◼️◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️◼️◼️",
        "◼️◼️◼️◼️◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n🔴🔵🌕♓♎⛎◼️◼️◼️◼️",
        "◼️◼️◼️◼️◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n◼️◼️◼️◼️◼️",
        "◼️◼️◼️◼️◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n◼️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n◼️◼️◼️◼️◼️",
        "◼️◼️◼️◼️◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n◼️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n◼️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n◼️◼️◼️◼️◼️",
        "◼️◼️◼️◼️◼️\n◼️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n◼️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n◼️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n◼️◼️◼️◼️◼️",
        "◼️◼️◼️◼️◼️\n◼️◼️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n◼️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n◼️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n◼️◼️◼️◼️◼️",
        "◼️◼️◼️◼️◼️\n◼️◼️◼️🔴🔵🌕♓♎⛎◼️\n◼️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n◼️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n◼️◼️◼️◼️◼️",
        "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n◼️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n◼️◼️◼️◼️◼️",
        "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️◼️\n◼️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n◼️◼️◼️◼️◼️",
        "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️◼️\n◼️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️◼️\n◼️◼️◼️◼️◼️",
        "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️◼️\n◼️🔴🔵🌕♓♎⛎◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🔴🔵🌕♓♎⛎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",
        "◼️◼️◼️◼️\n◼️◼️◼️◼️\n◼️◼️◼️◼️\n◼️◼️◼️◼️",
        "◼️◼️◼️\n◼️◼️◼️\n◼️◼️◼️",
        "◼️◼️\n◼️◼️",
        "◼️",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await ult.edit(animation_chars[i % 30])


@ultroid_cmd(pattern=r"repe$")
async def snku(ult):
    animation_interval = 0.2
    animation_ttl = range(0, 30)
    ult = await eor(ult, "repe")
    animation_chars = [
        "**r**",
        "**ra**",
        "**rap**",
        "**rape**",
        "**rape_**",
        "**rape_t**",
        "**rape_tr**",
        "**rape_tra**",
        "**rape_trai**",
        "**rape_train**",
        "**ape_train🚅**",
        "**pe_train🚅🚃🚃**",
        "**e_train🚅🚃🚃🚃**",
        "**_train🚅🚃🚃🚃🚃**",
        "**train🚅🚃🚃🚃🚃🚃**",
        "**rain🚅🚃🚃🚃🚃🚃🚃**",
        "**ain🚅🚃🚃🚃🚃🚃🚃🚃**",
        "**in🚅🚃🚃🚃🚃🚃🚃🚃🚃**",
        "**n🚅🚃🚃🚃🚃🚃🚃🚃🚃🚃**",
        "🚅🚃🚃🚃🚃🚃🚃🚃🚃🚃",
        "🚃🚃🚃🚃🚃🚃🚃🚃🚃",
        "🚃🚃🚃🚃🚃🚃🚃🚃",
        "🚃🚃🚃🚃🚃🚃🚃",
        "🚃🚃🚃🚃🚃🚃",
        "🚃🚃🚃🚃🚃",
        "🚃🚃🚃🚃",
        "🚃🚃🚃",
        "🚃🚃",
        "🚃",
        "**rApEd**",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await ult.edit(animation_chars[i % 30])


@ultroid_cmd(pattern=f"isro$")
async def snku(ult):
    animation_interval = 1
    animation_ttl = range(0, 24)
    ult = await eor(ult, "Connecting..")
    animation_chars = [
        "⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛",
        "⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n🚀⬛⬛⬛⬛⬛",
        "⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛🚀⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛",
        "⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛🚀⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛",
        "⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛🚀⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛",
        "⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛🚀⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛",
        "⬛⬛⬛⬛⬛🚀\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛",
        "🛸⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛",
        "⬛⬛⬛⬛⬛⬛\n🛸⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛",
        "⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛🛸⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛",
        "⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛🛸⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛",
        "⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛🛸⬛⬛⬛\n⬛⬛⬛⬛⬛⬛",
        "⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛🛸⬛⬛",
        "⬛⬛⬛🛸⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛",
        "⬛⬛⬛⬛⬛⬛\n⬛⬛⬛🛸⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛",
        "⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛🛸⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬜⬜⬜⬜⬜⬜",
        "⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛🛸⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬜⬜⬜⬜⬜⬜",
        "⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛🛸⬛⬛\n⬜⬜⬜⬜⬜⬜",
        "⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛🛸⬛🚶‍♂️\n⬜⬜⬜⬜⬜⬜",
        "⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛🛸🚶‍♂️⬛\n⬜⬜⬜⬜⬜⬜",
        "⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n👽⬛⬛🛸🚶‍♂️⬛\n⬜⬜⬜⬜⬜⬜",
        "⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛👽⬛🛸🚶‍♂️⬛\n⬜⬜⬜⬜⬜⬜",
        "⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛👽🛸🚶‍♂️⬛\n⬜⬜⬜⬜⬜⬜",
        "__Signal Lost....__",
    ]

    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await ult.edit(animation_chars[i % 24])


@ultroid_cmd(pattern=f"nakal$")
async def snku(ult):
    animation_interval = 0.5
    animation_ttl = range(0, 6)
    ult = await eor(ult, "nikalo")
    animation_chars = [
        "`⠀⠀⠀⣠⣶⡾⠏⠉⠙⠳⢦⡀⠀⠀⠀⢠⠞⠉⠙⠲⡀⠀\n ⠀⣴⠿⠏⠀⠀⠀⠀⠀   ⢳⡀⠀⡏⠀⠀⠀   ⠀⢷\n⢠⣟⣋⡀⢀⣀⣀⡀⠀⣀⡀⣧⠀⢸⠀⠀⠀  ⠀   ⡇\n⢸⣯⡭⠁⠸⣛⣟⠆⡴⣻⡲⣿  ⣸ Nikalo   ⡇\n ⣟⣿⡭⠀⠀⠀⠀⠀⢱⠀⠀  ⣿  ⢹⠀        ⡇\n  ⠙⢿⣯⠄⠀⠀⠀__⠀⠀⡿ ⠀⡇⠀⠀⠀⠀    ⡼\n⠀⠀⠀⠹⣶⠆⠀⠀⠀⠀⠀⡴⠃⠀   ⠘⠤⣄⣠⠞⠀\n⠀⠀⠀⠀⢸⣷⡦⢤⡤⢤⣞⣁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⢀⣤⣴⣿⣏⠁⠀⠀⠸⣏⢯⣷⣖⣦⡀⠀⠀⠀⠀⠀⠀\n⢀⣾⣽⣿⣿⣿⣿⠛⢲⣶⣾⢉⡷⣿⣿⠵⣿⠀⠀⠀⠀⠀⠀\n⣼⣿⠍⠉⣿⡭⠉⠙⢺⣇⣼⡏⠀⠀ ⠀⣄⢸⠀⠀⠀⠀⠀⠀`",
        "`⠀⠀⠀⣠⣶⡾⠏⠉⠙⠳⢦⡀⠀⠀⠀⢠⠞⠉⠙⠲⡀⠀\n ⠀⣴⠿⠏⠀⠀⠀⠀⠀  ⠀⢳⡀⠀⡏⠀⠀⠀   ⠀⢷\n⢠⣟⣋⡀⢀⣀⣀⡀⠀⣀⡀⣧⠀⢸⠀⠀⠀      ⡇\n⢸⣯⡭⠁⠸⣛⣟⠆⡴⣻⡲⣿  ⣸ bhai ⡇\n ⣟⣿⡭⠀⠀⠀⠀⠀⢱⠀⠀  ⣿  ⢹⠀        ⡇\n  ⠙⢿⣯⠄⠀⠀|__|⠀⠀⡿ ⠀⡇⠀⠀⠀⠀    ⡼\n⠀⠀⠀⠹⣶⠆⠀⠀⠀⠀⠀⡴⠃⠀   ⠘⠤⣄⣠⠞⠀\n⠀⠀⠀⠀⢸⣷⡦⢤⡤⢤⣞⣁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⢀⣤⣴⣿⣏⠁⠀⠀⠸⣏⢯⣷⣖⣦⡀⠀⠀⠀⠀⠀⠀\n⢀⣾⣽⣿⣿⣿⣿⠛⢲⣶⣾⢉⡷⣿⣿⠵⣿⠀⠀⠀⠀⠀⠀\n⣼⣿⠍⠉⣿⡭⠉⠙⢺⣇⣼⡏⠀⠀ ⠀⣄⢸⠀⠀⠀⠀⠀⠀`",
        "`⠀⠀⠀⣠⣶⡾⠏⠉⠙⠳⢦⡀⠀⠀⠀⢠⠞⠉⠙⠲⡀⠀\n ⠀⣴⠿⠏⠀⠀     ⠀⢳⡀⠀⡏⠀⠀    ⠀⢷\n⢠⣟⣋⡀⢀⣀⣀⡀⠀⣀⡀⣧⠀⢸⠀⠀⠀⠀     ⡇\n⢸⣯⡭⠁⠸⣛⣟⠆⡴⣻⡲⣿  ⣸ Pehli   ⡇\n ⣟⣿⡭⠀⠀⠀⠀⠀⢱⠀⠀  ⣿  ⢹⠀         ⡇\n  ⠙⢿⣯⠄⠀⠀(P)⠀⠀⡿ ⠀⡇⠀⠀⠀⠀    ⡼\n⠀⠀⠀⠹⣶⠆⠀⠀⠀⠀⠀⡴⠃⠀   ⠘⠤⣄⣠⠞⠀\n⠀⠀⠀⠀⢸⣷⡦⢤⡤⢤⣞⣁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⢀⣤⣴⣿⣏⠁⠀⠀⠸⣏⢯⣷⣖⣦⡀⠀⠀⠀⠀⠀⠀\n⢀⣾⣽⣿⣿⣿⣿⠛⢲⣶⣾⢉⡷⣿⣿⠵⣿⠀⠀⠀⠀⠀⠀\n⣼⣿⠍⠉⣿⡭⠉⠙⢺⣇⣼⡏⠀⠀ ⠀⣄⢸⠀⠀⠀⠀⠀⠀`",
        "`⠀⠀⠀⣠⣶⡾⠏⠉⠙⠳⢦⡀⠀⠀⠀⢠⠞⠉⠙⠲⡀⠀\n ⠀⣴⠿⠏⠀⠀     ⠀⢳⡀⠀⡏⠀⠀    ⠀⢷\n⢠⣟⣋⡀⢀⣀⣀⡀⠀⣀⡀⣧⠀⢸⠀   ⠀     ⡇\n⢸⣯⡭⠁⠸⣛⣟⠆⡴⣻⡲⣿  ⣸ Fursat  ⡇\n ⣟⣿⡭⠀⠀⠀⠀⠀⢱⠀   ⣿  ⢹⠀        ⡇\n  ⠙⢿⣯⠄⠀⠀⠀__ ⠀⠀⡿ ⠀⡇⠀⠀⠀⠀    ⡼\n⠀⠀⠀⠹⣶⠆⠀⠀⠀⠀⠀⡴⠃⠀   ⠘⠤⣄⣠⠞⠀\n⠀⠀⠀⠀⢸⣷⡦⢤⡤⢤⣞⣁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⢀⣤⣴⣿⣏⠁⠀⠀⠸⣏⢯⣷⣖⣦⡀⠀⠀⠀⠀⠀⠀\n⢀⣾⣽⣿⣿⣿⣿⠛⢲⣶⣾⢉⡷⣿⣿⠵⣿⠀⠀⠀⠀⠀⠀\n⣼⣿⠍⠉⣿⡭⠉⠙⢺⣇⣼⡏⠀⠀ ⠀⣄⢸⠀⠀⠀⠀⠀⠀`",
        "`⠀⠀⠀⣠⣶⡾⠏⠉⠙⠳⢦⡀⠀⠀⠀⢠⠞⠉⠙⠲⡀⠀\n ⠀⣴⠿⠏⠀⠀⠀⠀⠀   ⢳⡀⠀⡏⠀⠀    ⠀⢷\n⢠⣟⣋⡀⢀⣀⣀⡀⠀⣀⡀⣧⠀⢸⠀⠀ ⠀     ⡇\n⢸⣯⡭⠁⠸⣛⣟⠆⡴⣻⡲⣿  ⣸ Meeee   ⡇\n ⣟⣿⡭⠀⠀⠀⠀⠀⢱⠀⠀  ⣿  ⢹⠀        ⡇\n  ⠙⢿⣯⠄⠀⠀|__| ⠀⡿ ⠀⡇⠀⠀⠀⠀    ⡼\n⠀⠀⠀⠹⣶⠆⠀⠀⠀⠀⠀⡴⠃⠀   ⠘⠤⣄⣠⠞⠀\n⠀⠀⠀⠀⢸⣷⡦⢤⡤⢤⣞⣁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⢀⣤⣴⣿⣏⠁⠀⠀⠸⣏⢯⣷⣖⣦⡀⠀⠀⠀⠀⠀⠀\n⢀⣾⣽⣿⣿⣿⣿⠛⢲⣶⣾⢉⡷⣿⣿⠵⣿⠀⠀⠀⠀⠀⠀\n⣼⣿⠍⠉⣿⡭⠉⠙⢺⣇⣼⡏⠀⠀ ⠀⣄⢸⠀⠀⠀⠀⠀⠀`",
        "`⠀⠀⠀⣠⣶⡾⠏⠉⠙⠳⢦⡀⠀⠀⠀⢠⠞⠉⠙⠲⡀⠀\n ⠀⣴⠿⠏⠀⠀⠀⠀⠀  ⠀⢳⡀⠀⡏⠀⠀    ⠀⢷\n⢠⣟⣋⡀⢀⣀⣀⡀⠀⣀⡀⣧⠀⢸⠀  ⠀     ⡇\n⢸⣯⡭⠁⠸⣛⣟⠆⡴⣻⡲⣿  ⣸ Nikalo  ⡇\n ⣟⣿⡭⠀⠀⠀⠀⠀⢱⠀   ⣿  ⢹⠀        ⡇\n  ⠙⢿⣯⠄⠀⠀lodu⠀⠀⡿ ⠀⡇⠀⠀⠀⠀    ⡼\n⠀⠀⠀⠹⣶⠆⠀⠀⠀⠀⠀⡴⠃⠀   ⠘⠤⣄⣠⠞⠀\n⠀⠀⠀⠀⢸⣷⡦⢤⡤⢤⣞⣁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⢀⣤⣴⣿⣏⠁⠀⠀⠸⣏⢯⣷⣖⣦⡀⠀⠀⠀⠀⠀⠀\n⢀⣾⣽⣿⣿⣿⣿⠛⢲⣶⣾⢉⡷⣿⣿⠵⣿⠀⠀⠀⠀⠀⠀\n⣼⣿⠍⠉⣿⡭⠉⠙⢺⣇⣼⡏⠀⠀ ⠀⣄⢸⠀⠀⠀⠀⠀⠀`",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await ult.edit(animation_chars[i % 6])


@ultroid_cmd(pattern=f"music$")
async def snku(ult):
    animation_interval = 1.5
    animation_ttl = range(0, 11)
    await ult.edit("starting player...")
    animation_chars = [
        "⬤⬤⬤ 81% ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀`✖️`\n\n⠀⠀⠀⠀⠀[Survivor Music Player](tg://user?id=916234223)\n\n⠀⠀⠀⠀**Now Playing:shape of u**\n\n**00:00** ▱▱▱▱▱▱▱▱▱▱ **00:10**\n\n⠀⠀⠀⠀⠀`🔂` `⏮️` `⏪️` `▶️` `⏩️` `⏭️`\n\n**⠀Next Song:** __Alan Walker - Alone.__\n\n⠀⠀⠀⠀**⠀Device: Nokia 1100**",
        "⬤⬤⬤ 81% ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀`✖️`\n\n⠀⠀⠀⠀⠀[Survivor Music Player](tg://user?id=916234223)\n\n⠀⠀⠀⠀**Now Playing:shape of u**\n\n**00:01** ▰▱▱▱▱▱▱▱▱▱ **00:10**\n\n⠀⠀⠀⠀⠀`🔂` `⏮️` `⏪️` `⏸️` `⏩️` `⏭️`\n\n**⠀Next Song:** __Alan Walker - Alone.__\n\n⠀⠀⠀⠀**⠀Device: Nokia 1100**",
        "⬤⬤⬤ 81% ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀`✖️`\n\n⠀⠀⠀⠀⠀[Survivor  Music Player](tg://user?id=916234223)\n\n⠀⠀⠀⠀**Now Playing:shape of u**\n\n**00:02** ▰▰▱▱▱▱▱▱▱▱ **00:10**\n\n⠀⠀⠀⠀⠀`🔂` `⏮️` `⏪️` `⏸️` `⏩️` `⏭️`\n\n**⠀Next Song:** __Alan Walker - Alone.__\n\n⠀⠀⠀⠀**⠀Device: Nokia 1100**",
        "⬤⬤⬤ 81% ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀`✖️`\n\n⠀⠀⠀⠀⠀[Survivor Music Player](tg://user?id=916234223)\n\n⠀⠀⠀⠀**Now Playing:shape of u**\n\n**00:03** ▰▰▰▱▱▱▱▱▱▱ **00:10**\n\n⠀⠀⠀⠀⠀`🔂` `⏮️` `⏪️` `⏸️` `⏩️` `⏭️`\n\n**⠀Next Song:** __Alan Walker - Alone.__\n\n⠀⠀⠀⠀**⠀Device: Nokia 1100**",
        "⬤⬤◯ 80% ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀`✖️`\n\n⠀⠀⠀⠀ [Survivor Music Player](tg://user?id=916234223)\n\n⠀⠀⠀⠀**Now Playing:shape of u**\n\n**00:04** ▰▰▰▰▱▱▱▱▱▱ **00:10**\n\n⠀⠀⠀⠀⠀`🔂` `⏮️` `⏪️` `⏸️` `⏩️` `⏭️`\n\n**⠀Next Song:** __Alan Walker - Alone.__\n\n⠀⠀⠀⠀**⠀Device: Nokia 1100**",
        "⬤⬤◯ 80% ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀`✖️`\n\n⠀⠀⠀⠀⠀[Survivor Music Player](tg://user?id=916234223)\n\n⠀⠀⠀⠀**Now Playing:shape of u**\n\n**00:05** ▰▰▰▰▱▱▱▱▱▱ **00:10**\n\n⠀⠀⠀⠀⠀`🔂` `⏮️` `⏪️` `⏸️` `⏩️` `⏭️`\n\n**⠀Next Song:** __Alan Walker - Alone.__\n\n⠀⠀⠀⠀**⠀Device: Nokia 1100**",
        "⬤⬤◯ 80% ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀`✖️`\n\n⠀⠀⠀⠀⠀[Survivor Music Player](tg://user?id=916234223)\n\n⠀⠀⠀⠀**Now Playing:shape of u**\n\n**00:06** ▰▰▰▰▰▰▱▱▱▱ **00:10**\n\n⠀⠀⠀⠀⠀`🔂` `⏮️` `⏪️` `⏸️` `⏩️` `⏭️`\n\n**⠀Next Song:** __Alan Walker - Alone.__\n\n⠀⠀⠀⠀**⠀Device: Nokia 1100**",
        "⬤⬤◯ 80% ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀`✖️`\n\n⠀⠀⠀⠀⠀[Survivor Music Player](tg://user?id=916234223)\n\n⠀⠀⠀⠀**Now Playing:shape of u**\n\n**00:07** ▰▰▰▰▰▰▰▱▱▱ **00:10**\n\n⠀⠀⠀⠀⠀`🔂` `⏮️` `⏪️` `⏸️` `⏩️` `⏭️`\n\n**⠀Next Song:** __Alan Walker - Alone.__\n\n⠀⠀⠀⠀**⠀Device: Nokia 1100**",
        "⬤⬤◯ 80% ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀`✖️`\n\n⠀⠀⠀⠀⠀[Survivor Music Player](tg://user?id=916234223)\n\n⠀⠀⠀⠀**Now Playing:shape of u**\n\n**00:08** ▰▰▰▰▰▰▰▰▱▱ **00:10**\n\n⠀⠀⠀⠀⠀`🔂` `⏮️` `⏪️` `⏸️` `⏩️` `⏭️`\n\n**⠀Next Song:** __Alan Walker - Alone.__\n\n⠀⠀⠀⠀**⠀Device: Nokia 1100**",
        "⬤⬤◯ 80% ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀`✖️`\n\n⠀⠀⠀⠀⠀[Survivor Music Player](tg://user?id=916234223)\n\n⠀⠀⠀⠀**Now Playing:shape of u**\n\n**00:09** ▰▰▰▰▰▰▰▰▰▱ **00:10**\n\n⠀⠀⠀⠀⠀`🔂` `⏮️` `⏪️` `⏸️` `⏩️` `⏭️`\n\n**⠀Next Song:** __Alan Walker - Alone.__\n\n⠀⠀⠀⠀**⠀Device: Nokia 1100**",
        "⬤⬤◯ 80% ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀`✖️`\n\n⠀⠀⠀⠀⠀[Survivor Music Player](tg://user?id=916234223)\n\n⠀⠀⠀⠀**Now Playing:shape of u**\n\n**00:10** ▰▰▰▰▰▰▰▰▰▰ **00:10**\n\n⠀⠀⠀⠀⠀`🔂` `⏮️` `⏪️` `⏺️` `⏩️` `⏭️`\n\n**⠀Next Song:** __Alan Walker - Alone.__\n\n⠀⠀⠀⠀**⠀Device: Nokia 1100**",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await ult.edit(animation_chars[i % 11])


@ultroid_cmd(pattern=f"squ$")
async def snku(ult):
    ult = await eor(ult, "╔═══════════════════╗ \n  \n╚═══════════════════╝")
    await asyncio.sleep(1)
    await ult.edit("╔═══════════════════╗ \n \t░ \n╚═══════════════════╝")
    await asyncio.sleep(1)
    await ult.edit("╔═══════════════════╗ \n ░ \t░ \n╚═══════════════════╝")
    await asyncio.sleep(1)
    await ult.edit("╔═══════════════════╗ \n ░ ░ ░ \n╚═══════════════════╝")
    await asyncio.sleep(1)
    await ult.edit("╔═══════════════════╗ \n ░ ░ ░ ░ \n╚═══════════════════╝")
    await asyncio.sleep(1)
    await ult.edit("╔═══════════════════╗ \n ░ ░ ░ ░ ░ \n╚═══════════════════╝")
    await asyncio.sleep(1)
    await ult.edit("╔═══════════════════╗ \n ░ ░ ░ ░ ░ ░ \n╚═══════════════════╝")
    await asyncio.sleep(1)
    await ult.edit("╔═══════════════════╗ \n ░ ░ ░ ░ ░ ░ ░ \n╚═══════════════════╝")
    await asyncio.sleep(1)
    await ult.edit("╔═══════════════════╗ \n ░ ░ ░ ░ ░ ░ ░ ░ \n╚═══════════════════╝")
    await asyncio.sleep(1)
    await ult.edit(
        "╔═══════════════════╗ \n ░ ░ ░ ░ ░ ░ ░ ░ ░ \n╚═══════════════════╝"
    )
    await asyncio.sleep(1)
    await ult.edit(
        "╔═══════════════════╗ \n ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ \n╚═══════════════════╝"
    )
    await asyncio.sleep(1)
    await ult.edit(
        "╔═══════════════════╗ \n ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ \n╚═══════════════════╝"
    )
    await asyncio.sleep(1)
    await ult.edit(
        "╔═══════════════════╗ \n ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ \n╚═══════════════════╝"
    )
    await asyncio.sleep(1)
    await ult.edit(
        "╔═══════════════════╗ \n ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ \n╚═══════════════════╝"
    )
    await asyncio.sleep(1)
    await ult.edit(
        "╔═══════════════════╗ \n ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ \n╚═══════════════════╝"
    )
    await asyncio.sleep(6)


@ultroid_cmd(pattern="bufferedd( (.*)|$)")
async def snku(ult):
    ult = await eor(ult, "...")
    animation_interval = 0.3
    animation_ttl = range(0, 20)
    animation_chars = ["▮", "▯", "▬", "▭", "‎"]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await ult.edit(animation_chars[i % 4])


@ultroid_cmd(pattern="dabba( (.*)|$)")
async def snku(ult):
    ult = await eor(ult, "...")
    animation_interval = 0.3
    animation_ttl = range(0, 20)
    animation_chars = ["◧", "◨", "◧", "◨", "‎"]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await ult.edit(animation_chars[i % 4])


@ultroid_cmd(pattern="kein( (.*)|$)")
async def snku(ult):
    ult = await eor(ult, "...")
    animation_interval = 0.3
    animation_ttl = range(0, 20)
    animation_chars = ["╹", "╻", "╹", "╻", "‎"]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await ult.edit(animation_chars[i % 4])


@ultroid_cmd(pattern="dhab( (.*)|$)")
async def snku(ult):
    ult = await eor(ult, "...")
    animation_interval = 0.3
    animation_ttl = range(0, 20)
    animation_chars = ["⚫", "⬤", "●", "∘", "‎"]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await ult.edit(animation_chars[i % 4])


@ultroid_cmd(pattern="love2( (.*)|$)")
async def snku(ult):
    ult = await eor(ult, "...")
    animation_interval = 0.5
    animation_ttl = range(0, 20)
    animation_chars = ["🖤", "❤️", "🖤", "❤️", "‎"]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await ult.edit(animation_chars[i % 4])


@ultroid_cmd(pattern="raped( (.*)|$)")
async def snku(ult):
    ult = await eor(ult, "...")
    animation_interval = 1
    animation_ttl = range(0, 11)
    animation_chars = [
        "😁",
        "😧",
        "😡",
        "😢",
        "‎**Repo of  @r4v4n4**",
        "😁",
        "😧",
        "😡",
        "😢",
        "[Raped](github.com/ravana69)",
        "__**Good to See you Guys....**__",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await ult.edit(animation_chars[i % 11])


@ultroid_cmd(pattern="fnl( (.*)|$)")
async def snku(ult):
    ult = await eor(ult, "...")
    animation_interval = 2
    animation_ttl = range(0, 6)
    animation_chars = ["😁🏿", "😁🏾", "😁🏽", "😁🏼", "‎😁", "**Good to See you Guys....**"]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await ult.edit(animation_chars[i % 6])


@ultroid_cmd(pattern="monyet( (.*)|$)")
async def snku(ult):
    ult = await eor(ult, "..")
    animation_interval = 2
    animation_ttl = range(0, 6)
    animation_chars = ["🐵", "🙉", "🙈", "🙊", "🖕‎🐵🖕", "**Good to See you Guys....**"]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await ult.edit(animation_chars[i % 6])


@ultroid_cmd(pattern="herber( (.*)|$)")
async def snku(ult):
    ult = await eor(ult, "...")
    animation_interval = 2
    animation_ttl = range(0, 11)
    animation_chars = [
        "**===================**\n      **Server Details**  \n**===================**\n\n\n**=>>>   CPU   <<<=**\n\n    **🔹current_freq:** 2500.09MHz\n    **🔹total_usage:** 10%\n\n    ●○○○○○○○○○\n\n    **🔹cpu core**\n\n        **🔹core_usage:** 5.9%\n        **🔹current_freq:** 2500.09MHz\n        |██████████▉  |\n       \n**=>>>   RAM   <<<=**\n\n    **🔹free:** 8.13GB\n    **🔹used:** 33.77GB\n    **🔹total:** 60.0GB\n    \n    ●●●●●●●○○○\n\n\n**=>>>   DISK   <<<=**\n\n   **🔹free:** 224.12GB\n    **🔹used:** 131.84GB\n    **🔹total:** 375.02GB\n    **🔹usage:** 37.0%\n\n    |████▍        |\n\n\n**=>>>   NETWORK   <<<=**\n\n    **🔹sent:** 158.98GB\n    **🔹recv:** 146.27GB\n    **🔹sent_packets:** 84518799\n    **🔹recv_packets:** 159720314\n\n\n**===================**\n",
        "**===================**\n      **Server Details**  \n**===================**\n\n\n**=>>>   CPU   <<<=**\n\n    **🔹current_freq:** 2500.09MHz\n    **🔹total_usage:** 30%\n\n    ●●●○○○○○○○\n\n    **🔹cpu core**\n\n        **🔹core_usage:** 20.4%\n        **🔹current_freq:** 2500.09MHz\n        |██████████▉  |\n       \n**=>>>   RAM   <<<=**\n\n    **🔹free:** 7.18GB\n    **🔹used:** 28.26GB\n    **🔹total:** 60.0GB\n    \n    ●●●●●●●●●●\n\n\n**=>>>   DISK   <<<=**\n\n   **🔹free:** 224.12GB\n    **🔹used:** 131.84GB\n    **🔹total:** 375.02GB\n    **🔹usage:** 37.0%\n\n    |████▍        |\n\n\n**=>>>   NETWORK   <<<=**\n\n    **🔹sent:** 146.27GB\n    **🔹recv:** 124.33GB\n    **🔹sent_packets:** 54635686\n    **🔹recv_packets:** 143565654\n\n\n**===================**\n",
        "**===================**\n      **Server Details**  \n**===================**\n\n\n**=>>>   CPU   <<<=**\n\n    **🔹current_freq:** 2500.09MHz\n    **🔹total_usage:** 60%\n\n    ●●●●●●○○○○\n\n    **🔹cpu core**\n\n        **🔹core_usage:** 60.9%\n        **🔹current_freq:** 2500.09MHz\n        |██████████▉  |\n       \n**=>>>   RAM   <<<=**\n\n    **🔹free:** 6.52GB\n    **🔹used:** 35.78GB\n    **🔹total:** 60.0GB\n    \n    ●●●○○○○○○○\n\n\n**=>>>   DISK   <<<=**\n\n   **🔹free:** 224.12GB\n    **🔹used:** 131.84GB\n    **🔹total:** 375.02GB\n    **🔹usage:** 37.0%\n\n    |████▍        |\n\n\n**=>>>   NETWORK   <<<=**\n\n    **🔹sent:** 124.33GB\n    **🔹recv:** 162.48GB\n    **🔹sent_packets:** 25655655\n    **🔹recv_packets:** 165289456\n\n\n**===================**\n",
        "**===================**\n      **Server Details**  \n**===================**\n\n\n**=>>>   CPU   <<<=**\n\n    **🔹current_freq:** 2500.09MHz\n    **🔹total_usage:** 100%\n\n    ●●●●●●●●●●\n\n    **🔹cpu core**\n\n        **🔹core_usage:** 100.0%\n        **🔹current_freq:** 2500.09MHz\n        |██████████▉  |\n       \n**=>>>   RAM   <<<=**\n\n    **🔹free:** 9.81GB\n    **🔹used:** 30.11GB\n    **🔹total:** 60.0GB\n    \n    ●●●●●●●●●●\n\n\n**=>>>   DISK   <<<=**\n\n   **🔹free:** 224.12GB\n    **🔹used:** 131.84GB\n    **🔹total:** 375.02GB\n    **🔹usage:** 37.0%\n\n    |████▍        |\n\n\n**=>>>   NETWORK   <<<=**\n\n    **🔹sent:** 162.48GB\n    **🔹recv:** 175.75GB\n    **🔹sent_packets:** 56565435\n    **🔹recv_packets:** 135345655\n\n\n**===================**\n",
        "**===================**\n      **Server Details**  \n**===================**\n\n\n**=>>>   CPU   <<<=**\n\n    **🔹current_freq:** 2500.09MHz\n    **🔹total_usage:** 70%\n\n    ●●●●●●●○○○\n\n    **🔹cpu core**\n\n        **🔹core_usage:** 80.4%\n        **🔹current_freq:** 2500.09MHz\n        |██████████▉  |\n       \n**=>>>   RAM   <<<=**\n\n    **🔹free:** 5.76GB\n    **🔹used:** 29.35GB\n    **🔹total:** 60.0GB\n    \n    ●●●●●●●○○○\n\n\n**=>>>   DISK   <<<=**\n\n   **🔹free:** 224.12GB\n    **🔹used:** 131.84GB\n    **🔹total:** 375.02GB\n    **🔹usage:** 37.0%\n\n    |████▍        |\n\n\n**=>>>   NETWORK   <<<=**\n\n    **🔹sent:** 175.75GB\n    **🔹recv:** 118.55GB\n    **🔹sent_packets:** 36547698\n    **🔹recv_packets:** 185466554\n\n\n**===================**\n",
        "**===================**\n      **Server Details**  \n**===================**\n\n\n**=>>>   CPU   <<<=**\n\n    **🔹current_freq:** 2500.09MHz\n    **🔹total_usage:** 60%\n\n    ●●●●●●○○○○\n\n    **🔹cpu core**\n\n        **🔹core_usage:** 62.9%\n        **🔹current_freq:** 2500.09MHz\n        |██████████▉  |\n       \n**=>>>   RAM   <<<=**\n\n    **🔹free:** 8.23GB\n    **🔹used:** 33.32GB\n    **🔹total:** 60.0GB\n    \n    ●●●●●●○○○○\n\n\n**=>>>   DISK   <<<=**\n\n   **🔹free:** 224.12GB\n    **🔹used:** 131.84GB\n    **🔹total:** 375.02GB\n    **🔹usage:** 37.0%\n\n    |████▍        |\n\n\n**=>>>   NETWORK   <<<=**\n\n    **🔹sent:** 118.55GB\n    **🔹recv:** 168.65GB\n    **🔹sent_packets:** 24786554\n    **🔹recv_packets:** 156745865\n\n\n**===================**\n",
        "**===================**\n      **Server Details**  \n**===================**\n\n\n**=>>>   CPU   <<<=**\n\n    **🔹current_freq:** 2500.09MHz\n    **🔹total_usage:** 30%\n\n    ●●●○○○○○○○\n\n    **🔹cpu core**\n\n        **🔹core_usage:** 30.6%\n        **🔹current_freq:** 2500.09MHz\n        |██████████▉  |\n       \n**=>>>   RAM   <<<=**\n\n    **🔹free:** 9.75GB\n    **🔹used:** 36.54GB\n    **🔹total:** 60.0GB\n    \n    ●●●●●●●●●●\n\n\n**=>>>   DISK   <<<=**\n\n   **🔹free:** 224.12GB\n    **🔹used:** 131.84GB\n    **🔹total:** 375.02GB\n    **🔹usage:** 37.0%\n\n    |████▍        |\n\n\n**=>>>   NETWORK   <<<=**\n\n    **🔹sent:** 168.65GB\n    **🔹recv:** 128.35GB\n    **🔹sent_packets:** 56565435\n    **🔹recv_packets:** 1475823589\n\n\n**===================**\n",
        "**===================**\n      **Server Details**  \n**===================**\n\n\n**=>>>   CPU   <<<=**\n\n    **🔹current_freq:** 2500.09MHz\n    **🔹total_usage:** 10%\n\n    ●○○○○○○○○○\n\n    **🔹cpu core**\n\n        **🔹core_usage:** 10.2%\n        **🔹current_freq:** 2500.09MHz\n        |██████████▉  |\n       \n**=>>>   RAM   <<<=**\n\n    **🔹free:** 10.20GB\n    **🔹used:** 25.40GB\n    **🔹total:** 60.0GB\n    \n    ●●●●●●○○○○\n\n\n**=>>>   DISK   <<<=**\n\n   **🔹free:** 224.12GB\n    **🔹used:** 131.84GB\n    **🔹total:** 375.02GB\n    **🔹usage:** 37.0%\n\n    |████▍        |\n\n\n**=>>>   NETWORK   <<<=**\n\n    **🔹sent:** 128.35GB\n    **🔹recv:** 108.31GB\n    **🔹sent_packets:** 54635686\n    **🔹recv_packets:** 157865426\n\n\n**===================**\n",
        "**===================**\n      **Server Details**  \n**===================**\n\n\n**=>>>   CPU   <<<=**\n\n    **🔹current_freq:** 2500.09MHz\n    **🔹total_usage:** 100%\n\n    ●●●●●●●●●●\n\n    **🔹cpu core**\n\n        **🔹core_usage:** 100.0%\n        **🔹current_freq:** 2500.09MHz\n        |██████████▉  |\n       \n**=>>>   RAM   <<<=**\n\n    **🔹free:** 5.25GB\n    **🔹used:** 31.14GB\n    **🔹total:** 60.0GB\n    \n    ●●●●●●●●●●\n\n\n**=>>>   DISK   <<<=**\n\n   **🔹free:** 224.12GB\n    **🔹used:** 131.84GB\n    **🔹total:** 375.02GB\n    **🔹usage:** 37.0%\n\n    |████▍        |\n\n\n**=>>>   NETWORK   <<<=**\n\n    **🔹sent:** 108.31GB\n    **🔹recv:** 167.17GB\n    **🔹sent_packets:** 84518799\n    **🔹recv_packets:** 124575356\n\n\n**===================**\n",
        "**===================**\n      **Server Details**  \n**===================**\n\n\n**=>>>   CPU   <<<=**\n\n    **🔹current_freq:** 2500.09MHz\n    **🔹total_usage:** 70%\n\n    ●●●●●●●○○○\n\n    **🔹cpu core**\n\n        **🔹core_usage:** 76.2%\n        **🔹current_freq:** 2500.09MHz\n        |██████████▉  |\n       \n**=>>>   RAM   <<<=**\n\n    **🔹free:** 8.01GB\n    **🔹used:** 33.27GB\n    **🔹total:** 60.0GB\n    \n    ●●●○○○○○○○\n\n\n**=>>>   DISK   <<<=**\n\n   **🔹free:** 224.12GB\n    **🔹used:** 131.84GB\n    **🔹total:** 375.02GB\n    **🔹usage:** 37.0%\n\n    |████▍        |\n\n\n**=>>>   NETWORK   <<<=**\n\n    **🔹sent:** 167.17GB\n    **🔹recv:** 158.98GB\n    **🔹sent_packets:** 36547698\n    **🔹recv_packets:** 165455856\n\n\n**===================**\n",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await ult.edit(animation_chars[i % 11])


@ultroid_cmd(pattern="hand( (.*)|$)")
async def snku(ult):
    ult = await eor(ult, "...")
    animation_interval = 1
    animation_ttl = range(0, 14)
    animation_chars = [
        "👈",
        "👉",
        "☝️",
        "👆",
        "👇",
        "✌️",
        "🤞",
        "🖖",
        "🤘",
        "🤙",
        "🖐️",
        "👌",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await ult.edit(animation_chars[i % 14])


@ultroid_cmd(pattern="gsg( (.*)|$)")
async def snku(ult):
    ult = await eor(ult,  "...")
    animation_interval = 1
    animation_ttl = range(0, 13)
    animation_chars = [
        "🔟",
        "9️⃣",
        "8️⃣",
        "7️⃣",
        "6️⃣",
        "5️⃣",
        "4️⃣",
        "3️⃣",
        "2️⃣",
        "1️⃣",
        "0️⃣",
        "🆘",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await ult.edit(animation_chars[i % 13])


@ultroid_cmd(pattern="heart( (.*)|$)")
async def snku(ult):
    ult = await eor(ult, "...")
    animation_interval = 0.3
    animation_ttl = range(0, 54)
    animation_chars = [
        "❤️",
        "🧡",
        "💛",
        "💚",
        "💙",
        "💜",
        "🖤",
        "💘",
        "💝",
        "❤️",
        "🧡",
        "💛",
        "💚",
        "💙",
        "💜",
        "🖤",
        "💘",
        "💝",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await ult.edit(animation_chars[i % 18])


@ultroid_cmd(pattern=r"fdance")
async def snku(ult):
    animation_interval = 1
    animation_ttl = range(0, 5)
    ult = await eor(ult, "Connecting..")
    animation_chars = [
        "⠀⠀⠀⣶⣿⣶/n⠀⠀⠀⣿⣿⣿⣀/n⠀⣀⣿⣿⣿⣿⣿⣿/n⣶⣿⠛⣭⣿⣿⣿⣿/n⠛⠛⠛⣿⣿⣿⣿⠿/n⠀⠀⠀⠀⣿⣿⣿/n⠀⠀⣀⣭⣿⣿⣿⣿⣀/n⠀⠤⣿⣿⣿⣿⣿⣿⠉/n⠀⣿⣿⣿⣿⣿⣿⠉/n⣿⣿⣿⣿⣿⣿/n⣿⣿⣶⣿⣿/n⠉⠛⣿⣿⣶⣤/n⠀⠀⠉⠿⣿⣿⣤/n⠀⠀⣀⣤⣿⣿⣿/n⠀⠒⠿⠛⠉⠿⣿/n⠀⠀⠀⠀⠀⣀⣿⣿/n⠀⠀⠀⠀⣶⠿⠿⠛/n",
        "⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣤/n⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿/n⠀⠀⣶⠀⠀⣀⣤⣶⣤⣉⣿⣿⣤⣀/n⠤⣤⣿⣤⣿⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣀/n⠀⠛⠿⠀⠀⠀⠀⠉⣿⣿⣿⣿⣿⠉⠛⠿⣿⣤/n⠀⠀⠀⠀⠀⠀⠀⠀⠿⣿⣿⣿⠛⠀⠀⠀⣶⠿/n⠀⠀⠀⠀⠀⠀⠀⠀⣀⣿⣿⣿⣿⣤⠀⣿⠿/n⠀⠀⠀⠀⠀⠀⠀⣶⣿⣿⣿⣿⣿⣿⣿⣿/n⠀⠀⠀⠀⠀⠀⠀⠿⣿⣿⣿⣿⣿⠿⠉⠉/n⠀⠀⠀⠀⠀⠀⠀⠉⣿⣿⣿⣿⠿/n⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⠉/n⠀⠀⠀⠀⠀⠀⠀⠀⣛⣿⣭⣶⣀/n⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿/n⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠉⠛⣿/n⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⣿⣿/n⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣉⠀⣶⠿/n⠀⠀⠀⠀⠀⠀⠀⠀⣶⣿⠿/n⠀⠀⠀⠀⠀⠀⠀⠛⠿⠛/n",
        "⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣶/n⠀⠀⠀⠀⠀⣀⣀⠀⣶⣿⣿⠶/n⣶⣿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣤⣤/n⠀⠉⠶⣶⣀⣿⣿⣿⣿⣿⣿⣿⠿⣿⣤⣀/n⠀⠀⠀⣿⣿⠿⠉⣿⣿⣿⣿⣭⠀⠶⠿⠿/n⠀⠀⠛⠛⠿⠀⠀⣿⣿⣿⣉⠿⣿⠶/n⠀⠀⠀⠀⠀⣤⣶⣿⣿⣿⣿⣿/n⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⠒/n⠀⠀⠀⠀⣀⣿⣿⣿⣿⣿⣿⣿/n⠀⠀⠀⠀⠀⣿⣿⣿⠛⣭⣭⠉/n⠀⠀⠀⠀⠀⣿⣿⣭⣤⣿⠛/n⠀⠀⠀⠀⠀⠛⠿⣿⣿⣿⣭/n⠀⠀⠀⠀⠀⠀⠀⣿⣿⠉⠛⠿⣶⣤/n⠀⠀⠀⠀⠀⠀⣀⣿⠀⠀⣶⣶⠿⠿⠿/n⠀⠀⠀⠀⠀⠀⣿⠛/n⠀⠀⠀⠀⠀⠀⣭⣶/n",
        "⠀⠀⠀⠀⠀⠀⣶⣿⣶/n⠀⠀⠀⣤⣤⣤⣿⣿⣿/n⠀⠀⣶⣿⣿⣿⣿⣿⣿⣿⣶/n⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿/n⠀⠀⣿⣉⣿⣿⣿⣿⣉⠉⣿⣶/n⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⠿⣿/n⠀⣤⣿⣿⣿⣿⣿⣿⣿⠿⠀⣿⣶/n⣤⣿⠿⣿⣿⣿⣿⣿⠿⠀⠀⣿⣿⣤/n⠉⠉⠀⣿⣿⣿⣿⣿⠀⠀⠒⠛⠿⠿⠿/n⠀⠀⠀⠉⣿⣿⣿⠀⠀⠀⠀⠀⠀⠉/n⠀⠀⠀⣿⣿⣿⣿⣿⣶/n⠀⠀⠀⠀⣿⠉⠿⣿⣿/n⠀⠀⠀⠀⣿⣤⠀⠛⣿⣿/n⠀⠀⠀⠀⣶⣿⠀⠀⠀⣿⣶/n⠀⠀⠀⠀⠀⠀⠀⠀⠀⣭⣿⣿/n⠀⠀⠀⠀⠀⠀⠀⠀⣤⣿⣿⠉/n",
        "⠀⠀⠀⠀⠀⠀⣤⣶⣶/n⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣀⣀/n⠀⠀⠀⠀⠀⣀⣶⣿⣿⣿⣿⣿⣿/n⣤⣶⣀⠿⠶⣿⣿⣿⠿⣿⣿⣿⣿/n⠉⠿⣿⣿⠿⠛⠉⠀⣿⣿⣿⣿⣿/n⠀⠀⠉⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣤⣤/n⠀⠀⠀⠀⠀⠀⠀⣤⣶⣿⣿⣿⣿⣿⣿/n⠀⠀⠀⠀⠀⣀⣿⣿⣿⣿⣿⠿⣿⣿⣿⣿/n⠀⠀⠀⠀⣀⣿⣿⣿⠿⠉⠀⠀⣿⣿⣿⣿/n⠀⠀⠀⠀⣿⣿⠿⠉⠀⠀⠀⠀⠿⣿⣿⠛/n⠀⠀⠀⠀⠛⣿⣿⣀⠀⠀⠀⠀⠀⣿⣿⣀/n⠀⠀⠀⠀⠀⣿⣿⣿⠀⠀⠀⠀⠀⠿⣿⣿/n⠀⠀⠀⠀⠀⠉⣿⣿⠀⠀⠀⠀⠀⠀⠉⣿/n⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⣀⣿/n⠀⠀⠀⠀⠀⠀⣀⣿⣿/n⠀⠀⠀⠀⠤⣿⠿⠿⠿/n",
    ]

    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await ult.edit(animation_chars[i % 5])

@ultroid_cmd(pattern="g1 ?(.*)")
async def payf(event):
    paytext = event.pattern_match.group(1)
    pay = paytext+"\n"
    pay = pay*80
    await eor(event, pay)


@ultroid_cmd(pattern="uff ?(.*)")
async def _(event):
    event = await eor(event, "...")
    animation_interval = 1
    animation_ttl = range(0, 13)
    animation_chars = [
        "U",
        "Uf",
        "Uff",
        "Ufffff",
        "Uffffff",
        "Ufffffff",
        "Uffffffff",
        "Ufffffffff",
        "Uffffffffff",
        "Ufffffffffff",
        "Uffffffffffff",
        "Ufffffffffffff",
        "Uffffffffffffff",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 13])


@ultroid_cmd(pattern="ctext ?(.*)")
async def payf(event):
    paytext = event.pattern_match.group(1)
    pay = "{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}".format(
        paytext * 8,
        paytext * 8,
        paytext * 2,
        paytext * 2,
        paytext * 2,
        paytext * 2,
        paytext * 2,
        paytext * 2,
        paytext * 2,
        paytext * 2,
        paytext * 8,
        paytext * 8,
    )
    await eor(event, pay)


@ultroid_cmd(pattern="ftext ?(.*)")
async def payf(event):
    paytext = event.pattern_match.group(1)
    pay = "{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}".format(
        paytext * 8,
        paytext * 8,
        paytext * 2,
        paytext * 2,
        paytext * 2,
        paytext * 6,
        paytext * 6,
        paytext * 2,
        paytext * 2,
        paytext * 2,
        paytext * 2,
        paytext * 2,
    )
    await eor(event, pay)


@ultroid_cmd(pattern="kf$(.*)")
async def _(event):
    r = random.randint(0, 3)
    if r == 0:
        await eor(event, "┏━━━┓\n┃┏━━┛\n┃┗━━┓\n┃┏━━┛\n┃┃\n┗┛")
    else:
        r == 1
        await eor(event, "╭━━━╮\n┃╭━━╯\n┃╰━━╮\n┃╭━━╯\n┃┃\n╰╯")


@ultroid_cmd(pattern="f (.*)")
async def payf(e):
    paytext = e.pattern_match.group(1)
    pay = "{}\n{}\n{}\n{}\n{}\n{}\n{}".format(
        paytext * 5,
        paytext * 1,
        paytext * 1,
        paytext * 4,
        paytext * 1,
        paytext * 1,
        paytext * 1,
    )
    await eor(e, pay)
