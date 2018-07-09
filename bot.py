import discord
import os
import asyncio
import time
import datetime

client = discord.Client()
prefix = "/"

@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name=prefix+'comandos', type=2))
    print('[BOT ONLINE]')


@client.event
async def on_message(message):
    if message.content.startswith(prefix+'comandos'):
        await client.send_message(message.channel, "{},\n```diff\n- Este comando não está disponível no momento.\n```".format(message.author.mention))


    if message.content.startswith(prefix+'reiniciar'):
        if not message.author.id == "32248868597320910":
            reiniciar_embed = discord.Embed(
                title="Você não tem permissões necessárias para utilizar este comando.",
                color=0x00FF00
            )
            reiniciar_embed.set_footer(
                text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator)
            )
            return await client.send_message(message.channel, embed=reiniciar_embed)
        try:
            reiniciar_embed02 = discord.Embed(
                title=":pushpin: Reiniciando...",
                color=0x00FF00
            )
            reiniciar_embed02.set_footer(
                text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator)
            )
            await client.send_message(message.channel, embed=reiniciar_embed02)
            os.system("python bot.py reload")
        finally:
            pass


    if message.content.startswith(prefix+'ping'):
        canal = message.channel
        tempo01 = time.perf_counter()
        await client.send_typing(canal)
        tempo02 = time.perf_counter()
        ping_embed = discord.Embed(
            title="Pong!",
            description="🏓 Ping - {}ms".format(round((tempo02 - tempo01) * 1000)),
            color=0x00BFFF
        )
        await client.send_message(message.channel, embed=ping_embed)



client.run('NDY0NjA0NDczOTMxODU3OTIx.DiBYJw.S2iTn7TXy7L9D1r1nLqryoaNOwg')