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


bot.run(jdata['TOKEN'])
