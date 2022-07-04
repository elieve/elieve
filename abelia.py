import asyncio
from time import sleep

@ultroid_cmd(pattern="me")
async def _(xx):
 me = await xx.client.get_me()
 xxx = await edit("HAI JELEK!")
 await asyncio.sleep(3)
 await xxx.edit(xx, f"**KENALIN NIH {me.mention}**")
 await asyncio.sleep(1)
 await xxx.edit(xx, f"**{me.mention} ORANG PALING CAKEP SE TELEGRAM**")
 await asyncio.sleep(1)
 await xxx.edit("GAK KEK ELU")
 await asyncio.sleep(1)
 await xxx.edit("HEHEHE")
 await asyncio.sleep(1)
 await xxx.edit("Run! Run! Runn!!!")
 await asyncio.sleep(1)
 await xxx.edit("""
 
┏━━┳┓╋╋┏┳━━━┓
┃┏┓┃┗┓┏┛┃┏━━┛
┃┗┛┗┓┗┛┏┫┗━━┓
┃┏━┓┣┓┏┛┃┏━━┛
┃┗━┛┃┃┃╋┃┗━━┓
┗━━━┛┗┛╋┗━━━┛
MWAHH
       
 """)


 
