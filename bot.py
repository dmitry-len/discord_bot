import discord
from discord.ext import commands
from config import settings
import json
import requests

bot = commands.Bot(command_prefix = settings['prefix'])

@bot.command() 
@commands.has_any_role(872927248888524921, 745959363297935400)      
async def hello(ctx): 
    author = ctx.message.author 
    await ctx.send(f'Hello, {author.mention}!')

@bot.command()
@commands.has_any_role(872927248888524921, 745959363297935400) 
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()


@bot.command()
@commands.has_any_role(872927248888524921, 745959363297935400) 
async def lessGo(ctx, user: discord.Member):
    x=0
    channel1 = bot.get_channel(745954103795908678)
    channel2 = bot.get_channel(745954704256925758)
    user = await ctx.guild.fetch_member(user.id)
    while x < 20:
            await user.move_to(channel1)
            await user.move_to(channel2)
            x+=1

@bot.command()
async def wink(ctx):
    response = requests.get('https://some-random-api.ml/animu/wink') # Get-запрос
    json_data = json.loads(response.text) # Извлекаем JSON

    embed = discord.Embed(color = 0xff9900, title = 'wink') # Создание Embed'a
    embed.set_image(url = json_data['link']) # Устанавливаем картинку Embed'a
    await ctx.send(embed = embed) # Отправляем Embed

@bot.command()
async def hug(ctx):
    response = requests.get('https://some-random-api.ml/animu/hug') # Get-запрос
    json_data = json.loads(response.text) # Извлекаем JSON

    embed = discord.Embed(color = 0xff9900, title = 'hug') # Создание Embed'a
    embed.set_image(url = json_data['link']) # Устанавливаем картинку Embed'a
    await ctx.send(embed = embed) # Отправляем Embed

@bot.command()
async def pat(ctx):
    response = requests.get('https://some-random-api.ml/animu/pat') # Get-запрос
    json_data = json.loads(response.text) # Извлекаем JSON

    embed = discord.Embed(color = 0xff9900, title = 'pat') # Создание Embed'a
    embed.set_image(url = json_data['link']) # Устанавливаем картинку Embed'a
    await ctx.send(embed = embed) # Отправляем Embed

@bot.command()
async def cat(ctx):
    response = requests.get('https://some-random-api.ml/img/cat') # Get-запрос
    json_data = json.loads(response.text) # Извлекаем JSON

    embed = discord.Embed(color = 0xff9900, title = 'Рандомный кот') # Создание Embed'a
    embed.set_image(url = json_data['link']) # Устанавливаем картинку Embed'a
    await ctx.send(embed = embed) # Отправляем Embed

@commands.has_permissions(ban_members=True)
@bot.command()
async def ban(ctx, user: discord.Member, *, reason="No reason provided"):
        await user.ban(reason=reason)
        ban = discord.Embed(title=f":boom: Banned {user.name}!", description=f"Reason: {reason}\nBy: {ctx.author.mention}")
        await ctx.message.delete()
        await ctx.channel.send(embed=ban)
        await user.send(embed=ban)

bot.run(settings['token']) 

