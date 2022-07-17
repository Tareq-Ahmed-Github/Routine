import discord
import os

client = discord.Client()

@client.event
async def on_ready() :
      print('Logged in successfully')

@client.event 
async def on_message(message) :
  if message.author == client.user :
    return

  if message.content.startswith('$Saturday') :
    await message.channel.send('1. Compiler 10-12')
    await message.channel.send('2. Internet Programming 12-1')
    await message.channel.send('3. URED 2-4')
    
client.run(os.getenv('TOKEN'))
