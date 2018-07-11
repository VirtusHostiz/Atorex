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
            os.system("python bot.py restart")
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
            ban_embed04 = discord.Embed(title="Utilize o comando: '/ban @usuário <motivo>'.", color=0xFF0000)
            ban_embed04.set_footer(text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
            return await client.send_message(message.channel, embed=ban_embed04)
        try:
            user = message.mentions[0]
            canal = client.get_channel("465673373201203210")
            ban_embed02 = discord.Embed(title="Usuário banido do servidor Discord com sucesso!", color=0x00BFFF)
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
            unban_embed02 = discord.Embed(title="Usuário desbanido do servidor Discord com sucesso!", color=0x00BFFF)
            unban_embed02.set_footer(text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
            unban_embed03 = discord.Embed(title="Usuário desbanido!", color=0x00FF00)
            unban_embed03.add_field(name="Usuário:", value=user)
            unban_embed03.add_field(name="ID do usuário:", value=user.id)
            unban_embed03.add_field(name="Autor:", value=message.author.mention)
            await client.unban(message.server, user)
            await client.send_message(message.channel, embed=unban_embed02)
            await client.send_message(canal, embed=unban_embed03)
        except:
            unban_embed04 = discord.Embed(title="Utilize o comando: '/unban <ID do usuário>'.", color=0xFF0000)
            unban_embed04.set_footer(text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
            return await client.send_message(message.channel, embed=unban_embed04)
        finally:
            pass


    if message.content.lower().startswith(prefix+'kick'):
        if not message.author.server_permissions.kick_members:
            kick_embed = discord.Embed(title="Você não tem permissões necessárias para utilizar este comando.", color=0xFF0000)
            kick_embed.set_footer(text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
            return await client.send_message(message.channel, embed=kick_embed)
        if not message.content[28:]:
            kick_embed02 = discord.Embed(title="Utilize o comando: '/kick @usuário <motivo>'.", color=0xFF0000)
            kick_embed02.set_footer(text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
            return await client.send_message(message.channel, embed=kick_embed02)
        try:
            user = message.mentions[0]
            canal = client.get_channel("465673373201203210")
            kick_embed03 = discord.Embed(title="Usuário expulso do servidor Discord com sucesso!", color=0x00BFFF)
            kick_embed03.set_footer(text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
            kick_embed04 = discord.Embed(title="Usuário expulso!", color=0xFF0000)
            kick_embed04.add_field(name="Usuário:", value=user)
            kick_embed04.add_field(name="ID do usuário:", value=user.id)
            kick_embed04.add_field(name="Motivo:", value=message.content[28:])
            kick_embed04.add_field(name="Autor:", value=message.author.mention)
            await client.kick(user)
            await client.send_message(message.channel, embed=kick_embed03)
            await client.send_message(canal, embed=kick_embed04)
        except discord.errors.Forbidden:
            kick_embed05 = discord.Embed(title="Utilize o comando: '/kick @usuário <motivo>'.", color=0xFF0000)
            kick_embed05.set_footer(text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
            return await client.send_message(message.channel, embed=kick_embed05)
        finally:
            pass


    if message.content.lower().startswith(prefix+'mute'):
        if not message.author.server_permissions.kick_members:
            mute_embed = discord.Embed(title="Você não tem permissões necessárias para utilizar este comando.", color=0xFF0000)
            mute_embed.set_footer(text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
            return await client.send_message(message.channel, embed=mute_embed)
        if not message.content[28:]:
            mute_embed02 = discord.Embed(title="Utilize o comando: '/mute @usuário <motivo>'.", color=0xFF0000)
            mute_embed02.set_footer(text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
            return await client.send_message(message.channel, embed=mute_embed02)
        try:
            user = message.mentions[0]
            canal = client.get_channel("465673373201203210")
            cargo = discord.utils.find(lambda r: r.name == "Mutado", message.server.roles)
            mute_embed03 = discord.Embed(title="Usuário mutado no servidor Discord com sucesso!", color=0x00BFFF)
            mute_embed03.set_footer(text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
            mute_embed04 = discord.Embed(title="Usuário mutado!", color=0xFF0000)
            mute_embed04.add_field(name="Usuário:", value=user)
            mute_embed04.add_field(name="ID do usuário:", value=user.id)
            mute_embed04.add_field(name="Motivo:", value=message.content[28:])
            mute_embed04.add_field(name="Autor:", value=message.author.mention)
            await client.add_roles(user, cargo)
            await client.send_message(message.channel, embed=mute_embed03)
            await client.send_message(canal, embed=mute_embed04)
        except discord.errors.Forbidden:
            mute_embed05 = discord.Embed(title="Utilize o comando: '/mute @usuário <motivo>'.", color=0xFF0000)
            mute_embed05.set_footer(text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
            return await client.send_message(message.channel, embed=mute_embed05)
        finally:
            pass


    if message.content.lower().startswith(prefix+'unmute'):
        if not message.author.server_permissions.kick_members:
            unmute_embed = discord.Embed(title="Você não tem permissões necessárias para utilizar este comando.", color=0xFF0000)
            unmute_embed.set_footer(text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
            return await client.send_message(message.channel, embed=unmute_embed)
        try:
            user = message.mentions[0]
            canal = client.get_channel("465673373201203210")
            cargo = discord.utils.find(lambda r: r.name == "Mutado", message.server.roles)
            unmute_embed02 = discord.Embed(title="Usuário desmutado no servidor Discord com sucesso!", color=0x00BFFF)
            unmute_embed02.set_footer(text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
            unmute_embed03 = discord.Embed(title="Usuário desmutado!", color=0x00FF00)
            unmute_embed03.add_field(name="Usuário:", value=user)
            unmute_embed03.add_field(name="ID do usuário:", value=user.id)
            unmute_embed03.add_field(name="Autor:", value=message.author.mention)
            await client.remove_roles(user, cargo)
            await client.send_message(message.channel, embed=unmute_embed02)
            await client.send_message(canal, embed=unmute_embed03)
        except discord.errors.Forbidden:
            unmute_embed04 = discord.Embed(title="Utilize o comando: '/unmute @usuário'.", color=0xFF0000)
            unmute_embed04.set_footer(text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
            return await client.send_message(message.channel, embed=unmute_embed04)
        finally:
            pass


    if message.content.lower().startswith(prefix+'alertar'):
        if not message.author.server_permissions.kick_members:
            kick_embed = discord.Embed(title="Você não tem permissões necessárias para utilizar este comando.", color=0xFF0000)
            kick_embed.set_footer(text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
            return await client.send_message(message.channel, embed=kick_embed)
        if not message.content[31:]:
            kick_embed02 = discord.Embed(title="Utilize o comando: '/alertar @usuário <motivo>'.", color=0xFF0000)
            kick_embed02.set_footer(text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
            return await client.send_message(message.channel, embed=kick_embed02)
        try:
            user = message.mentions[0]
            canal = client.get_channel("465673373201203210")
            kick_embed03 = discord.Embed(title="Usuário alertado no servidor Discord com sucesso!", color=0x00BFFF)
            kick_embed03.set_footer(text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
            kick_embed04 = discord.Embed(title="Você foi alertado!", color=0xFF0000)
            kick_embed04.add_field(name="Motivo:", value=message.content[31:])
            kick_embed04.add_field(name="Autor:", value=message.author.mention)
            kick_embed05 = discord.Embed(title="Usuário alertado!", color=0xFF0000)
            kick_embed05.add_field(name="Usuário:", value=user)
            kick_embed05.add_field(name="ID do usuário:", value=user.id)
            kick_embed05.add_field(name="Motivo:", value=message.content[31:])
            kick_embed05.add_field(name="Autor:", value=message.author.mention)
            await client.send_message(message.channel, embed=kick_embed03)
            await client.send_message(user, "{},".format(message.author.mention))
            await client.send_message(user, embed=kick_embed04)
            await client.send_message(canal, embed=kick_embed05)
        except discord.errors.Forbidden:
            kick_embed05 = discord.Embed(title="Utilize o comando: '/alertar @usuário <motivo>'.", color=0xFF0000)
            kick_embed05.set_footer(text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
            return await client.send_message(message.channel, embed=kick_embed05)
        finally:
            pass



client.run('NDY0NjA0NDczOTMxODU3OTIx.DiBYJw.S2iTn7TXy7L9D1r1nLqryoaNOwg')
