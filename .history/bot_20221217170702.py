import discord
from discord.ext import commands
from requests import get
import json
import random
import os

bot = commands.Bot(command_prefix="+", intents=discord.Intents.all())

@bot.event
async def on_ready():
    # channel = bot.get_all_channels(int(jdata['Minecraft_channel']))
    print("Bot is online")

for filename in os.listdir('./cmds'):
    if filename.endswith('.py'):
        bot.load_extension(f'cmds.{')


bot.run(jdata['TOKEN'])
