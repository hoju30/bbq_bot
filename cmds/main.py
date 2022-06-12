#副程式main
import  discord 
from discord.ext import commands
from core.classes import Cog_Extension

class Main(Cog_Extension):

    @commands.command()
    async def ping(selF,ctx):#顯示ping
        await ctx.send(f"{round(selF.bot.latency*1000)}ms")
    
    @commands.command()
    async def hi(selF,ctx):#說"hi"
        await ctx.send(f"hi")

def setup(bot):
    bot.add_cog(Main(bot))