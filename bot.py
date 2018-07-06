import discord
import asyncio

client = discord.Client()

@client.event
async def on_ready():
  print('BOT ONLINE')


@client.event
async def on_message(message):
  if message.content.lower().startswith('/skell'):
    await client.send_message(message.channel, "Sem palavras para descrever o @skell#3434!!! <3")


client.run('NDY0NjA0NDczOTMxODU3OTIx.DiBYJw.S2iTn7TXy7L9D1r1nLqryoaNOwg')
