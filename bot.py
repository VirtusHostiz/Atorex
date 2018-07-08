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
    await client.send_message(message.channel,embed=serverinfo_embed)


  if message.content.lower().startswith(prefix+'avatar'):
      try:
        user = message.mentions[0]
        embed =discord.Embed(
          title="Avatar de {}:".format(user.name),
          color=0xFFFFFF
        )
        embed.set_image(url=user.avatar_url)
        embed.set_footer(text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
        await client.send_message(message.channel, embed=embed)
      except IndexError:
        user2 = message.author
        embed2 = discord.Embed(
          title="Avatar de {}:".format(user2.name),
          color=0xFFFFFF,
        )
        embed2.set_image(url=user2.avatar_url)
        embed2.set_footer(text="• Comando enviado por {}#{}.".format(message.author.name, message.author.discriminator))
        await client.send_message(message.channel, embed=embed2)



client.run('NDY0NjA0NDczOTMxODU3OTIx.DiBYJw.S2iTn7TXy7L9D1r1nLqryoaNOwg')
