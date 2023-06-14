from discord.ext import commands, tasks
import discord
import calculator
from matrix import Matrix
import matrix
from decouple import config


BOT_TOKEN = config('KEY') 
CHANNEL_ID = 1113263431299117137

bot = commands.Bot(command_prefix='!',  intents=discord.Intents.all())
bot.remove_command('help')

def run_math_bot():
    @bot.event
    async def on_command_error(ctx, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.send("Command does not exist. Do !help to see what I can do")
    @bot.command()
    async def format(ctx):
        format_basics = 'For !add, !divison, !multiply, and !subtract uses this format: Command number number number...\nEx:```!add 3 4 5\n!divison 3 4 5 6 NOTE: ((3/4)/5)/6```\n'
        format_calculate = 'For !calculate simply put your equation\nEx:```!calculate 8/2(2+4)```\n' 
        format_two_matrices= 'For !matrixAdd, !matrixMultiply and !matrixSubtract Give the ROWxCOLUMN of the first matrix followed by the contents from left to right, top to bottom seprated by a comma and the second matrix.Ex:```!matrixMultiply 2x3 1 2 1 3 4 1 , 3x4 5 6 1 1 7 8 1 1 1 1 1 1\nNOTE: This only allows 2 matrices, also make sure the dimensions are the same for add and subtract, and for multiply the first matrix columns are equal to the second matrix row```\n'
        format_one_matrix = 'For !matrixDeterminant, !matrixInverse, !matrixTranspose just give the matrix\nEx: ```!matrixDeterminant 2x2 2 3 4 5```\n'
        format_matrix_power = 'For !matrixPower give the Matrix comma power\nEx: ```!matrixPower 2x2 4 3 2 1 , 3```'
        await ctx.send(f'{format_basics}{format_calculate}{format_two_matrices}{format_one_matrix}{format_matrix_power}')
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
        numerator = int(arr[0])
        denominator = 1
        for i in range(1,len(arr)):
            denominator = denominator * int(arr[i])
        decimal = numerator/denominator
        await ctx.send(f'Your answer is: {numerator}/{denominator} or {decimal}')
    @bot.command()
    async def help(ctx):
        helptext = '```Here is what I can do!!! \n'
        for command in bot.commands:
            helptext+=f'\t{command}\n'
        helptext+='Check out !format first!```'
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
    async def matrixTranspose(ctx, *arr):
        l,c = matrix.make_matrices(arr)
        m,s = calculator.matrix_transpose(l[0])
        await ctx.send(f'{s}{m}')
    @bot.command()
    async def matrixDeterminant(ctx, *arr):
        l,c = matrix.make_matrices(arr)
        p,s = calculator.matrix_determinant(l[0])
        await ctx.send(f'{s}/n{p}')
    @bot.command()
    async def matrixInverse(ctx, *arr):
        l,c = matrix.make_matrices(arr)
        s = calculator.matrix_inverse(l[0])
        await ctx.send(f'{s}')
    @bot.command()
    async def griddy(ctx):
        embed = discord.Embed(
            color=(discord.Color.random()),
            description= f'{ctx.author} I griddy with you!'
        )
        embed.set_image(url='https://media.tenor.com/yfrLPeADRYAAAAAd/nfl-football.gif')
        await ctx.send(embed=embed)
    bot.run(BOT_TOKEN)