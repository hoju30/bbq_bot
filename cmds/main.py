#命令副程式
import  discord 
from discord.ext import commands
from core.classes import Cog_Extension
import datetime
import time

class Main(Cog_Extension):

    @commands.command()
    async def ping(selF,ctx):#顯示ping
        await ctx.send(f"{round(selF.bot.latency*1000)}ms")

    @commands.command()
    async def 早上好中國(selF,ctx):#說"現在我有冰淇淋"
        await ctx.send("現在我有冰淇淋")
    
    @commands.command()
    async def bbq(self,ctx):#簡介製作
        embed=discord.Embed(title="BBQ", url="https://youtu.be/lbydPkfy4tg", description="BBQ",timestamp=datetime.datetime.now())
        embed.set_author(name="hoju", url="https://i.imgur.com/a8uJj0Bh.jpg", icon_url="https://i.imgur.com/a8uJj0Bh.jpg")
        embed.set_thumbnail(url="https://i.imgur.com/a8uJj0Bh.jpg")
        embed.add_field(name="q", value="undefined", inline=True)
        embed.add_field(name="bbq", value="undefined", inline=True)
        embed.add_field(name="芭比Q", value="undefined", inline=False)
        await ctx.send(embed=embed)
         
    @commands.command()
    async def sayd(self,ctx,*,msg):#機器人說話
        await ctx.message.delete()
        await ctx.send(msg)

    @commands.command()
    async def clean(self,ctx,num:int):#刪除訊息
        await ctx.channel.purge(limit=num+1)    

    '''@commands.command()
    async def status(self,ctx):
        online=[]
        for member in ctx.guild.members:
            if str(member.status)=="online":
                online.append(member)
        await ctx.send(online)'''

    @commands.group()
    async def mood(self,ctx):
        pass

    @mood.command()
    async def gt(self,ctx):
        await ctx.send("keep on")
        
    @mood.command()
    async def bd(self,ctx):
        await ctx.send("don't mind")

    @commands.command()
    async def time(self,ctx):#輸出現在時間
        await ctx.send(time.ctime())

def setup(bot):
    bot.add_cog(Main(bot))