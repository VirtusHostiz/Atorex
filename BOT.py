import discord
import json
import requests
import aiohttp
import time
from time import *

client = discord.Client()
prefix = "/"

@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name='yWilliam#7959', type=2))
    print('[BOT ONLINE]')



@client.event
async def on_message(message):
    if message.content.startswith(prefix+'reiniciar'):
        if not message.author.id == "322488685973209109":
            reiniciar_embed = discord.Embed(title="Você não tem permissões necessárias para utilizar este comando.", color=0xFF0000)
            reiniciar_embed.set_footer(text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
            return await client.send_message(message.channel, embed=reiniciar_embed)
        try:
            reiniciar_embed02 = discord.Embed(title=":pushpin: Reiniciando...", color=0x00FF00)
            reiniciar_embed02.set_footer(icon_url=message.author.avatar_url, text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
            await client.send_message(message.channel, embed=reiniciar_embed02)
            os.system("python BOT.py reload")
        finally:
            pass


    if message.content.lower().startswith(prefix+'testar'):
        if not message.author.id == "322488685973209109":
            testar_embed = discord.Embed(title="Você não tem permissões necessárias para utilizar este comando.", color=0xFF0000)
            testar_embed.set_footer(text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
            return await client.send_message(message.channel, embed=testar_embed)
        try:
            await client.send_message(message.channel, str(eval(message.content[8:])))
        except Exception as e:
            await client.send_message(message.channel, repr(e))
        finally:
            pass


    if message.content.startswith(prefix+'rankup'):
        a = requests.get('https://mcapi.xdefcon.com/server/pingrankup.mcpe.network:25615/full/json').json()
        b = requests.get('https://api.minetools.eu/query/pingrankup.mcpe.network/25615').json()
        tempo01 = time.perf_counter()
        await client.send_typing(canal)
        tempo02 = time.perf_counter()
        if a['serverStatus'] == "online":
            online = a['players']
            maximo = a['maxplayers']
            ping = a['ping']
            jogadores = b['Playerlist']
            rankup_embed = discord.Embed(title="⚔️ Rankup ⚔️", color=0x00BFFF)
            rankup_embed.add_field(name="IP:", value="jogar.atorexmc.com")
            rankup_embed.add_field(name="Status:", value="Online")
            rankup_embed.add_field(name="Jogando:", value="{}/{}".format(online, maximo))
            rankup_embed.add_field(name="Ping:", value="{}ms".format(round((tempo02 - tempo01) * 1000)))
            rankup_embed.add_field(name="Versão:", value="1.8.x")
            rankup_embed.add_field(name="Jogadores online:", value="{}".format(', '.join(jogadores)))
            rankup_embed.set_thumbnail(url="https://i.imgur.com/Cy4vDsc.png")
            rankup_embed.set_footer(icon_url=message.author.avatar_url, text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
            await client.send_message(message.channel, embed=rankup_embed)



client.run('NDcyODY4NzA0OTUxMDc0ODE4.Dj5o_g.qiUTDKB2Yfjp9SX9OlbRC7atv-E')