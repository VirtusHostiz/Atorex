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
    if message.content.startswith(prefix+'reiniciar'):
        if not message.author.id == "322488685973209109":
            reiniciar_embed = discord.Embed(title="Você não tem permissões necessárias para utilizar este comando.", color=0xFF0000)
            reiniciar_embed.set_footer(text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
            return await client.send_message(message.channel, embed=reiniciar_embed)
        try:
            reiniciar_embed02 = discord.Embed(title=":pushpin: Reiniciando...", color=0x00FF00)
            reiniciar_embed02.set_footer(text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
            await client.send_message(message.channel, embed=reiniciar_embed02)
            os.system("python bot.py restart")
        finally:
            pass


    if message.content.lower().startswith(prefix+'comandos'):
            comandos_embed = discord.Embed(title="Este comando não está disponível no momento, está em criação!", color=0xFF0000)
            comandos_embed.set_footer(text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
            await client.send_message(message.channel, embed=comandos_embed)


    if message.content.lower().startswith(prefix+'jogar'):
            jogar_embed = discord.Embed(title=":regional_indicator_a: :regional_indicator_t: :regional_indicator_o: :regional_indicator_r: :regional_indicator_e: :regional_indicator_x:", color=0x00BFFF)
            jogar_embed.add_field(name="Para jogar utilize o IP:", value="ATOREXMC.NET", inline=False)
            jogar_embed.add_field(name="Versão:", value="1.8.x", inline=False)
            jogar_embed.set_footer(text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
            await client.send_message(message.channel, embed=jogar_embed)


    if message.content.lower().startswith(prefix+'loja'):
            loja_embed = discord.Embed(title=":regional_indicator_a: :regional_indicator_t: :regional_indicator_o: :regional_indicator_r: :regional_indicator_e: :regional_indicator_x:", color=0x00BFFF)
            loja_embed.add_field(name="Acesse nossa loja:", value="http://loja.atorexmc.com/", inline=False)
            loja_embed.add_field(name="Compre pontos e garanta itens especiais!", value="O prazo para confirmação do pagamento é de até 3 dias úteis.", inline=False)
            loja_embed.set_footer(text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
            await client.send_message(message.channel, embed=loja_embed)


    if message.content.lower().startswith(prefix+'form'):
            form_embed = discord.Embed(title="O formulário não está disponível no momento, as vagas estão encerradas!", color=0xFF0000)
            form_embed.set_footer(text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
            await client.send_message(message.channel, embed=form_embed)


    if message.content.lower().startswith(prefix+'ping'):
        canal = message.channel
        tempo01 = time.perf_counter()
        await client.send_typing(canal)
        tempo02 = time.perf_counter()
        ping_embed = discord.Embed(title="Pong!", description="🏓 Ping - {}ms".format(round((tempo02 - tempo01) * 1000)), color=0x00BFFF)
        await client.send_message(message.channel, embed=ping_embed)


    if message.content.lower().startswith(prefix+'convidar'):
        convite = await client.create_invite(message.channel, max_uses=0, max_age=0)
        covite_embed = discord.Embed(title="📬 Convite gerado!", description="Link : {}\n".format(convite), color=0x00BFFF)
        covite_embed.add_field(name="Canal:", value=convite.channel)
        await client.send_message(message.channel, embed=covite_embed)


    if message.content.lower().startswith(prefix+'denunciar'):
        if not message.content[33:]:
            denunciar_embed = discord.Embed(title="Utilize o comando: '/denunciar @usuário <motivo>'.", color=0xFF0000)
            denunciar_embed.set_footer(text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
            return await client.send_message(message.channel, embed=denunciar_embed)
        try:
            user = message.mentions[0]
            canal = client.get_channel("464095862318956544")
            denunciar_embed02 = discord.Embed(title="O usuário foi denunciado com sucesso no servidor Discord!", color=0x00BFFF)
            denunciar_embed02.set_footer(text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
            denunciar_embed03 = discord.Embed(title="Usuário denunciado!", color=0xFF0000)
            denunciar_embed03.add_field(name="Usuário:", value=user, inline=False)
            denunciar_embed03.add_field(name="ID do usuário:", value=user.id, inline=False)
            denunciar_embed03.add_field(name="Motivo:", value=message.content[33:], inline=False)
            denunciar_embed03.add_field(name="Autor:", value=message.author.mention, inline=False)
            await client.send_message(message.channel, embed=denunciar_embed02)
            await client.send_message(canal, embed=denunciar_embed03)
        except discord.errors.Forbidden:
            denunciar_embed04 = discord.Embed(title="Utilize o comando: '/denunciar @usuário <motivo>'.", color=0xFF0000)
            denunciar_embed04.set_footer(text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
            return await client.send_message(message.channel, embed=denunciar_embed04)
        finally:
            pass


    if message.content.lower().startswith(prefix+'sugerir'):
        if not message.content[9:]:
            denunciar_embed = discord.Embed(title="Utilize o comando: '/sugerir <sugestão>'.", color=0xFF0000)
            denunciar_embed.set_footer(text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
            return await client.send_message(message.channel, embed=denunciar_embed)
        try:
            canal = client.get_channel("457887056207675393")
            denunciar_embed02 = discord.Embed(title="Sua sugestão foi enviada com sucesso!", color=0x00BFFF)
            denunciar_embed02.set_footer(text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
            denunciar_embed03 = discord.Embed(title="Nova sugestão!", color=0xFF0000)
            denunciar_embed03.add_field(name="Sugestão:", value=message.content[8:], inline=False)
            denunciar_embed03.add_field(name="Autor:", value=message.author.mention, inline=False)
            await client.send_message(message.channel, embed=denunciar_embed02)
            await client.send_message(canal, embed=denunciar_embed03)
        except discord.errors.Forbidden:
            denunciar_embed04 = discord.Embed(title="Utilize o comando: '/sugerir <sugestão>'.", color=0xFF0000)
            denunciar_embed04.set_footer(text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
            return await client.send_message(message.channel, embed=denunciar_embed04)
        finally:
            pass


    if message.content.lower().startswith(prefix+'clear'):
        if not message.author.server_permissions.manage_messages:
            await client.send_message(message.channel, ":no_good:**Sem permissão!**")
        try:
            lim = int(message.content[7:]) + 1
            await client.purge_from(message.channel, limit=lim)
            await client.send_message(message.channel, '{} mensagens foram deletadas com sucesso ,por {}'.format(lim,
                                                                                                            message.author.mention))
        finally:
            pass


    if message.content.lower().startswith(prefix+'falar'):
        if not message.author.server_permissions.ban_members:
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
            ban_embed02 = discord.Embed(title="O usuário foi banido com sucesso no servidor Discord!", color=0x00BFFF)
            ban_embed02.set_footer(text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
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
            unban_embed02 = discord.Embed(title="O usuário foi desbanido com sucesso no servidor Discord!", color=0x00BFFF)
            unban_embed02.set_footer(text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
            unban_embed03 = discord.Embed(title="Usuário desbanido!", color=0x00FF00)
            unban_embed03.add_field(name="Usuário:", value=user, inline=False)
            unban_embed03.add_field(name="ID do usuário:", value=user.id, inline=False)
            unban_embed03.add_field(name="Autor:", value=message.author.mention, inline=False)
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
            kick_embed03 = discord.Embed(title="O usuário foi expulso com sucesso no servidor Discord!", color=0x00BFFF)
            kick_embed03.set_footer(text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
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
            mute_embed03 = discord.Embed(title="O usuário foi mutado com sucesso no servidor Discord!", color=0x00BFFF)
            mute_embed03.set_footer(text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
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
            unmute_embed02 = discord.Embed(title="O usuário foi desmutado com sucesso no servidor Discord!", color=0x00BFFF)
            unmute_embed02.set_footer(text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
            unmute_embed03 = discord.Embed(title="Usuário desmutado!", color=0x00FF00)
            unmute_embed03.add_field(name="Usuário:", value=user, inline=False)
            unmute_embed03.add_field(name="ID do usuário:", value=user.id, inline=False)
            unmute_embed03.add_field(name="Autor:", value=message.author.mention, inline=False)
            await client.remove_roles(user, cargo)
            await client.send_message(message.channel, embed=unmute_embed02)
            await client.send_message(canal, embed=unmute_embed03)
        except discord.errors.Forbidden:
            unmute_embed04 = discord.Embed(title="Utilize o comando: '/unmute @usuário'.", color=0xFF0000)
            unmute_embed04.set_footer(text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
            return await client.send_message(message.channel, embed=unmute_embed04)
        finally:
            pass


    if message.content.lower().startswith(prefix+'warn'):
        if not message.author.server_permissions.kick_members:
            warn_embed = discord.Embed(title="Você não tem permissões necessárias para utilizar este comando.", color=0xFF0000)
            warn_embed.set_footer(text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
            return await client.send_message(message.channel, embed=warn_embed)
        if not message.content[28:]:
            warn_embed02 = discord.Embed(title="Utilize o comando: '/warn @usuário <motivo>'.", color=0xFF0000)
            warn_embed02.set_footer(text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
            return await client.send_message(message.channel, embed=warn_embed02)
        try:
            user = message.mentions[0]
            canal = client.get_channel("465673373201203210")
            warn_embed03 = discord.Embed(title="O usuário foi alertado com sucesso no servidor Discord!", color=0x00BFFF)
            warn_embed03.set_footer(text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
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
            warn_embed06.set_footer(text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
            return await client.send_message(message.channel, embed=warn_embed06)
        finally:
            pass


    if message.content.lower().startswith(prefix+'votar'):
        if not message.author.server_permissions.ban_members:
            unban_embed = discord.Embed(title="Você não tem permissões necessárias para utilizar este comando.", color=0xFF0000)
            unban_embed.set_footer(text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
            return await client.send_message(message.channel, embed=unban_embed)
        try:
            vote = discord.Embed(
                title= "Votação!",
                color=0x00BFFF,
                description='O que vocês acham sobre: {}?'.format(message.content[7:])
            )
            vote = await client.send_message(message.channel, embed=vote)
            await client.add_reaction(vote, "✅")
            await client.add_reaction(vote, "❎")
        finally:
            pass



client.run('NDY0NjA0NDczOTMxODU3OTIx.DiBYJw.S2iTn7TXy7L9D1r1nLqryoaNOwg')
