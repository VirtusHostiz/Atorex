import discord
import asyncio
import random
import time
import datetime

client = discord.Client()
prefix = "/"

seconds = 0
minutes = 0
hour = 0

@client.event    
async def on_message(message):    
    if message.content.startswith(prefix+'uptime'):
        uptimeemb = discord.Embed(
            title="Uptime",
            color=0x000000,
            description="`Estou online faz {0} horas, {1} minutos e {2} segundos|{3}. `".format(hour, minutes,
                                                                                                     seconds, message.server)
        )

        await client.send_message(message.channel, embed=uptimeemb)


async def uptime():
    await client.wait_until_ready()
    global seconds
    seconds = 0
    global minutes
    minutes = 0
    global hour
    hour = 0
    while not client.is_closed:

        seconds += 
        if seconds == 60:
            seconds = 0
            minutes += 1
        await asyncio.sleep(1)
        if minutes == 60:
            minutes = 0
            hour += 1





client.run('NDY0NjA0NDczOTMxODU3OTIx.DiBYJw.S2iTn7TXy7L9D1r1nLqryoaNOwg')
