import asyncio
from time import sleep

@ultroid_cmd(pattern="me")
async def _(xx):
 me = await xx.client.get_me()
 xx = await xx.edit("HAI JELEK!")
 await asyncio.sleep(3)
 await xx.edit(xx, f"**KENALIN NIH {me.first_name}**")
 await asyncio.sleep(1)
 await xx.edit(xx, f"**{me.first_name} ORANG PALING CAKEP SE TELEGRAM**")
 await asyncio.sleep(1)
 await xx.edit("GAK KEK ELU")
 await asyncio.sleep(1)
 await xx.edit("HEHEHE")
 await asyncio.sleep(1)
 await xx.edit("Run! Run! Runn!!!")
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


 
