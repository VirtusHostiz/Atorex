import discord
import os
import asyncio
import time
from time import sleep as s
import datetime
from random import *
import json
from discord.ext import commands
import requests
import aiohttp
import googletrans
from googletrans import Translator
import wikipedia

client = discord.Client()
prefix = "/"

msg_id = None
msg_user = None

tradutor = Translator(service_urls=[
      'translate.google.com',
      'translate.google.co.kr',
    ])

def wiki_summary(arg):
    wikipedia.set_lang("pt")
    definition = wikipedia.summary(arg, sentences=1, chars=100, auto_suggest=True, redirect=True)
    return definition

@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name=prefix+'comandos', type=2))
    print('[BOT ONLINE]')
    while True:
        try:
            a = requests.get('https://api.mcsrvstat.us/1/play.atorexmc.com').json()
            b = requests.get('https://mcapi.xdefcon.com/server/play.atorexmc.com/full/json').json()
            c = requests.get('https://mcapi.xdefcon.com/server/pingrankup.mcpe.network:25615/full/json').json()
            d = requests.get('https://mcapi.xdefcon.com/server/pingkitpvp.mcpe.network:25663/full/json').json()
            canal01 = client.get_channel('472867146360160258')
            canal02 = client.get_channel('472868023473274882')
            canal03 = client.get_channel('472868040879505409')
            canal04 = client.get_channel('472868064799621120')
            canal05 = client.get_channel('472868078942814211')
            canal06 = client.get_channel('472868095665504266')
            if b['serverStatus'] == "online":
                ip = a['hostname']
                await client.edit_channel(channel=canal01, name="🎮| IP: {}".format(ip))
                if b['serverStatus'] == "online" and canal02.name != "🎇| Status: Manutenção":
                    await client.edit_channel(channel=canal02, name="🎇| Status: Online")
                if b['serverStatus'] == "online":
                    jogadores01 = c['players']
                    maximo01 = c['maxplayers']
                    await client.edit_channel(channel=canal03, name="👥| Rankup: {}/{}".format(jogadores01, maximo01))
                if b['serverStatus'] == "online":
                    jogadores02 = d['players']
                    maximo02 = d['maxplayers']
                    await client.edit_channel(channel=canal04, name="👥| KitPvp: {}/{}".format(jogadores02, maximo02))
                if b['serverStatus'] == "online":
                    ping = b['ping']
                    await client.edit_channel(channel=canal05, name="⏰| Ping: {}ms".format(ping))
                if b['serverStatus'] == "online":   
                    versao = a['version']
                    await client.edit_channel(channel=canal06, name="💠| Versão: {}".format(versao))
            if b['serverStatus'] == "offline":
                await client.edit_channel(channel=canal01, name="🎮| IP: {}".format(ip))
                if not canal02.name == "🎇| Status: Manutenção":
                    await client.edit_channel(channel=canal02, name="🎇| Status: Offline")
                await client.edit_channel(channel=canal03, name="👥| Rankup: ❌")
                await client.edit_channel(channel=canal04, name="👥| KitPvp: ❌")
                await client.edit_channel(channel=canal05, name="⏰| Ping: ❌")
                await client.edit_channel(channel=canal06, name="💠| Versão: ❌")
        except (requests.exceptions.ConnectionError, discord.errors.HTTPException, aiohttp.errors.ClientResponseError, json.decoder.JSONDecodeError, KeyError):
            a = requests.get('https://api.mcsrvstat.us/1/play.atorexmc.com').json()
            ip = a['hostname']
            await client.edit_channel(channel=canal01, name="🎮| IP: {}".format(ip))
            if not canal02.name == "🎇| Status: Manutenção":
                await client.edit_channel(channel=canal02, name="🎇| Status: 🔎")
            await client.edit_channel(channel=canal03, name="👥| Jogadores: 🔎")
            await client.edit_channel(channel=canal04, name="⏰| Ping: 🔎")
            await client.edit_channel(channel=canal05, name="💠| Versão: 🔎")
        finally:
            pass
        await asyncio.sleep(1)


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


    if message.content.lower().startswith(prefix+'comandos'):
        comandos_embed = discord.Embed(title="Atorex Network", description="• :gear: **Usuários**\n\n• :video_game: **Jogos**\n\n• :tools: **Staff**", color=0x00BFFF)
        comandos_embed.set_thumbnail(url="https://i.imgur.com/P9o8NUE.png")
        comandos_embed.set_footer(icon_url=message.author.avatar_url, text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
        botmsg = await client.send_message(message.channel, embed=comandos_embed)
        await client.add_reaction(botmsg, "⚙")
        await client.add_reaction(botmsg, "🎮")
        await client.add_reaction(botmsg, "🛠")
        await asyncio.sleep(2)
        global msg_id
        msg_id = botmsg.id
        global msg_user
        msg_user = message.author


    if message.content.lower().startswith(prefix+'jogar'):
        jogar_embed = discord.Embed(title="Atorex Network", color=0x00BFFF)
        jogar_embed.add_field(name="Para jogar utilize o IP:", value="PLAY.ATOREXMC.COM", inline=False)
        jogar_embed.add_field(name="Versão:", value="1.8.x", inline=False)
        jogar_embed.set_footer(icon_url=message.author.avatar_url, text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
        await client.send_message(message.channel, embed=jogar_embed)


    if message.content.lower().startswith(prefix+'site'):
        loja_embed = discord.Embed(title="Atorex Network", value="http://atorexmc.com/", inline=False)
        loja_embed.set_footer(icon_url=message.author.avatar_url, text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
        await client.send_message(message.channel, embed=loja_embed)


    if message.content.lower().startswith(prefix+'form'):
        form_embed = discord.Embed(title="Formulário não disponível no momento, vagas encerradas!", color=0xFF0000)
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


    if message.content.lower().startswith(prefix+'traduzir'):
        try:
            msg = message.content[10:12]
            msg2 = message.content[13:]
            traduzido = tradutor.translate(msg2, dest=msg).text
            traduzir_embed = discord.Embed(color=0x00BFFF)
            traduzir_embed.add_field(name="Tradutor", value="Texto original: ```{}```\nTradução: ```{}```".format(msg2, traduzido))
            traduzir_embed.set_footer(icon_url=message.author.avatar_url, text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
            await client.send_message(message.channel, embed=traduzir_embed)
        except Exception as e:
            traduzir_embed02 = discord.Embed(title="Ocorreu um erro ao traduzir a mensagem.", color=0xFF0000)
            traduzir_embed02.set_footer(icon_url=message.author.avatar_url, text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
            return await client.send_message(message.channel, embed=traduzir_embed02)
        finally:
            pass


    if message.content.lower().startswith(prefix+'pesquisar'):
        try:
            words = message.content.split()
            pergunta = message.content[11:]
            important_words = words[1:]
            pesquisar_embed = discord.Embed(title="Definição de {}:".format(pergunta), description="```" + wiki_summary(important_words) + "```", color=0x00BFFF)
            await client.send_message(message.channel, embed=pesquisar_embed)
        except Exception as e:
            pesquisar_embed02 = discord.Embed(title="Ocorreu um erro ao pesquisar definições para esta palavra.", color=0xFF0000)
            pesquisar_embed02.set_footer(icon_url=message.author.avatar_url, text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
            return await client.send_message(message.channel, embed=pesquisar_embed02)
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
            respostas = ['Sim','Claro','Sempre','As vezes','Talvez','Quase sempre','Quase nunca','Não','Nunca','Jamais']
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


    if message.content.lower().startswith(prefix+'loteria'):
        try:
            test = int(message.content.strip(prefix+'loteria').strip())
            float(test)
            test += 1
        except ValueError:
            loteria_embed = discord.Embed(title="Utilize o comando: '/loteria <número>'.", color=0xFF0000)
            loteria_embed.set_footer(icon_url=message.author.avatar_url, text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
            return await client.send_message(message.channel, embed=loteria_embed)
        else:
            number = randint(1,100)
            loteria_embed02 = discord.Embed(title="🎰 Rodando...", color=0x00BFFF)
            loteria_embed02.set_footer(icon_url=message.author.avatar_url, text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
            rol = await client.send_message(message.channel, embed=loteria_embed02)
            s(2)
            if number == int(message.content.strip(prefix+'loteria').strip()):
                loteria_embed03 = discord.Embed(title=":white_check_mark:ㅤVocê **ganhou**, o número foi " + str(number) + "!", color=0x00FF00)
                loteria_embed03.set_footer(icon_url=message.author.avatar_url, text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
                await client.edit_message(rol, embed=loteria_embed03)
            else:
                loteria_embed04 = discord.Embed(title=":x:ㅤVocê **perdeu**, o número foi " + str(number) + "!", color=0xFF0000)
                loteria_embed04.set_footer(icon_url=message.author.avatar_url, text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
                await client.edit_message(rol, embed=loteria_embed04)


    if message.content.startswith(prefix+'dado'):
        escolher = randint(1, 6)
        dado_embed = discord.Embed(title="🎲 Dado", description=" Joguei o dado e o resultado foi (**{}**)!".format(escolher), color=0x00BFFF)
        dado_embed.set_footer(icon_url=message.author.avatar_url, text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
        await client.send_message(message.channel, embed=dado_embed)


    if message.content.lower().startswith(prefix+'clear'):
        if not message.author.server_permissions.manage_messages:
            clear_embed = discord.Embed(title="Você não tem permissões necessárias para utilizar este comando.", color=0xFF0000)
            clear_embed.set_footer(icon_url=message.author.avatar_url, text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
            return await client.send_message(message.channel, embed=clear_embed)
        if not message.content[7:]:
            clear_embed02 = discord.Embed(title="Utilize o comando: '/clear <quantidade>'.", color=0xFF0000)
            clear_embed02.set_footer(icon_url=message.author.avatar_url, text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
            return await client.send_message(message.channel, embed=clear_embed02)
        if not int(message.content[7:]) > 0 and int(message.content[7:]) < 100:
            clear_embed03 = discord.Embed(title="Escolha um número de mensagens entre 1 e 100.", color=0xFF0000)
            clear_embed03.set_footer(icon_url=message.author.avatar_url, text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
            return await client.send_message(message.channel, embed=clear_embed03)
        try:
            lim = int(message.content[7:]) + 1
            clear_embed04 = discord.Embed(title=":pencil: Foram apagadas {} mensagens com sucesso!".format(lim), color=0x00FF00)
            clear_embed04.set_footer(icon_url=message.author.avatar_url, text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
            await client.purge_from(message.channel, limit=lim)
            await client.send_message(message.channel, embed=clear_embed04)
        except:
            ban_embed05 = discord.Embed(title="Ocorreu um erro ao apagar as mensagens.", color=0xFF0000)
            ban_embed05.set_footer(icon_url=message.author.avatar_url, text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
            return await client.send_message(message.channel, embed=ban_embed05)
        finally:
            pass


    if message.content.lower().startswith(prefix+'falar'):
        if not message.author.server_permissions.ban_members:
            falar_embed = discord.Embed(title="Você não tem permissões necessárias para utilizar este comando.", color=0xFF0000)
            falar_embed.set_footer(icon_url=message.author.avatar_url, text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
            return await client.send_message(message.channel, embed=falar_embed)
        if not message.content[7:]:
            falar_embed03 = discord.Embed(title="Utilize o comando: '/falar <mensagem>'.", color=0xFF0000)
            falar_embed03.set_footer(icon_url=message.author.avatar_url, text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
            return await client.send_message(message.channel, embed=falar_embed03)
        try:
            mensagem = str(message.content).replace(prefix+"falar", "")
            falar_embed03 = discord.Embed(description=mensagem, color=0x00BFFF)
            await client.delete_message(message)
            await client.send_message(message.channel, embed=falar_embed03)
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


    if message.content.lower().startswith(prefix+'manu'):
        if not message.author.server_permissions.administrator:
            manu_embed = discord.Embed(title="Você não tem permissões necessárias para utilizar este comando.", color=0xFF0000)
            manu_embed.set_footer(icon_url=message.author.avatar_url, text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
            return await client.send_message(message.channel, embed=manu_embed)
        try:
            manu = message.content[6:]
            canal = client.get_channel('472868023473274882')
            if manu == "on":
                return await client.edit_channel(channel=canal, name="🎇| Status: Manutenção")
            if manu == "off":
                return await client.edit_channel(channel=canal, name="🎇| Status: 🔎")
            if not manu == "on" or "off":
                manu_embed02 = discord.Embed(title="Utilize o comando: '/manu on' ou '/manu off'.", color=0xFF0000)
                manu_embed02.set_footer(icon_url=message.author.avatar_url, text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
                return await client.send_message(message.channel, embed=manu_embed02)
        finally:
            pass



@client.event
async def on_reaction_add(reaction, user):
    msg = reaction.message
    if reaction.emoji == "⚙" and msg.id == msg_id:
        comandos_embed = discord.Embed(title="⚙ Comandos dos usuário:", description="ㅤ", color=0x00BFFF)
        comandos_embed.set_thumbnail(url="https://i.imgur.com/P9o8NUE.png")
        comandos_embed.add_field(name="• [/comandos] - Comandos do BOT.", value="• [/jogar] - Como jogar.", inline=False)
        comandos_embed.add_field(name="• [/site] - Site do servidor.", value="• [/form] - Formulário para ser staff.", inline=False)
        comandos_embed.add_field(name="• [/ping] - Saber seu ping.", value="• [/convidar] - Convide pessoas.", inline=False)
        comandos_embed.add_field(name="• [/denunciar @usuário <motivo>] - Denuncie algum usuário.", value="• [/sugerir <sugestão>] - Sugira mudanças.", inline=False)
        comandos_embed.add_field(name="• [/solicitar <link do vídeo>] - Solicite sua tag.", value="• [/parceria <mensagem>] - Solicite uma parceria.", inline=False)
        await client.send_message(user, embed=comandos_embed)


    if reaction.emoji == "🎮" and msg.id == msg_id:
        comandos_embed02 = discord.Embed(title="🎮 Comandos de jogos:", description="ㅤ", color=0x00BFFF)
        comandos_embed02.set_thumbnail(url="https://i.imgur.com/P9o8NUE.png")
        comandos_embed02.add_field(name="• [/moeda] - Cara ou coroa?", value="• [/8ball <pergunta>] - Faça uma pergunta ao BOT.", inline=False)
        comandos_embed02.add_field(name="• [/loteria <número>] - Teste sua sorte.", value="• [/dado] - Jogue o dado.", inline=False)
        await client.send_message(user, embed=comandos_embed02)


    if reaction.emoji == "🛠" and msg.id == msg_id:
        comandos_embed03 = discord.Embed(title="🛠 Comandos da staff:", description="ㅤ", color=0x00BFFF)
        comandos_embed03.set_thumbnail(url="https://i.imgur.com/P9o8NUE.png")
        comandos_embed03.add_field(name="• [/clear <quantidade>] - Apagar mensagens.", value="• [/falar <mensagem>] - Faça o BOT falar.", inline=False)
        comandos_embed03.add_field(name="• [/ban @usuário <motivo>] - Banir um usuário.", value="• [/unban <ID do usuário>] - Desbanir um usuário.", inline=False)
        comandos_embed03.add_field(name="• [/kick @usuário <motivo>] - Expulsar um usuário.", value="• [/mute @usuário <motivo>] - Mutar um usuário.", inline=False)
        comandos_embed03.add_field(name="• [/unmute @usuário] - Desmutar um usuário.", value="• [/warn @usuário <motivo>] - Alertar um usuário,.", inline=False)
        comandos_embed03.add_field(name="• [/votar <assunto>] - Criar uma votação.", value="ㅤ", inline=False)
        await client.send_message(user, embed=comandos_embed03)


    if reaction.emoji == "🤖" and msg.id == msg_id:
        comandos_embed04 = discord.Embed(title="🤖 Comandos do yWilliam:", description="ㅤ", color=0x00BFFF)
        comandos_embed04.set_thumbnail(url="https://i.imgur.com/P9o8NUE.png")
        comandos_embed04.add_field(name="• [/reiniciar] - Reiniciar o BOT.", value="ㅤ", inline=False)
        await client.send_message(user, embed=comandos_embed04)



@client.event
async def on_member_join(member):
    canal = client.get_channel("467096925087465489")
    cargo = discord.utils.find(lambda r: r.name == "Membro", member.server.roles)
    entrar_embed = discord.Embed(title="Atorex Network", description="**{}** seja bem-vindo(a) ao servidor Discord do **Atorex Network**!".format(member.mention), color=0x00BFFF)
    entrar_embed.add_field(name="IP do servidor: PLAY.ATOREXMC.COM", value="Site do servidor: **http://atorexmc.com/**", inline=False)
    entrar_embed.add_field(name="Formulário: Não disponível no momento.", value="Utilize **/comandos** para saber os comandos do BOT.", inline=False)
    await client.send_message(canal, embed=entrar_embed)
    await client.add_roles(member, cargo)



client.run('NDcyODY4NzA0OTUxMDc0ODE4.Dj5o_g.qiUTDKB2Yfjp9SX9OlbRC7atv-E')
