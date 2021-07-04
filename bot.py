from asyncio.events import Handle
import discord
from discord.ext import commands
from matplotlib.pyplot import table
from web import show_info
import hash
import schedule
from save_data import Data
bot=commands.Bot(command_prefix="!")
#error handling

@bot.event
async def on_command_error(ctx,error):
    if isinstance(error,commands.CommandNotFound):
        await ctx.send('無效的指令')
    elif isinstance(error,commands.CommandInvokeError):
        if str(error).split(':')[1]==" KeyError":
            await ctx.send('請先執行!connect')
        else:
            await ctx.send('請檢查指令是否輸入錯誤')
    else:
        await ctx.send("請檢察指令是否輸入錯誤")

## initial
database=Data()
class_schedule = schedule.ClassSchedule()
#load data
@bot.command()
async def connect(ctx):
    database.database[str(ctx.guild.id)]=hash.Hash(150) # initial Hash
    print(database.database[str(ctx.guild.id)])
    database.load(str(ctx.guild.id))

@bot.command ()
async def disconnect(ctx):
    database.save(str(ctx.guild.id))
    del database.database[str(ctx.guild.id)]

@bot.command()
async def show(ctx,arg):
    table=database.database[str(ctx.guild.id)]
    name,teacher,when,credit=show_info(arg)
    link="https://www.ptt.cc/bbs/NTUcourse/search?q=+"+teacher
    message="課程名稱:"+name+" "+"\n"+"教師姓名:"+teacher+"\n"+"上課時間"+when+"\n"+"ntu course: "+link
    await ctx.send(message)

    _list=[name,teacher,when,credit,0,0,link]
    key=name+' '+teacher       #新增key尋找有沒有已經被加入過了

    if type(table.search(key))==str:
        table.insert(_list)
    else:
        pass

@bot.command()
async def show_all(ctx):
    table=database.database[str(ctx.guild.id)]
    result=table.list_all()
    if result=='':
        result='no class inside'
    await ctx.send(result)

@bot.command()
async def find(ctx,arg1,arg2):
    arg=arg1+' '+arg2
    table=database.database[str(ctx.guild.id)]
    pointer=table.search(arg)
    if type(pointer)==str:
        await ctx.send(pointer)
    else:
        result=pointer.output()
        await ctx.send(result)

@bot.command()
async def comment(ctx,arg1,arg2,arg3):
    arg=arg1+' '+arg2
    table=database.database[str(ctx.guild.id)]
    table.add_comment(ctx,arg,arg3)

@bot.command()
async def clear(ctx,arg1,arg2):
    arg=arg1+' '+arg2
    table=database.database[str(ctx.guild.id)]
    table.clear_comment(ctx,arg)

@bot.command()
async def liked(ctx,arg1,arg2):
    arg = arg1+' '+arg2
    table=database.database[str(ctx.guild.id)]
    table.great_points(arg)

@bot.command()
async def disliked(ctx,arg1,arg2):
    arg = arg1+' '+arg2
    table=database.database[str(ctx.guild.id)]
    table.disliked_points(arg)

@bot.command()
async def save(ctx):
    table=database.database[str(ctx.guild.id)]
    table.save_data()

@bot.command()
async def add_to_schedule(ctx,arg1,arg2):
    username = str(ctx.author)
    arg = arg1 + ' ' + arg2
    table=database.database[str(ctx.guild.id)]
    if class_schedule.add(arg,table,username) == False :
        await ctx.send('你已經有選這堂課')
    else:
        await ctx.send('課程已加入')

@bot.command()
async def delete_from_schedule(ctx,arg1,arg2):
    username = str(ctx.author)
    arg = arg1 + ' ' + arg2
    table=database.database[str(ctx.guild.id)]
    if class_schedule.delete(arg,table,username) == False :
        await ctx.send('你沒有選這堂課')
    else :
        await ctx.send('課程已刪除')

@bot.command()
async def show_schedule(ctx):
    username = str(ctx.author)
    embedVr = class_schedule.show(username)
    await ctx.send(embed = embedVr)

