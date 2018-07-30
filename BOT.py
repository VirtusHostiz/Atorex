import discord
import json
import requests
import aiohttp

client = discord.Client()
prefix = "/"

@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name='yWilliam#7959', type=2))
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
                if b['serverStatus'] == "online":
                    await client.edit_channel(channel=canal02, name="🎇| Status: Online")
                if b['serverStatus'] == "online":
                    jogadores01 = c['players']
                    maximo01 = c['maxplayers']
                    await client.edit_channel(channel=canal03, name="👥| Rankup: {}/{}".format(jogadores01, maximo01))
                if b['serverStatus'] == "online":
                    jogadores02 = d['players']
                    maximo02 = d['maxplayers']
                    await client.edit_channel(channel=canal04, name="👥| Kitpvp: {}/{}".format(jogadores02, maximo02))
                if b['serverStatus'] == "online":
                    ping = b['ping']
                    await client.edit_channel(channel=canal05, name="⏰| Ping: {}ms".format(ping))
                if b['serverStatus'] == "online":   
                    versao = a['version']
                    await client.edit_channel(channel=canal06, name="💠| Versão: {}".format(versao))
            elif b['serverStatus'] == "offline":
                await client.edit_channel(channel=canal01, name="🎮| IP: {}".format(ip))
                await client.edit_channel(channel=canal02, name="🎇| Status: Offline")
                await client.edit_channel(channel=canal03, name="👥| Rankup: ❌")
                await client.edit_channel(channel=canal04, name="👥| Kitpvp: ❌")
                await client.edit_channel(channel=canal05, name="⏰| Ping: ❌")
                await client.edit_channel(channel=canal06, name="💠| Versão: ❌")
        except (requests.exceptions.ConnectionError, discord.errors.HTTPException, aiohttp.errors.ClientResponseError, json.decoder.JSONDecodeError, KeyError):
            a = requests.get('https://api.mcsrvstat.us/1/play.atorexmc.com').json()
            ip = a['hostname']
            await client.edit_channel(channel=canal01, name="🎮| IP: {}".format(ip))
            await client.edit_channel(channel=canal02, name="🎇| Status: 🔎")
            await client.edit_channel(channel=canal03, name="👥| Rankup: 🔎")
            await client.edit_channel(channel=canal04, name="👥| Kitpvp: 🔎")
            await client.edit_channel(channel=canal05, name="⏰| Ping: 🔎")
            await client.edit_channel(channel=canal06, name="💠| Versão: 🔎")
        except RuntimeError:
            os.system("python BOT.py reload")
        finally:
            pass



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
        e = requests.get('https://api.minetools.eu/query/pingrankup.mcpe.network/25615').json()
        if e['status'] == "OK":
            jogadores = e['Playerlist']
            rankup_embed = discord.Embed(title="⚔️ Rankup ⚔️", color=0x00FF00)
            rankup_embed.add_field(name="Jogadores online no momento:", value="{}".format(', '.join(jogadores)), inline=False)
            rankup_embed.set_footer(icon_url=message.author.avatar_url, text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
            return await client.send_message(message.channel, embed=rankup_embed)
        elif e['status'] == "ERR":
            rankup_embed04 = discord.Embed(title="⚔️ Rankup ⚔️", color=0x00FF00)
            rankup_embed04.add_field(name="O **Rankup** não está online no momento, tente novamente mais tarde!", value="{}".format(', '.join(jogadores)), inline=False)
            rankup_embed04.set_footer(icon_url=message.author.avatar_url, text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
            return await client.send_message(message.channel, embed=rankup_embed04)
        else:
            rankup_embed05 = discord.Embed(title="⚔️ Rankup ⚔️", color=0x00FF00)
            rankup_embed05.add_field(name="Ocorreu um erro, tente novamente mais tarde!", value="{}".format(', '.join(jogadores)), inline=False)
            rankup_embed05.set_footer(icon_url=message.author.avatar_url, text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
            return await client.send_message(message.channel, embed=rankup_embed05)



client.run('NDcyODY4NzA0OTUxMDc0ODE4.Dj5o_g.qiUTDKB2Yfjp9SX9OlbRC7atv-E')