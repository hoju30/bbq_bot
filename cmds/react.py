#副程式react
import  discord 
from discord.ext import commands
from core.classes import Cog_Extension
import json
import random
with open("set.json","r",encoding="utf8") as jfile:
    jdata=json.load(jfile)

class react(Cog_Extension):
    

    @commands.command()
    async def 圖片(selF,ctx):
        random_pic=random.choice(jdata["pic"])
        pic=discord.File(random_pic)
        await ctx.send(file=pic)

    @commands.command()
    async def web(selF,ctx):
        random_pic=random.choice(jdata["url"])
        await ctx.send(random_pic)

    
def setup(bot):
    bot.add_cog(react(bot))