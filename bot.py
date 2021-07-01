import discord
from discord.ext import commands
from web import show_info
from web1 import search_class
import hash 
from add_table import add_to_table
from  show_table import show_table
from delete_from_table import  delete_from_table
bot=commands.Bot(command_prefix="!")
table=hash.Hash(150)

@bot.command()
async def show(ctx,arg):
    
    name,teacher,when=show_info(arg)
    link=search_class(name,teacher)
    message="課程名稱:"+name+" "+"\n"+"教師姓名:"+teacher+"\n"+"上課時間"+when+"\n"+"ntu course: "+link
    await ctx.send(message)
    _list=[name,teacher,when,link]
    table.insert(_list)
@bot.command()    
async def show_all(ctx):
    result=table.list_all()
    await ctx.send(result)
@bot.command()   
async def find(ctx,arg1,arg2):
    arg=arg1+' '+arg2

    pointer=table.search(arg)
    if type(pointer)==str:
        await ctx.send(pointer)
    else:
        result=pointer.output()
        await ctx.send(result)

@bot.command()
async def add_class(ctx,arg1,arg2):
    arg=arg1+' '+arg2 
    add_to_table(arg,table)

@bot.command()
async def show_class(ctx):
    table_shown=show_table()
    print(table_shown)

@bot.command()
async def delete(ctx,arg1,arg2):
    arg=arg1+' '+arg2
    delete_from_table(arg,table)
@bot.command()
async def comment(ctx,arg1,arg2,arg3):
    arg=arg1+' '+arg2
    table.add_comment(ctx,arg,arg3)

