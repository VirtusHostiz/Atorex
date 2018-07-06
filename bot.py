import discord
import asyncio

client = discord.Client()

@client.event
async def on_ready():
  await client.change_status(game=discord.Game(name='/skell'))
  print('[BOT ONLINE COM SUCESSO]')


@client.event
async def on_message(message):
  if message.content.lower().startswith('/skell'):
    await client.send_message(message.channel, message.author.mention",\n```fix\nSem palavras para descrever o ySkell!!!\n```")


client.run('NDY0NjA0NDczOTMxODU3OTIx.DiBYJw.S2iTn7TXy7L9D1r1nLqryoaNOwg')
