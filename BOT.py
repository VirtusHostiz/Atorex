import discord
import os
import asyncio
import time
import datetime
from random import *

client = discord.Client()
prefix = "/"

msg_id = None
msg_user = None

@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name=prefix+'comandos', type=2))
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


    if message.content.lower().startswith(prefix+'comandos'):
        comandos_embed = discord.Embed(title=":regional_indicator_a: :regional_indicator_t: :regional_indicator_o: :regional_indicator_r: :regional_indicator_e: :regional_indicator_x:", description="• :gear: **Usuários** \n\n• :tools: **Staff**\n\n• :robot: **yWilliam**", color=0x00BFFF)
        comandos_embed.set_thumbnail(url="https://i.imgur.com/P9o8NUE.png")
        comandos_embed.set_footer(icon_url=message.author.avatar_url, text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
        botmsg = await client.send_message(message.channel, embed=comandos_embed)
        await client.add_reaction(botmsg, "⚙")
        await client.add_reaction(botmsg, "🛠")
        await client.add_reaction(botmsg, "🤖")
        await asyncio.sleep(2)
        global msg_id
        msg_id = botmsg.id
        global msg_user
        msg_user = message.author


    if message.content.lower().startswith(prefix+'jogar'):
        jogar_embed = discord.Embed(title=":regional_indicator_a: :regional_indicator_t: :regional_indicator_o: :regional_indicator_r: :regional_indicator_e: :regional_indicator_x:", color=0x00BFFF)
        jogar_embed.add_field(name="Para jogar utilize o IP:", value="ATOREXMC.NET", inline=False)
        jogar_embed.add_field(name="Versão:", value="1.8.x", inline=False)
        jogar_embed.set_footer(icon_url=message.author.avatar_url, text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
        await client.send_message(message.channel, embed=jogar_embed)


    if message.content.lower().startswith(prefix+'site'):
        loja_embed = discord.Embed(title=":regional_indicator_a: :regional_indicator_t: :regional_indicator_o: :regional_indicator_r: :regional_indicator_e: :regional_indicator_x:", color=0x00BFFF)
        loja_embed.add_field(name="Acesse nosso site:", value="http://atorexmc.com/", inline=False)
        loja_embed.set_footer(icon_url=message.author.avatar_url, text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
        await client.send_message(message.channel, embed=loja_embed)


    if message.content.lower().startswith(prefix+'form'):
        form_embed = discord.Embed(title="Formulário: https://www.atorexmc.com/formulario.html", color=0x00BFFF)
        form_embed.set_footer(icon_url=message.author.avatar_url, text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
        await client.send_message(message.channel, embed=form_embed)


    if message.content.lower().startswith(prefix+'ping'):
        canal = message.channel
        tempo01 = time.perf_counter()
        await client.send_typing(canal)
        tempo02 = time.perf_counter()
        ping_embed = discord.Embed(title="Pong!", description="🏓 Ping - {}ms".format(round((tempo02 - tempo01) * 1000)), color=0x00BFFF)
        ping_embed.set_footer(icon_url=message.author.avatar_url, text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
        await client.send_message(message.channel, embed=ping_embed)


    if message.content.lower().startswith(prefix+'convidar'):
        convite = await client.create_invite(message.channel, max_uses=0, max_age=0)
        covite_embed = discord.Embed(title="📬 Convite gerado!", description="Link : {}\n".format(convite), color=0x00BFFF)
        covite_embed.add_field(name="Canal:", value=convite.channel)
        covite_embed.set_footer(icon_url=message.author.avatar_url, text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
        await client.send_message(message.channel, embed=covite_embed)


    if message.content.lower().startswith(prefix+'denunciar'):
        if not message.content[33:]:
            denunciar_embed = discord.Embed(title="Utilize o comando: '/denunciar @usuário <motivo>'.", color=0xFF0000)
            denunciar_embed.set_footer(icon_url=message.author.avatar_url, text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
            return await client.send_message(message.channel, embed=denunciar_embed)
        try:
            user = message.mentions[0]
            canal = client.get_channel("464095862318956544")
            denunciar_embed02 = discord.Embed(title="O usuário foi denunciado com sucesso no servidor Discord!", color=0x00BFFF)
            denunciar_embed02.set_footer(icon_url=message.author.avatar_url, text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
            denunciar_embed03 = discord.Embed(title="Usuário denunciado!", color=0xFF0000)
            denunciar_embed03.add_field(name="Usuário:", value=user, inline=False)
            denunciar_embed03.add_field(name="ID do usuário:", value=user.id, inline=False)
            denunciar_embed03.add_field(name="Motivo:", value=message.content[33:], inline=False)
            denunciar_embed03.add_field(name="Autor:", value=message.author.mention, inline=False)
            await client.send_message(message.channel, embed=denunciar_embed02)
            await client.send_message(canal, embed=denunciar_embed03)
        except discord.errors.Forbidden:
            denunciar_embed04 = discord.Embed(title="Utilize o comando: '/denunciar @usuário <motivo>'.", color=0xFF0000)
            denunciar_embed04.set_footer(icon_url=message.author.avatar_url, text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
            return await client.send_message(message.channel, embed=denunciar_embed04)
        finally:
            pass


    if message.content.lower().startswith(prefix+'sugerir'):
        if not message.content[9:]:
            denunciar_embed = discord.Embed(title="Utilize o comando: '/sugerir <sugestão>'.", color=0xFF0000)
            denunciar_embed.set_footer(icon_url=message.author.avatar_url, text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
            return await client.send_message(message.channel, embed=denunciar_embed)
        try:
            canal = client.get_channel("466708423409664031")
            denunciar_embed02 = discord.Embed(title="Sua sugestão foi enviada com sucesso!", color=0x00BFFF)
            denunciar_embed02.set_footer(icon_url=message.author.avatar_url, text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
            denunciar_embed03 = discord.Embed(title="Nova sugestão!", color=0xFF0000)
            denunciar_embed03.add_field(name="Sugestão:", value=message.content[8:], inline=False)
            denunciar_embed03.add_field(name="Autor:", value=message.author.mention, inline=False)
            await client.send_message(message.channel, embed=denunciar_embed02)
            await client.send_message(canal, embed=denunciar_embed03)
        except discord.errors.Forbidden:
            denunciar_embed04 = discord.Embed(title="Utilize o comando: '/sugerir <sugestão>'.", color=0xFF0000)
            denunciar_embed04.set_footer(icon_url=message.author.avatar_url, text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
            return await client.send_message(message.channel, embed=denunciar_embed04)
        finally:
            pass


    if message.content.lower().startswith(prefix+'solicitar'):
        if not message.content[11:]:
            denunciar_embed = discord.Embed(title="Utilize o comando: '/soliciar <link do vídeo>'.", color=0xFF0000)
            denunciar_embed.set_footer(icon_url=message.author.avatar_url, text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
            return await client.send_message(message.channel, embed=denunciar_embed)
        try:
            canal = client.get_channel("467135084076597249")
            denunciar_embed02 = discord.Embed(title="Sua solicitação foi enviada com sucesso!", color=0x00BFFF)
            denunciar_embed02.set_footer(icon_url=message.author.avatar_url, text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
            denunciar_embed03 = discord.Embed(title="Nova solicitação de TAG!", color=0xFF0000)
            denunciar_embed03.add_field(name="Link do vídeo:", value=message.content[11:], inline=False)
            denunciar_embed03.add_field(name="Autor:", value=message.author.mention, inline=False)
            await client.send_message(message.channel, embed=denunciar_embed02)
            await client.send_message(canal, embed=denunciar_embed03)
        except discord.errors.Forbidden:
            denunciar_embed04 = discord.Embed(title="Utilize o comando: '/solicitar <link do vídeo>'.", color=0xFF0000)
            denunciar_embed04.set_footer(icon_url=message.author.avatar_url, text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
            return await client.send_message(message.channel, embed=denunciar_embed04)
        finally:
            pass


    if message.content.lower().startswith(prefix+'parceria'):
        if not message.content[10:]:
            parceria_embed = discord.Embed(title="Utilize o comando: '/parceria <mensagem>'.", color=0xFF0000)
            parceria_embed.set_footer(icon_url=message.author.avatar_url, text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
            return await client.send_message(message.channel, embed=parceria_embed)
        try:
            canal = client.get_channel("468922164868022299")
            parceria_embed02 = discord.Embed(title="Sua solicitação foi enviada com sucesso!", color=0x00BFFF)
            parceria_embed02.set_footer(icon_url=message.author.avatar_url, text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
            parceria_embed03 = discord.Embed(title="Nova solicitação de parceria!", color=0xFF0000)
            parceria_embed03.add_field(name="Mensagem:", value=message.content[10:], inline=False)
            parceria_embed03.add_field(name="Autor:", value=message.author.mention, inline=False)
            await client.send_message(message.channel, embed=parceria_embed02)
            await client.send_message(canal, embed=parceria_embed03)
        except discord.errors.Forbidden:
            parceria_embed04 = discord.Embed(title="Utilize o comando: '/parceria <mensagem>'.", color=0xFF0000)
            parceria_embed04.set_footer(icon_url=message.author.avatar_url, text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
            return await client.send_message(message.channel, embed=parceria_embed04)
        finally:
            pass


    if message.content.lower().startswith(prefix+'moeda'):
        escolher = randint(1, 2)
        if escolher == 1:
            await client.add_reaction(message, '😀')
        if escolher == 2:
            await client.add_reaction(message, '👑')


    if message.content.lower().startswith(prefix+'8ball'):
        if not message.content[7:]:
            oitoball_embed = discord.Embed(title="Utilize o comando: '/8ball <pergunta>'.", color=0xFF0000)
            oitoball_embed.set_footer(icon_url=message.author.avatar_url, text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
            return await client.send_message(message.channel, embed=oitoball_embed)
        try:
            respostas = ['Sim','Não','Talvez','Nunca','Claro']
            resposta = choice(respostas)
            mensagem = message.content[7:]
            oitoball_embed02 = discord.Embed(color=0x00BFFF)
            oitoball_embed02.add_field(name="Pergunta:", value='{}'.format(mensagem),inline=False)
            oitoball_embed02.add_field(name="Resposta:", value=resposta,inline=False)
            oitoball_embed02.set_thumbnail(url="https://i.imgur.com/P9o8NUE.png")
            oitoball_embed02.set_footer(icon_url=message.author.avatar_url, text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
            await client.send_message(message.channel, embed=oitoball_embed02)
            await client.delete_message(message)
        finally:
            pass   


    if message.content.lower().startswith(prefix+'clear'):
        if not message.author.server_permissions.manage_messages:
            clear_embed = discord.Embed(title="Você não tem permissões necessárias para utilizar este comando.", color=0xFF0000)
            clear_embed.set_footer(icon_url=message.author.avatar_url, text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
            return await client.send_message(message.channel, embed=clear_embed)
        if not message.content[7:]:
            clear_embed02 = discord.Embed(title="Utilize o comando: '/clear <quantidade>'.", color=0xFF0000)
            clear_embed02.set_footer(icon_url=message.author.avatar_url, text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
            return await client.send_message(message.channel, embed=clear_embed02)
        try:
            lim = int(message.content[7:]) + 1
            clear_embed03 = discord.Embed(title=":pencil: Foram apagadas {} mensagens com sucesso!".format(lim), color=0x00FF00)
            clear_embed03.set_footer(icon_url=message.author.avatar_url, text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
            await client.purge_from(message.channel, limit=lim)
            await client.send_message(message.channel, embed=clear_embed03)
        finally:
            pass


    if message.content.lower().startswith(prefix+'falar'):
        if not message.author.server_permissions.ban_members:
            falar_embed = discord.Embed(title="Você não tem permissões necessárias para utilizar este comando.", color=0xFF0000)
            falar_embed.set_footer(icon_url=message.author.avatar_url, text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
            return await client.send_message(message.channel, embed=falar_embed)
        try:
            mensagem = str(message.content).replace(prefix+"falar", "")
            falar_embed02 = discord.Embed(title=mensagem, color=0x00BFFF)
            await client.delete_message(message)
            await client.send_message(message.channel, embed=falar_embed02)
        except:
            falar_embed03 = discord.Embed(title="Utilize o comando: '/falar <mensagem>'.", color=0xFF0000)
            falar_embed03.set_footer(icon_url=message.author.avatar_url, text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
            return await client.send_message(message.channel, embed=falar_embed03)
        finally:
            pass


    if message.content.lower().startswith(prefix+'ban'):
        if not message.author.server_permissions.ban_members:
            ban_embed = discord.Embed(title="Você não tem permissões necessárias para utilizar este comando.", color=0xFF0000)
            ban_embed.set_footer(icon_url=message.author.avatar_url, text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
            return await client.send_message(message.channel, embed=ban_embed)
        if not message.content[27:]:
            ban_embed04 = discord.Embed(title="Utilize o comando: '/ban @usuário <motivo>'.", color=0xFF0000)
            ban_embed04.set_footer(icon_url=message.author.avatar_url, text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
            return await client.send_message(message.channel, embed=ban_embed04)
        try:
            user = message.mentions[0]
            canal = client.get_channel("465673373201203210")
            ban_embed02 = discord.Embed(title="O usuário foi banido com sucesso no servidor Discord!", color=0x00BFFF)
            ban_embed02.set_footer(icon_url=message.author.avatar_url, text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
            ban_embed03 = discord.Embed(title="Usuário banido!", color=0xFF0000)
            ban_embed03.add_field(name="Usuário:", value=user, inline=False)
            ban_embed03.add_field(name="ID do usuário:", value=user.id, inline=False)
            ban_embed03.add_field(name="Motivo:", value=message.content[27:], inline=False)
            ban_embed03.add_field(name="Autor:", value=message.author.mention, inline=False)
            await client.ban(user, delete_message_days=7)
            await client.send_message(message.channel, embed=ban_embed02)
            await client.send_message(canal, embed=ban_embed03)
        except discord.errors.Forbidden:
            ban_embed04 = discord.Embed(title="Utilize o comando: '/ban @usuário <motivo>'.", color=0xFF0000)
            ban_embed04.set_footer(icon_url=message.author.avatar_url, text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
            return await client.send_message(message.channel, embed=ban_embed04)
        finally:
            pass


    if message.content.lower().startswith(prefix+'unban'):
        if not message.author.server_permissions.ban_members:
            unban_embed = discord.Embed(title="Você não tem permissões necessárias para utilizar este comando.", color=0xFF0000)
            unban_embed.set_footer(icon_url=message.author.avatar_url, text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
            return await client.send_message(message.channel, embed=unban_embed)
        try:
            uid = message.content[7:]
            user = await client.get_user_info(uid)
            canal = client.get_channel("465673373201203210")
            unban_embed02 = discord.Embed(title="O usuário foi desbanido com sucesso no servidor Discord!", color=0x00BFFF)
            unban_embed02.set_footer(icon_url=message.author.avatar_url, text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
            unban_embed03 = discord.Embed(title="Usuário desbanido!", color=0x00FF00)
            unban_embed03.add_field(name="Usuário:", value=user, inline=False)
            unban_embed03.add_field(name="ID do usuário:", value=user.id, inline=False)
            unban_embed03.add_field(name="Autor:", value=message.author.mention, inline=False)
            await client.unban(message.server, user)
            await client.send_message(message.channel, embed=unban_embed02)
            await client.send_message(canal, embed=unban_embed03)
        except:
            unban_embed04 = discord.Embed(title="Utilize o comando: '/unban <ID do usuário>'.", color=0xFF0000)
            unban_embed04.set_footer(icon_url=message.author.avatar_url, text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
            return await client.send_message(message.channel, embed=unban_embed04)
        finally:
            pass


    if message.content.lower().startswith(prefix+'kick'):
        if not message.author.server_permissions.kick_members:
            kick_embed = discord.Embed(title="Você não tem permissões necessárias para utilizar este comando.", color=0xFF0000)
            kick_embed.set_footer(icon_url=message.author.avatar_url, text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
            return await client.send_message(message.channel, embed=kick_embed)
        if not message.content[28:]:
            kick_embed02 = discord.Embed(title="Utilize o comando: '/kick @usuário <motivo>'.", color=0xFF0000)
            kick_embed02.set_footer(icon_url=message.author.avatar_url, text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
            return await client.send_message(message.channel, embed=kick_embed02)
        try:
            user = message.mentions[0]
            canal = client.get_channel("465673373201203210")
            kick_embed03 = discord.Embed(title="O usuário foi expulso com sucesso no servidor Discord!", color=0x00BFFF)
            kick_embed03.set_footer(icon_url=message.author.avatar_url, text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
            kick_embed04 = discord.Embed(title="Usuário expulso!", color=0xFF0000)
            kick_embed04.add_field(name="Usuário:", value=user, inline=False)
            kick_embed04.add_field(name="ID do usuário:", value=user.id, inline=False)
            kick_embed04.add_field(name="Motivo:", value=message.content[28:], inline=False)
            kick_embed04.add_field(name="Autor:", value=message.author.mention, inline=False)
            await client.kick(user)
            await client.send_message(message.channel, embed=kick_embed03)
            await client.send_message(canal, embed=kick_embed04)
        except discord.errors.Forbidden:
            kick_embed05 = discord.Embed(title="Utilize o comando: '/kick @usuário <motivo>'.", color=0xFF0000)
            kick_embed05.set_footer(icon_url=message.author.avatar_url, text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
            return await client.send_message(message.channel, embed=kick_embed05)
        finally:
            pass


    if message.content.lower().startswith(prefix+'mute'):
        if not message.author.server_permissions.kick_members:
            mute_embed = discord.Embed(title="Você não tem permissões necessárias para utilizar este comando.", color=0xFF0000)
            mute_embed.set_footer(icon_url=message.author.avatar_url, text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
            return await client.send_message(message.channel, embed=mute_embed)
        if not message.content[28:]:
            mute_embed02 = discord.Embed(title="Utilize o comando: '/mute @usuário <motivo>'.", color=0xFF0000)
            mute_embed02.set_footer(icon_url=message.author.avatar_url, text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
            return await client.send_message(message.channel, embed=mute_embed02)
        try:
            user = message.mentions[0]
            canal = client.get_channel("465673373201203210")
            cargo = discord.utils.find(lambda r: r.name == "Mutado", message.server.roles)
            mute_embed03 = discord.Embed(title="O usuário foi mutado com sucesso no servidor Discord!", color=0x00BFFF)
            mute_embed03.set_footer(icon_url=message.author.avatar_url, text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
            mute_embed04 = discord.Embed(title="Usuário mutado!", color=0xFF0000)
            mute_embed04.add_field(name="Usuário:", value=user, inline=False)
            mute_embed04.add_field(name="ID do usuário:", value=user.id, inline=False)
            mute_embed04.add_field(name="Motivo:", value=message.content[28:], inline=False)
            mute_embed04.add_field(name="Autor:", value=message.author.mention, inline=False)
            await client.add_roles(user, cargo)
            await client.send_message(message.channel, embed=mute_embed03)
            await client.send_message(canal, embed=mute_embed04)
        except discord.errors.Forbidden:
            mute_embed05 = discord.Embed(title="Utilize o comando: '/mute @usuário <motivo>'.", color=0xFF0000)
            mute_embed05.set_footer(icon_url=message.author.avatar_url, text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
            return await client.send_message(message.channel, embed=mute_embed05)
        finally:
            pass


    if message.content.lower().startswith(prefix+'unmute'):
        if not message.author.server_permissions.kick_members:
            unmute_embed = discord.Embed(title="Você não tem permissões necessárias para utilizar este comando.", color=0xFF0000)
            unmute_embed.set_footer(icon_url=message.author.avatar_url, text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
            return await client.send_message(message.channel, embed=unmute_embed)
        try:
            user = message.mentions[0]
            canal = client.get_channel("465673373201203210")
            cargo = discord.utils.find(lambda r: r.name == "Mutado", message.server.roles)
            unmute_embed02 = discord.Embed(title="O usuário foi desmutado com sucesso no servidor Discord!", color=0x00BFFF)
            unmute_embed02.set_footer(icon_url=message.author.avatar_url, text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
            unmute_embed03 = discord.Embed(title="Usuário desmutado!", color=0x00FF00)
            unmute_embed03.add_field(name="Usuário:", value=user, inline=False)
            unmute_embed03.add_field(name="ID do usuário:", value=user.id, inline=False)
            unmute_embed03.add_field(name="Autor:", value=message.author.mention, inline=False)
            await client.remove_roles(user, cargo)
            await client.send_message(message.channel, embed=unmute_embed02)
            await client.send_message(canal, embed=unmute_embed03)
        except IndexError:
            unmute_embed04 = discord.Embed(title="Utilize o comando: '/unmute @usuário'.", color=0xFF0000)
            unmute_embed04.set_footer(icon_url=message.author.avatar_url, text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
            return await client.send_message(message.channel, embed=unmute_embed04)
        finally:
            pass


    if message.content.lower().startswith(prefix+'warn'):
        if not message.author.server_permissions.kick_members:
            warn_embed = discord.Embed(title="Você não tem permissões necessárias para utilizar este comando.", color=0xFF0000)
            warn_embed.set_footer(icon_url=message.author.avatar_url, text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
            return await client.send_message(message.channel, embed=warn_embed)
        if not message.content[28:]:
            warn_embed02 = discord.Embed(title="Utilize o comando: '/warn @usuário <motivo>'.", color=0xFF0000)
            warn_embed02.set_footer(icon_url=message.author.avatar_url, text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
            return await client.send_message(message.channel, embed=warn_embed02)
        try:
            user = message.mentions[0]
            canal = client.get_channel("465673373201203210")
            warn_embed03 = discord.Embed(title="O usuário foi alertado com sucesso no servidor Discord!", color=0x00BFFF)
            warn_embed03.set_footer(icon_url=message.author.avatar_url, text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
            warn_embed04 = discord.Embed(title="Você foi alertado!", color=0xFF0000)
            warn_embed04.add_field(name="Motivo:", value=message.content[28:], inline=False)
            warn_embed04.add_field(name="Autor:", value=message.author.mention, inline=False)
            warn_embed05 = discord.Embed(title="Usuário alertado!", color=0xFF0000)
            warn_embed05.add_field(name="Usuário:", value=user, inline=False)
            warn_embed05.add_field(name="ID do usuário:", value=user.id, inline=False)
            warn_embed05.add_field(name="Motivo:", value=message.content[28:], inline=False)
            warn_embed05.add_field(name="Autor:", value=message.author.mention, inline=False)
            await client.send_message(message.channel, embed=warn_embed03)
            await client.send_message(user, "{},".format(user.mention))
            await client.send_message(user, embed=warn_embed04)
            await client.send_message(canal, embed=warn_embed05)
        except discord.errors.Forbidden:
            warn_embed06 = discord.Embed(title="Utilize o comando: '/warn @usuário <motivo>'.", color=0xFF0000)
            warn_embed06.set_footer(icon_url=message.author.avatar_url, text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
            return await client.send_message(message.channel, embed=warn_embed06)
        finally:
            pass


    if message.content.lower().startswith(prefix+'votar'):
        if not message.author.server_permissions.ban_members:
            votar_embed = discord.Embed(title="Você não tem permissões necessárias para utilizar este comando.", color=0xFF0000)
            votar_embed.set_footer(icon_url=message.author.avatar_url, text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
            return await client.send_message(message.channel, embed=votar_embed)
        if not message.content[7:]:
            warn_embed02 = discord.Embed(title="Utilize o comando: '/votar <assunto>'.", color=0xFF0000)
            warn_embed02.set_footer(icon_url=message.author.avatar_url, text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
            return await client.send_message(message.channel, embed=warn_embed02)
        try:
            canal = client.get_channel("464097786191806474")
            votar_embed03 = discord.Embed(title="Votação iniciado com sucesso no servidor Discord!", color=0x00BFFF)
            votar_embed03.set_footer(icon_url=message.author.avatar_url, text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
            votar_embed04 = discord.Embed(title="Votação!", description="O que vocês acham sobre: {}?".format(message.content[7:]), color=0x00BFFF)
            votar_embed04.set_footer(icon_url=message.author.avatar_url, text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
            await client.send_message(message.channel, embed=votar_embed03)
            votar = await client.send_message(canal, embed=votar_embed04)
            await client.add_reaction(votar, "✅")
            await client.add_reaction(votar, "❎")
        finally:
            pass



@client.event
async def on_reaction_add(reaction, user):
    msg = reaction.message
    if reaction.emoji == "⚙" and msg.id == msg_id:
        comandos02_embed = discord.Embed(title="⚙ Comandos dos usuário:", description="ㅤ", color=0x00BFFF)
        comandos02_embed.set_thumbnail(url="https://i.imgur.com/P9o8NUE.png")
        comandos02_embed.add_field(name="• [/comandos] - Comandos do BOT.", value="• [/jogar] - Como jogar.", inline=False)
        comandos02_embed.add_field(name="• [/site] - Site do servidor.", value="• [/form] - Formulário para ser staff.", inline=False)
        comandos02_embed.add_field(name="• [/ping] - Saber seu ping.", value="• [/convidar] - Convide pessoas.", inline=False)
        comandos02_embed.add_field(name="• [/denunciar @usuário <motivo>] - Denuncie algum usuário.", value="• [/sugerir <sugestão>] - Sugira mudanças.", inline=False)
        comandos02_embed.add_field(name="• [/solicitar <link do vídeo>] - Solicite sua tag.", value="• [/parceria <mensagem>] - Solicite uma parceria.", inline=False)
        await client.send_message(user, embed=comandos02_embed)


    if reaction.emoji == "🛠" and msg.id == msg_id:
        comandos04_embed = discord.Embed(title="🛠 Comandos da staff:", description="ㅤ", color=0x00BFFF)
        comandos04_embed.set_thumbnail(url="https://i.imgur.com/P9o8NUE.png")
        comandos04_embed.add_field(name="• [/clear <quantidade>] - Apagar mensagens.", value="• [/falar <mensagem>] - Faça o BOT falar.", inline=False)
        comandos04_embed.add_field(name="• [/ban @usuário <motivo>] - Banir um usuário.", value="• [/unban <ID do usuário>] - Desbanir um usuário.", inline=False)
        comandos04_embed.add_field(name="• [/kick @usuário <motivo>] - Expulsar um usuário.", value="• [/mute @usuário <motivo>] - Mutar um usuário.", inline=False)
        comandos04_embed.add_field(name="• [/unmute @usuário] - Desmutar um usuário.", value="• [/warn @usuário <motivo>] - Alertar um usuário,.", inline=False)
        comandos04_embed.add_field(name="• [/votar <assunto>] - Criar uma votação.", value="ㅤ", inline=False)
        await client.send_message(user, embed=comandos04_embed)


    if reaction.emoji == "🤖" and msg.id == msg_id:
        comandos04_embed = discord.Embed(title="🤖 Comandos do yWilliam:", description="ㅤ", color=0x00BFFF)
        comandos04_embed.set_thumbnail(url="https://i.imgur.com/P9o8NUE.png")
        comandos04_embed.add_field(name="• [/reiniciar] - Reiniciar o BOT.", value="ㅤ", inline=False)
        await client.send_message(user, embed=comandos04_embed)



@client.event
async def on_member_join(member):
    canal = client.get_channel("467096925087465489")
    cargo = discord.utils.find(lambda r: r.name == "Membro", member.server.roles)
    entrar_embed = discord.Embed(title=":regional_indicator_a: :regional_indicator_t: :regional_indicator_o: :regional_indicator_r: :regional_indicator_e: :regional_indicator_x:", description="**{}** seja bem-vindo(a) ao servidor Discord do **Atorex Network**!".format(member.mention), color=0x00BFFF)
    entrar_embed.add_field(name="IP do servidor: ATOREXMC.NET", value="Site do servidor: **http://atorexmc.com/**", inline=False)
    entrar_embed.add_field(name="Formulário: Não disponível no momento.", value="Utilize **/comandos** para saber os comandos do BOT.", inline=False)
    await client.send_message(canal, embed=entrar_embed)
    await client.add_roles(member, cargo)



client.run('NDY3MTA0MzkwODA1ODQ4MDk0.DilwYQ.BU9JpZPsMlAcs2-Petl-TrIg238')
