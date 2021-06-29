import discord
from discord.ext import commands
from web import show_info
from web1 import search_class
import hash 
bot=commands.Bot(command_prefix="!")
table=hash.Hash(150)

@bot.command()
async def show(ctx,arg):
    print(arg)
    name,teacher,when=show_info(arg)
    link=search_class(name,teacher)
    message="課程名稱:"+name+" "+"\n"+"教師姓名:"+teacher+"\n"+"上課時間"+when+"\n"+"ntu course: "+link
    await ctx.send(message)
    _list=[name,teacher,when,link]
    table._insert(_list)
@bot.command()    
async def show_all(ctx):
    result=table.output()
    print(result)
    await ctx.send(result)
@bot.command()   
async def find(ctx,arg1,arg2):
    arg=arg1+' '+arg2
   
    result=table.find(arg)
    print(result)
    await ctx.send(result)

bot.run("ODU3OTc0NjE3OTA5ODg2OTg2.YNXZIQ.dLEowdY5wJvaLuuoo9vfxTqSQDU") 
