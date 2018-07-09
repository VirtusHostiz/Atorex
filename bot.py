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
        if not message.author.id == "322488685973209109":
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


    if message.content.startswith(prefix+'ban'):
        if not message.author.server_permissions.ban_members:
            ban_embed = discord.Embed(
                title="Você não tem permissão necessárias para utilizar este comando.",
                color=0xFF000
            )
            ban_embed.set_footer(
                text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator)
            )
            return await client.send_message(message.channel, embed=ban_embed)
        try:
            usuario = message.mentions[0]
            canal = client.get_channel("465673373201203210")
            ban_embed02 = discord.Embed(
                title="Usuário banido com sucesso do Discord!",
                color=0xFF000
            )
            ban_embed02.set_footer(
                text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator)
            )
            ban_embed03 = discord.Embed(
                title="Usuário banido!",
                color=0xFF000
            )
            ban_embed03.add_field(
                name="Usuário:",
                value=usuario
            )
            ban_embed03.add_field(
                name="ID do usuário:",
                value=usuario.id
            )
            ban_embed03.add_field(
                name="Motivo:",
                value=message.content[27:]
            )
            ban_embed03.add_field(
                name="Autor:",
                value=message.author.mention
            )
            await client.send_message(message.channel, embed=ban_embed02)
            await client.send_message(canal, embed=ban_embed03)
            await client.ban(usuario, delete_message_days=7)
        except:
            ban_embed04 = discord.Embed(
                title="Utilize o comando: '/ban @usuário <motivo>'.",
                color=0xFF000
            )
            ban_embed04.set_footer(
                text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator)
            )
            await client.send_message(message.channel, embed=ban_embed04)



client.run('NDY0NjA0NDczOTMxODU3OTIx.DiBYJw.S2iTn7TXy7L9D1r1nLqryoaNOwg')