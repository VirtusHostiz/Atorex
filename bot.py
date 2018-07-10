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
            reiniciar_embed = discord.Embed(title="Você não tem permissões necessárias para utilizar este comando.", color=0x00FF00)
            reiniciar_embed.set_footer(text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
            return await client.send_message(message.channel, embed=reiniciar_embed)
        try:
            reiniciar_embed02 = discord.Embed(title=":pushpin: Reiniciando...", color=0x00FF00)
            reiniciar_embed02.set_footer(text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
            await client.send_message(message.channel, embed=reiniciar_embed02)
            os.system("python bot.py reload")
        finally:
            pass


    if message.content.startswith(prefix+'falar'):
        if not message.author.server_permissions.kick_members:
            falar_embed = discord.Embed(title="Você não tem permissões necessárias para utilizar este comando.", color=0xFF0000)
            falar_embed.set_footer(text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
            return await client.send_message(message.channel, embed=falar_embed)
        try:
            mensagem = str(message.content).replace(prefix+"falar", "")
            falar_embed02 = discord.Embed(title=mensagem, color=0x00BFFF)
            await client.delete_message(message)
            await client.send_message(message.channel, embed=falar_embed02)
        except:
            falar_embed03 = discord.Embed(title="Utilize o comando: '/falar <mensagem>'.", color=0xFF0000)
            falar_embed03.set_footer(text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
            return await client.send_message(message.channel, embed=falar_embed03)
        finally:
            pass


    if message.content.startswith(prefix+'clear'):
        if not message.author.server_permissions.manage_messages:
            clear_embed = discord.Embed(title="Você não tem permissões necessárias para utilizar este comando.", color=0xFF0000)
            clear_embed.set_footer(text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
            return await client.send_message(message.channel, embed=clear_embed)
        try:
            limpar = int(message.content[7:]) + 1
            clear_embed02 = discord.Embed(title=":pencil: Foram apagadas {} mensagens com sucesso!".format(limpar), color=0x00FF00)
            clear_embed02.set_footer(text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
            await client.purge_from(message.channel, limit=limpar)
            await client.send_message(message.channel, embed=clear_embed02)
        except:
            clear_embed03 = discord.Embed(title="Utilize o comando: '/clear <quantidade de mensagens>'.", color=0xFF0000)
            clear_embed03.set_footer(text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
            return await client.send_message(message.channel, embed=clear_embed03)
        finally:
            pass


    if message.content.startswith(prefix+'ping'):
        canal = message.channel
        tempo01 = time.perf_counter()
        await client.send_typing(canal)
        tempo02 = time.perf_counter()
        ping_embed = discord.Embed(title="Pong!", description="🏓 Ping - {}ms".format(round((tempo02 - tempo01) * 1000)), color=0x00BFFF)
        await client.send_message(message.channel, embed=ping_embed)


    if message.content.lower().startswith(prefix+'ban'):
        if not message.author.server_permissions.ban_members:
            ban_embed = discord.Embed(title="Você não tem permissões necessárias para utilizar este comando.", color=0xFF0000)
            ban_embed.set_footer(text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
            return await client.send_message(message.channel, embed=ban_embed)
        if not message.content[27:]:
            return await client.send_message(message.channel, "Insira um motivo")
        try:
            user = message.mentions[0]
            canal = client.get_channel("465673373201203210")
            ban_embed02 = discord.Embed(title="Usuário banido com sucesso do servidor Discord!", color=0x00BFFF)
            ban_embed02.set_footer(text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
            ban_embed03 = discord.Embed(title="Usuário banido!", color=0xFF0000)
            ban_embed03.add_field(name="Usuário:", value=user)
            ban_embed03.add_field(name="ID do usuário:", value=user.id)
            ban_embed03.add_field(name="Motivo:", value=message.content[27:])
            ban_embed03.add_field(name="Autor:", value=message.author.mention)
            await client.ban(user, delete_message_days=7)
            await client.send_message(message.channel, embed=ban_embed02)
            await client.send_message(canal, embed=ban_embed03)
        except discord.errors.Forbidden:
            ban_embed04 = discord.Embed(title="Utilize o comando: '/ban @usuário <motivo>'.", color=0xFF0000)
            ban_embed04.set_footer(text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
            return await client.send_message(message.channel, embed=ban_embed04)
        finally:
            pass


    if message.content.lower().startswith(prefix+'unban'):
        if not message.author.server_permissions.ban_members:
            unban_embed = discord.Embed(title="Você não tem permissões necessárias para utilizar este comando.", color=0xFF0000)
            unban_embed.set_footer(text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
            return await client.send_message(message.channel, embed=unban_embed)
        try:
            uid = message.content[7:]
            user = await client.get_user_info(uid)
            canal = client.get_channel("465673373201203210")
            unban_embed02 = discord.Embed(title="Usuário desbanido com sucesso do servidor Discord!", color=0x00BFFF)
            unban_embed02.set_footer(text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
            await client.send_message(message.channel, embed=unban_embed02)
            unban_embed03 = discord.Embed(title="Usuário desbanido!", color=0x00FF00)
            ban_embed03.add_field(name="Usuário:", value=user)
            unban_embed03.add_field(name="ID do usuário:", value=user.id)
            unban_embed03.add_field(name="Autor:", value=message.author.mention)
            await client.send_message(canal, embed=unban_embed03)
            await client.unban(message.server, user)
        except:
            unban_embed04 = discord.Embed(title="Utilize o comando: '/unban <ID do usuário>'.", color=0xFF0000)
            unban_embed04.set_footer(text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
            return await client.send_message(message.channel, embed=unban_embed04)
        finally:
            pass



client.run('NDY0NjA0NDczOTMxODU3OTIx.DiBYJw.S2iTn7TXy7L9D1r1nLqryoaNOwg')