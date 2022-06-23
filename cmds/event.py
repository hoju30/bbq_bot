#事件副程式
import  discord 
from discord.ext import commands
from core.classes import Cog_Extension
import json
with open("set.json","r",encoding="utf8") as jfile:
    jdata=json.load(jfile)

class Event(Cog_Extension):

    @commands.Cog.listener()
    async def on_message(self,msg):
        if msg.content in jdata["subject"] and msg.author!=self.bot.user:#自動偵測關鍵字
            await msg.channel.send("完了.... 完啦!八比Q拉 玩拉!玩啦! 我丢我操 这不是给我烧烤了吗挖草你这....牛b阿兄弟!挖草 芭比Q~")
    
    @commands.Cog.listener()
    async def on_command_error(self,ctx,error):#偵錯
        if isinstance(error,commands.errors.MissingRequiredArgument):
            await ctx.send("遺失參數拉")
        elif isinstance(error,commands.errors.CommandNotFound):
            await ctx.send("沒這指令拉")
        else:
            await ctx.send("發生錯誤瞜")

    @commands.Cog.listener()
    async def on_raw_reaction_add(self,data):#反映貼圖取得身分組
        if data.message_id==986084663552528405:
            if str(data.emoji)=="<:bbq:986092576186703892>":#如果新增反映貼圖==""
                guild=self.bot.get_guild(data.guild_id)#取得伺服器
                role=guild.get_role(986075753231835176)#設定身分組
                await data.member.add_roles(role)#給予做出反應的成員身分組
                await data.member.send(f"你取得了{role}身分組")
    '''            
    @commands.Cog.listener()
    async def on_raw_reaction_remove(self,data):
        if data.message_id==986084663552528405:
            if str(data.emoji)=="<:bbq:986092576186703892>":
                guild=self.bot.get_guild(data.guild_id)
                user=guild.get_member(data.user_id)
                role=guild.get_role(986075753231835176)
                await user.remove_roles(role)
                await user.send(f"你移除了{role}身分組")

    @commands.Cog.listener()#顯示歡迎成員
    async def  on_member_join(self,member):
        channel = self.bot.get_channel(int(jdata["Welcome"]))
        await channel.send(f"{member}welcome!")

    @commands.Cog.listener()#顯示成員離開
    async def  on_member_remove(self,member):
        channel = self.bot.get_channel(int(jdata["Leave"]))
        await channel.send(f"{member}byebye!")'''

def setup(bot):
    bot.add_cog(Event(bot))