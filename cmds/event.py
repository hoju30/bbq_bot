#副程式event
import  discord 
from discord.ext import commands
from core.classes import Cog_Extension
import json
with open("set.json","r",encoding="utf8") as jfile:
    jdata=json.load(jfile)

class Event(Cog_Extension):

    @commands.Cog.listener()#顯示歡迎成員
    async def  on_member_join(self,member):
        channel = self.bot.get_channel(int(jdata["Welcome"]))
        await channel.send(f"{member}join!")

    @commands.Cog.listener()#顯示成員離開
    async def  on_member_remove(self,member):
        channel = self.bot.get_channel(int(jdata["Leave"]))
        await channel.send(f"{member}leave!")
    
    @commands.Cog.listener()
    async def on_message(self,msg):
        if msg.content in jdata["subject"] and msg.author!=self.bot.user:#輸入的內容包含"apple"
            await msg.channel.send("玩了.... 玩啦!八比Q拉 玩拉!玩啦! 我丟我操 這不是給我燒烤了嗎挖草你這....牛b阿兄弟!挖草 芭比Q~~~~~~~~~")#找出輸入內容的頻道並輸出"hi"

def setup(bot):
    bot.add_cog(Event(bot))