import discord
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


  if message.content.lower().startswith(prefix+'reiniciar') and message.author.id == "322488685973209109":
    try:
      await client.send_message(message.channel, "Reiniciando...")
    except IndexError:
      await client.send_message(message.channel, "Serm permissão")


  if message.content.lower().startswith(prefix+'ping'):
    timep = time.time()
    ping_embed = discord.Embed(title = 'Aguarde...', color = 0x00FF40)
    pingm0 = await client.send_message(message.channel, embed=ping_embed)
    ping = time.time() - timep
    ping2_embed = discord.Embed(title = 'Pong!', description = '🏓 Ping - %.01f segundos' % ping, color=0x00FF40)
    await client.edit_message(pingm0, embed=ping2_embed)


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
      userinfo_embed.add_field(name=":door:Entrou no servidor em:", value=userjoinedat, inline=True)
      userinfo_embed.add_field(name="📅Conta criada em:", value=usercreatedat, inline=True)
      userinfo_embed.add_field(name="💻ID:", value=user.id, inline=True)
      userinfo_embed.add_field(name=":label:Tag:", value=user.discriminator, inline=True)
      userinfo_embed.add_field(name="Cargos:", value=role, inline=True)
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
      userinfo_embed2.add_field(name=":door:Entrou no servidor em:", value=userjoinedat2, inline=True)
      userinfo_embed2.add_field(name="📅Conta criada em:", value=usercreatedat2, inline=True)
      userinfo_embed2.add_field(name="💻ID:", value=user2.id, inline=True)
      userinfo_embed2.add_field(name=":label:Tag:", value=user2.discriminator, inline=True)
      userinfo_embed2.add_field(name="Cargos:", value=role2, inline=True)
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
          color=0xFFFFFF
        )
        avatar_embed.set_image(url=user.avatar_url)
        avatar_embed.set_footer(text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
        await client.send_message(message.channel, embed=avatar_embed)
      except IndexError:
        user2 = message.author
        avatar_embed2 = discord.Embed(
          title="Avatar de {}:".format(user2.name),
          color=0xFFFFFF,
        )
        avatar_embed2.set_image(url=user2.avatar_url)
        avatar_embed2.set_footer(text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
        await client.send_message(message.channel, embed=avatar_embed2)



client.run('NDY0NjA0NDczOTMxODU3OTIx.DiBYJw.S2iTn7TXy7L9D1r1nLqryoaNOwg')
