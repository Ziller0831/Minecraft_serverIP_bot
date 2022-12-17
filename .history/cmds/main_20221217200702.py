import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json
from requests import get

with open("setting.json", mode='r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

class Main(Cog_Extension):
    @commands.command()
    async ping(self, ctx):
        await ctx.send(f'{round(self.bot.latency*1000)}(ms)')

    @commands.command()
    async def serverIP(self, ctx):
        IP = get(jdata['IP_search_web']).content.decode('utf8')
        await ctx.send(f'Server IP:{IP}')

def setup(bot):
    bot.add_cog(Main(bot))