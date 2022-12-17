import discord
from discord.ext import commands
from requests import get
import json
import random
import os

with open("setting.json", mode='r', encoding='utf8') as jfile:
    jdata = json.load(jfile)


bot = commands.Bot(command_prefix="+", intents=discord.Intents.all())

@bot.event
async def on_ready():
    # channel = bot.get_all_channels(int(jdata['Minecraft_channel']))
    print("Bot is online")

@bot.
for filename in os.listdir('./cmds'):
    if filename.endswith('.py'):
        bot.load_extension(f'cmds.{filename[:-3]}')

if __name__ == "__main__":
    bot.run(jdata['TOKEN'])
