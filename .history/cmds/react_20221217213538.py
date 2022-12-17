import discord
import json
import random


with open("setting.json", mode='r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

class React(Cog_Extension):
    @commands.command()
    async def rickroll(self, ctx):
        rickroll_gif = random.choice(jdata['rickroll_gif'])
        await ctx.send(rickroll_gif)

def setup(bot):
    bot.add_cog(React(bot))
