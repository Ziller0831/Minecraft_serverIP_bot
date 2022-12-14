import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='[')

@bot.event
async def on_ready():
    print(">> Bot is online<<")

bot.run('MTA1MjU4ODE1ODU4OTYxNjE0OQ.GzjLnR.cGsPLxlk_ZDazbz8FMm0Y0B-Plnq8LLLxgbQQ8')
