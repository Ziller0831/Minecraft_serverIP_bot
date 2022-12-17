import discord
from discord.ext import commands

class Main(commands.cog):
    def __init__(self, _bot):
        self.bot = bot

    @bot.command()
    async def rickroll(ctx):
    rickroll_gif = random.choice(jdata['rickroll_gif'])
    await ctx.send(rickroll_gif)
