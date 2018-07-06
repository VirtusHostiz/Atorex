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


  if message.content.lower().startswith(prefix+'ping'):
    timep = time.time()
    emb = discord.Embed(title = 'Aguarde...', color = 0x00FF40)
    pingm0 = await client.send_message(message.channel, embed=emb)
    ping = time.time() - timep
    pingm1 = discord.Embed(title = 'Pong!', description = '🏓 Ping - %.01f segundos' % ping, color=0x00FF40)
    await client.edit_message(pingm0, embed=pingm1)


  if message.content.startswith(prefix+'info'):
    user = message.author.name
    serverinfo_embed = discord.Embed(title="\n", description="Abaixo está as principais informações do nosso servidor Discord:", color=0x00FFFF)
    serverinfo_embed.set_thumbnail(url=message.server.icon_url)
    serverinfo_embed.set_footer(text="• Comando enviado por: {}.".format(user))
    serverinfo_embed.add_field(name="Nome:", value=message.server.name, inline=True)
    serverinfo_embed.add_field(name="Dono:", value=message.server.owner.mention)
    serverinfo_embed.add_field(name="ID:", value=message.server.id, inline=True)
    serverinfo_embed.add_field(name="Cargos:", value=len(message.server.roles), inline=True)
    serverinfo_embed.add_field(name="Canais de texto:", value=len([message.channel.mention for channel in message.server.channels if channel.type==discord.ChannelType.text]), inline=True)
    serverinfo_embed.add_field(name="Canais de voz:", value=len([message.channel.mention for channel in message.server.channels if channel.type==discord.ChannelType.voice]), inline=True)
    serverinfo_embed.add_field(name="Membros:", value=len(message.server.members), inline=True)
    serverinfo_embed.add_field(name="Bots:", value=len([user.mention for user in message.server.members if user.bot]), inline=True)        
    serverinfo_embed.add_field(name="Região:", value=str(message.server.region).title(), inline=True)
    await client.send_message(message.channel,embed=serverinfo_embed)


  if message.content.startswith(prefix+'ban'):
    user = message.author.name
    if not message.author.server_permissions.ban_members:
      ban01_embed = discord.Embed(title="\n", description="Você não tem permissão para utilizar este comando.", color=0xFF0000)
      ban01_embed.set_thumbnail(url=message.server.icon_url)
      ban01_embed.set_footer(text="• Comando enviado por: {}.".format(user))
      return await client.send_message(message.channel,embed=ban01_embed)
    try:
      usuario = message.mentions[0]
      ban02_embed = discord.Embed(title="\n", description="O usuário <@{}> foi banido do servidor AtorexNetwork!".format(usuario.id), color=0xFF0000)
      ban02_embed.set_thumbnail(url=message.server.icon_url)
      ban02_embed.set_footer(text="• Comando enviado por: {}.".format(user))
      await client.send_message(message.channel,embed=ban02_embed)
      await client.ban(usuario,delete_message_days=2)
    except:
      ban03_embed = discord.Embed(title="\n", description="Você deve espicificar um usuário para bani-lo.", color=0xFF0000)
      ban03_embed.set_thumbnail(url=message.server.icon_url)
      ban03_embed.set_footer(text="• Comando enviado por: {}.".format(user))
      await client.send_message(message.channel,embed=ban03_embed)
    finally:
      pass


    if message.content.lower().startswith(prefix+'avatar'):
      try:
        user = message.author.name
        usuario = message.mentions[0]
        embed = discord.Embed(
          title="Avatar do(a): {}".format(usuario.name),
          color=0xFFFFFF,
          description="[Clique aqui]("+usuario.avatar_url+") para ver o avatar!"
            )
        embed.set_image(url=usuario.avatar_url)
        embed.set_footer(text="• Comando enviado por: {}.".format(user))
        await client.send_message(message.channel, embed=embed)



client.run('NDY0NjA0NDczOTMxODU3OTIx.DiBYJw.S2iTn7TXy7L9D1r1nLqryoaNOwg')
