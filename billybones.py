import discord
intents = discord.Intents.none()
intents.guilds = True
intents.members = True
intents.messages = True

client = discord.Client(intents=intents)

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    await message.channel.send(message.content)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

client.run('MTA2ODE5NzAwMDE4NjcwMzg5NA.GBNMtE.boK4WQt86sxmMkLSYX_GadUiIFdrLKjf4fEyeU')