import discord
from discord.ext import commands
from web import show_info
from web1 import search_class
import hash 

bot=commands.Bot(command_prefix="!")
## initial 
table=hash.Hash(150)
#load data 
with open('data.txt','r',encoding="utf-8") as data:
    for line in data :
        line=line.split('!')
        line[6]=line[6][:-1]
        table.insert(line)



@bot.command()
async def show(ctx,arg):
    
    name,teacher,when,credit=show_info(arg)
    if when:   #檢查傳回值是否異常
        when=when.strip()
    if not when:
        when=''
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
    result=table.list_all()
    if result=='':
        result='no class inside'
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
'''
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
    '''
@bot.command()
async def comment(ctx,arg1,arg2,arg3):
    arg=arg1+' '+arg2
    table.add_comment(ctx,arg,arg3)

@bot.command()
async def clear(ctx,arg1,arg2):
    arg=arg1+' '+arg2
    table.clear_comment(ctx,arg)

@bot.command()
async def liked(ctx,arg1,arg2):
    arg = arg1+' '+arg2
    table.great_points(arg)

@bot.command()
async def disliked(ctx,arg1,arg2):
    arg = arg1+' '+arg2
    table.disliked_points(arg)

@bot.command()
async def save(ctx):
    table.save_data()
