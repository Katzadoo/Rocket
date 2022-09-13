import os
import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
    if message.content.startswith('$rocket pass the butter'):
        await message.channel.send('Whats my purpose?')

    if message.content.startswith('$rocket you pass butter'):
        await message.channel.send('Oh my god.')


client.run('MTAxNzgyNjU1MTM3MjQ2MDA0Mg.GWRwa4.0gTGhjqtoRyL4EXLF7kKvH8AfSuWSeoVQhiabo')