import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json

with open("setting.json", mode='r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

class React(Cog_Extension):


def setup(bot):
    bot.add_cog(Main(bot))
