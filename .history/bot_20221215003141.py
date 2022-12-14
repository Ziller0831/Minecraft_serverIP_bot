import discord
from discord.ext import commands
from requests import get

bot = commands.Bot(command_prefix="+", intents=discord.Intents.all())

@bot.event
async def on_ready(): 
    print("Bot is online")

@bot.command()
async def serverIP(ctx):
    await ctx.send(fip)

bot.run('MTA1MjU4ODE1ODU4OTYxNjE0OQ.GwuiwX.570rK5TEPgse5lIQM0rPqlD7efntI6Qh9W5mtg')
