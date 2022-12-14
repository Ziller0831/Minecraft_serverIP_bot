import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="+", intents=discord.Intents.all())

@bot.event
async def on_ready(): 
    print(">> Bot is online<<")

bot.run('https://discord.com/api/oauth2/authorize?client_id=1052588158589616149&permissions=2048&scope=bot%20applications.commands')
 