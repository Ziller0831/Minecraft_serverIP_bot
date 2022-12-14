import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="+", intents=discord.Intents.all())

@bot.event
async def on_ready(): 
    print(">> Bot is online<<")

bot.run('MTA1MjU4ODE1ODU4OTYxNjE0OQ.Gn29Hz._xKPKyavFMSxEMhPHhxurb_Hl6ZwAGI3HIw0hM')
