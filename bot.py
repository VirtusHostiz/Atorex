import discord
import os
import asyncio
import time
import datetime

client = discord.Client()
prefix = "/"

@client.event
async def on_ready():
  await client.change_presence(game=discord.Game(name=prefix+"comandos", type=2))
  print('[BOT ONLINE COM SUCESSO]')


@client.event
async def on_message(message):
  if message.content.lower().startswith(prefix+'comandos'):
    await client.send_message(message.channel, "{},\n```diff\n- Este comando não está disponível no momento.\n```".format(message.author.mention))


  if message.content.lower().startswith(prefix+'reiniciar'): 
    if not message.author.id == "322488685973209109":
      reiniciar_embed = discord.Embed(title="Você não tem permissões necessárias para utilizar este comando.", color=0xFF0000)
      reiniciar_embed.set_footer(text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
      await client.send_message(message.channel, embed=reiniciar_embed)
    try:
      reiniciar2_embed = discord.Embed(title=":pushpin: Reiniciando...", color=0x00FF00)
      reiniciar2_embed.set_footer(text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
      await client.send_message(message.channel, embed=reiniciar2_embed)
      os.system("python bot.py reload")
    finally:
      pass


  if message.content.lower().startswith(prefix+'ping'):
    channel = message.channel
    t1 = time.perf_counter()
    await client.send_typing(channel)
    t2 = time.perf_counter()
    ping_embed = discord.Embed(title='Pong!', description="🏓 Ping - {}ms".format(round((t2 - t1) * 1000)), color=0x00BFFF)
    await client.send_message(message.channel, embed=ping_embed)


  if message.content.startswith(prefix+'serverinfo'):
    serverinfo_embed = discord.Embed(title="\n", description="Principais informações do nosso servidor Discord:", color=0x00FFFF)
    serverinfo_embed.set_thumbnail(url=message.server.icon_url)
    serverinfo_embed.set_footer(text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
    serverinfo_embed.add_field(name="Nome:", value=message.server.name, inline=True)
    serverinfo_embed.add_field(name="ID:", value=message.server.id, inline=True)
    serverinfo_embed.add_field(name="Dono:", value=message.server.owner.mention)
    serverinfo_embed.add_field(name="Canais de texto:", value=len([message.channel.mention for channel in message.server.channels if channel.type==discord.ChannelType.text]), inline=True)
    serverinfo_embed.add_field(name="Canais de voz:", value=len([message.channel.mention for channel in message.server.channels if channel.type==discord.ChannelType.voice]), inline=True)
    serverinfo_embed.add_field(name="Usuários:", value=len(message.server.members), inline=True)     
    await client.send_message(message.channel, embed=serverinfo_embed)


  if message.content.lower().startswith(prefix+'userinfo'):
    try:
      user = message.mentions[0]
      role = ",".join([r.name for r in user.roles if r.name!="@everyone"])
      userjoinedat = str(user.joined_at).split('.', 1)[0]
      usercreatedat = str(user.created_at).split('.', 1)[0]
      userinfo_embed = discord.Embed(
        title=":pushpin:Informações pessoais de:",
        color=0x690FC3,
        description=user.name
      )
      userinfo_embed.add_field(name=":door: Entrou no servidor em:", value=userjoinedat, inline=True)
      userinfo_embed.add_field(name="📅 Conta criada em:", value=usercreatedat, inline=True)
      userinfo_embed.add_field(name="💻 ID:", value=user.id, inline=True)
      userinfo_embed.add_field(name=":label: Tag:", value=user.discriminator, inline=True)
      userinfo_embed.add_field(name=" Cargos:", value=role, inline=True)
      userinfo_embed.set_footer(text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
      userinfo_embed.set_thumbnail(url=user.avatar_url)
      await client.send_message(message.channel, embed=userinfo_embed)
    except IndexError:
      user2 = message.author
      role2 = ",".join([r.name for r in message.author.roles if r.name!= "@everyone"])
      userjoinedat2 = str(user2.joined_at).split('.', 1)[0]
      usercreatedat2 = str(user2.created_at).split('.', 1)[0]
      userinfo_embed2 = discord.Embed(
        title=":pushpin:Informações pessoais de:",
        color=0x690FC3,
        description=user2.name
      )
      userinfo_embed2.add_field(name=":door: Entrou no servidor em:", value=userjoinedat2, inline=True)
      userinfo_embed2.add_field(name="📅 Conta criada em:", value=usercreatedat2, inline=True)
      userinfo_embed2.add_field(name="💻 ID:", value=user2.id, inline=True)
      userinfo_embed2.add_field(name=":label: Tag:", value=user2.discriminator, inline=True)
      userinfo_embed2.add_field(name=" Cargos:", value=role2, inline=True)
      userinfo_embed2.set_footer(text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
      userinfo_embed2.set_thumbnail(url=message.author.avatar_url)
      await client.send_message(message.channel, embed=userinfo_embed2)
    finally:
      pass


  if message.content.lower().startswith(prefix+'avatar'):
    try:
      user = message.mentions[0]
      avatar_embed =discord.Embed(
        title="Avatar de {}:".format(user.name),
        color=0x00BFFF,
      )
      avatar_embed.set_image(url=user.avatar_url)
      avatar_embed.set_footer(text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
      await client.send_message(message.channel, embed=avatar_embed)
    except:
      user2 = message.author
      avatar2_embed = discord.Embed(
        title="Avatar de {}:".format(user2.name),
        color=0x00BFFF,
      )
      avatar2_embed.set_image(url=user2.avatar_url)
      avatar2_embed.set_footer(text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
      await client.send_message(message.channel, embed=avatar2_embed)
    finally:
      pass


  if message.content.lower().startswith(prefix+'ban'):
    if not message.author.server_permissions.ban_members:
      ban_embed = discord.Embed(title="Você não tem permissões necessárias para utilizar este comando.", color=0xFF0000)
      ban_embed.set_footer(text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
      return await client.send_message(message.channel, embed=ban_embed)
    try:
      user = message.mentions[0]
      canal = client.get_channel("465673373201203210")
      ban2_embed = discord.Embed(title="Usuário banido com sucesso do servidor Discord.", color=0x00BFFF)
      ban2_embed.set_footer(text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
      await client.send_message(message.channel, embed=ban2_embed)
      ban3_embed = discord.Embed(
        title="Banimento ocorrido:",
        color=0xFF0000
      )
      ban3_embed.add_field(name="Usuário banido:", value=user)
      ban3_embed.add_field(name="ID do usuário:", value=user.id)
      ban3_embed.add_field(name="Motivo:", value=message.content[27:])
      ban3_embed.add_field(name="Autor:", value=message.author.mention)
      await client.send_message(canal, embed=ban3_embed)
      await client.ban(user, delete_message_days=7)
    except:
      ban4_embed = discord.Embed(title="Utilize o comando: '/ban @usuário <motivo>'.", color=0xFF0000)
      ban4_embed.set_footer(text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
      return await client.send_message(message.channel, embed=ban4_embed)
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
      unban2_embed = discord.Embed(title="Usuário desbanido com sucesso do servidor Discord.", color=0x00BFFF)
      unban2_embed.set_footer(text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
      await client.send_message(message.channel, embed=unban2_embed)
      unban3_embed = discord.Embed(
        title="Desbanimento ocorrido:",
        color=0x00FF00
      )
      unban3_embed.add_field(name="ID do usuário:", value=user)
      unban3_embed.add_field(name="Autor:", value=message.author.mention)
      await client.send_message(canal, embed=unban3_embed)
      await client.unban(message.server, user)
    except:
      unban4_embed = discord.Embed(title="Utilize o comando: '/unban <ID do usuário>'.", color=0xFF0000)
      unban4_embed.set_footer(text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
      return await client.send_message(message.channel, embed=unban4_embed)
    finally:
      pass


  if message.content.lower().startswith(prefix+'kick'):
    if not message.author.server_permissions.kick_members:
      kick_embed = discord.Embed(title="Você não tem permissões necessárias para utilizar este comando.", color=0xFF0000)
      kick_embed.set_footer(text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
      return await client.send_message(message.channel, embed=kick_embed)
    try:
      user = message.mentions[0]
      canal = client.get_channel("465673373201203210")
      kick2_embed = discord.Embed(title="Usuário expulso com sucesso do servidor Discord.", color=0x00BFFF)
      kick2_embed.set_footer(text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
      await client.send_message(message.channel, embed=kick2_embed)
      kick3_embed = discord.Embed(
        title="Expulsão ocorrida:",
        color=0xFF0000
      )
      kick3_embed.add_field(name="Usuário expulso:", value=user)
      kick3_embed.add_field(name="ID do usuário:", value=user.id)
      kick3_embed.add_field(name="Motivo:", value=message.content[27:])
      kick3_embed.add_field(name="Autor:", value=message.author.mention)
      await client.send_message(canal, embed=kick3_embed)
      await client.kick(user)
    except:
      kick4_embed = discord.Embed(title="Utilize o comando: '/kick @usuário <motivo>'.", color=0xFF0000)
      kick4_embed.set_footer(text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
      return await client.send_message(message.channel, embed=kick4_embed)
    finally:
      pass



client.run('NDY0NjA0NDczOTMxODU3OTIx.DiBYJw.S2iTn7TXy7L9D1r1nLqryoaNOwg')
