from discord.ext import commands, tasks
import discord
import calculator
from matrix import Matrix
import matrix

BOT_TOKEN = ''
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
            string += f'Step {index}: {element}  \n'
            index+=1
        string += 'Final answer!: ' +str(eval(c[-1]))
        await ctx.send(string)
    @bot.command()
    async def matrixAdd(ctx, *arr):
        l,c = matrix.make_matrices(arr)
        if c == 2:
            p,s = calculator.add_matrices(l)
            if p :
                await ctx.send(f'{s}{p}')
            else:
                await ctx.send('`You can not add these matrices, check the dimensions. The Matricies must have the same number of rows and the same number of coloumns`')
        else:
            await ctx.send('There are not enough matrices')
        

    @bot.command()
    async def matrixSubtract(ctx, *arr):
        l,c = matrix.make_matrices(arr)
        if c == 2:
            p,s = calculator.subtract_matrices(l)
            if p :
                await ctx.send(f'{s}{p}')
            else:
                await ctx.send('`You can not subtract these matrices, check the dimensions. The Matricies must have the same number of rows and the same number of coloumns`')
        else:
            await ctx.send('There are not enough matrices')
    @bot.command()
    async def matrixMultiply(ctx, *arr):
        l,c = matrix.make_matrices(arr)
        if c == 2:
            p,s = calculator.multiply_matrices(l)
            if p:
                await ctx.send(f'{s}{p}')
            else:
                await ctx.send('`You can not multiply these matrices, check the dimensions`')
        else:
            await ctx.send('There are not enough matrices')

    @bot.command()
    async def matrixPower(ctx, *arr):
        temp = ''
        for element in arr:
            temp += str(element) + ' '
        spl = temp.split(' , ')
        m = spl[0]
        i = m.find('x')
        j = m.find(' ')
        row = int(m[:i])
        col = int(m[i+1:j])
        data_set = m[j+1:].split(' ')
        power = int(spl[-1])
        matrix = Matrix(row,col,data_set)
        p,c = calculator.matrix_power_to(matrix, power)
        await ctx.send(f'{c}')
    @bot.command()
    async def griddy(ctx):
        embed = discord.Embed(
            color=(discord.Color.random()),
            description= f'{ctx.author} I griddy with you!'
        )
        embed.set_image(url='https://media.tenor.com/yfrLPeADRYAAAAAd/nfl-football.gif')
        await ctx.send(embed=embed)
    bot.run(BOT_TOKEN)