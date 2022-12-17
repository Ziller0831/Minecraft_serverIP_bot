import discord
from discord.ext import commands

class Main(commands.cog):
    def __init__(self, _bot):
        self.bot = bot

    @commands.command()
    async def serverIP(self, ctx):
        IP = get('https://api.ipify.org').content.decode('utf8')
        await ctx.send(f'Server IP:{IP}')
