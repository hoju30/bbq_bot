#主程式
import  discord 
from discord.ext import commands
import json
import os
with open("set.json","r",encoding="utf8") as jfile:
    jdata=json.load(jfile)


bot=commands.Bot(command_prefix="[")

@bot.event
async def on_ready():
    print(">>bot is online<<")

@bot.command()#上傳指令
async def load(ctx,extension):
    bot.load_extension(f"cmds.{extension}")
    await ctx.send(f"loaded {extension} done.")

@bot.command()#重載指令
async def reload(ctx,extension):
    bot.reload_extension(f"cmds.{extension}")
    await ctx.send(f"re-loaded {extension} done.")
    
@bot.command()#取消指令
async def unload(ctx,extension):
    bot.unload_extension(f"cmds.{extension}")
    await ctx.send(f"unloaded {extension} done.")

for Filename in  os.listdir("./cmds"):#列出所有資料夾下的文件不用一一在import
    if Filename.endswith(".py"):
        bot.load_extension(f"cmds.{Filename[:-3]}")#去掉".py"

if __name__=="__main__":
    bot.run(jdata["TOKEN"])