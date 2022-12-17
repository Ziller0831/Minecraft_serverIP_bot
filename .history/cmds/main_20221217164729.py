import discord
from discord.ext import commands
From core

class Main(Cog_Extension):

    @commands.command()
    async def serverIP(self, ctx):
        IP = get('https://api.ipify.org').content.decode('utf8')
        await ctx.send(f'Server IP:{IP}')

def setup(bot):
    bot.add_cog(Main(bot))