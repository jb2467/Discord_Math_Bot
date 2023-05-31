from discord.ext import commands, tasks
import discord
import calculator


BOT_TOKEN = 'MTExMTg1NTk0MDM5NjkyNTA4MA.G_7iDb.TXjttrfLVDdOk-jmal0Iuv9Brr0VsFo9pZ9ibg'
CHANNEL_ID = 1113263431299117137

bot = commands.Bot(command_prefix="!",  intents=discord.Intents.all())
bot.remove_command('help')
def run_math_bot():
    
    @bot.event
    async def on_ready():
        channel = bot.get_channel(CHANNEL_ID)
        await channel.send("Hello! Math bot at your service!")

    @bot.command()
    async def add(ctx, *arr):
        res = 0
        for element in arr:
            res += int(element)
        await ctx.send(f'Your answer is: {res}')
    @bot.command()
    async def subtract(ctx, *arr):
        res = int(arr[0])
        for i in range(1,len(arr)):
            res -= int(arr[i])
        await ctx.send(f'Your answer is: {res}')

    @bot.command()
    async def division(ctx, *arr):
        res = int(arr[0])
        for i in range(1,len(arr)):
            res = res / int(arr[i])
        await ctx.send(f'Your answer is: {res}')
    @bot.command()
    async def help(ctx):
        helptext = "```Here is what I can do!!! \n"
        for command in bot.commands:
            helptext+=f"\t{command}\n"
        helptext+="```"
        await ctx.send(helptext)
    @bot.command()
    async def multiply(ctx, *arr):
        res = int(arr[0])
        for i in range(1,len(arr)):
            res = res * int(arr[i])
        await ctx.send(f'Your answer is: {res}')
    @bot.command()
    async def calculate(ctx, *arr):
        c = calculator.calculate(arr)
        string = ''
        index = 0
        for element in c:
            string += f'Step{index}: {element}  \n'
            index+=1
        string += 'Final answer!: ' +str(eval(c[-1]))
        await ctx.send(string)
    
    @bot.command()
    async def griddy(ctx):
        embed = discord.Embed(
            color=(discord.Color.random()),
            description= f'{ctx.author} I griddy with you!'
        )
        embed.set_image(url='https://media.tenor.com/yfrLPeADRYAAAAAd/nfl-football.gif')
        await ctx.send(embed=embed)
    bot.run(BOT_TOKEN)