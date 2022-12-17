import discord
from discord.ext import commands
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

@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cmds.{extension}')
    await ctx.send(f'Loaded {extension} done...')

@bot.command()
async def unload(ctx, extension):
    bot.load_extension(f'cmds.{extension}')
    await ctx.send(f'Unloaded {extension} done...')

@bot.command()
async def reload(ctx, extension):
    bot.load_extension(f'cmds.{extension}')
    await ctx.send(f'Reloaded {extension} done...')

    for filename in os.listdir("./cmds"):
        if filename.endswith('.py'):
            bot.load_extension(f"cmds.{filename[:-3]}")

if __name__ == "__main__":
    bot.run(jdata['TOKEN'])
