import os
from dotenv import load_dotenv
import discord
from discord.ext import commands

load_dotenv()

#############################################################################
## Discord Configuration
#############################################################################

TOKEN = os.getenv('TOKEN_ORC_POG')
CUSTOM_EMOJI_NAME = 'orc_pog' # Change this to what the emote name is :name_here: (without the : :)
CUSTOM_EMOJI_ID = 1204836858828423268 # Change this to your own custom ID

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
intents.guilds = True
client = commands.Bot(command_prefix='!', intents=intents)

#############################################################################
## Bot comes online
#############################################################################

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

#############################################################################
## React when user post a message or detect 'pog' or 'poggers' in a message
#############################################################################

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    print(f"Received message in channel {message.channel.name} ({message.channel.id}): {message.content}")

    emoji = discord.utils.get(client.emojis, id=CUSTOM_EMOJI_ID)
    if emoji:
        await message.add_reaction(emoji)

    if "pog" in message.content.lower() or "poggers" in message.content.lower():
        await message.channel.send(f"{message.author.mention} Poggers! <:{CUSTOM_EMOJI_NAME}:{CUSTOM_EMOJI_ID}>", reference=message)

    await client.process_commands(message)

client.run(TOKEN)