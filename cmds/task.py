#任務副程式
import  discord 
from discord.ext import commands
from core.classes import Cog_Extension
import json,asyncio,datetime

class Task(Cog_Extension):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)#父類別初始化設定

        self.counter=0
        self.counter2=0
        
        async def time_task():
            await self.bot.wait_until_ready()#準備
            self.channel=self.bot.get_channel(896816735171264585)
            while not self.bot.is_closed():#在線上
                now_time=datetime.datetime.now().strftime("%H%M")
                with open("set.json","r",encoding="utf8") as jfile:
                    jdata=json.load(jfile)
                if now_time==jdata["time"] and self.counter==0:#對應時間
                    await self.channel.send("Time correct")#顯示"Time correct"
                    self.counter=1
                    await asyncio.sleep(1)
                else:
                    await asyncio.sleep(1)
                    pass

        self.bg_task=self.bot.loop.create_task(time_task())#背景作業

    @commands.command()
    async def set_time(self,ctx,time):
        self.counter=0
        with open("set.json","r",encoding="utf8") as jfile:#讀取資料庫
            jdata=json.load(jfile)
        jdata["time"]=time
        with open("set.json","w",encoding="utf8") as jfile:#寫入資料庫
            json.dump(jdata,jfile,indent=4)   

def setup(bot):
    bot.add_cog(Task(bot))