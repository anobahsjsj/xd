import json
import requests
import random
import aiohttp
import io
import discord
from discord.ext import commands
import os
intents = discord.Intents.all()
intents.members = True

client = commands.Bot(command_prefix = "*", intents = intents)

@client.event
async def on_ready():
	print('Подключено к {0.user}'.format(client))

@client.event
async def on_message(message):
	if message.author == client.user:
		return
	if message.content.startswith('<@962700278853959770>'):
		await message.channel.send('**Мои команды - *хелп**')

	await client.process_commands(message)
 
@client.command()
async def хелп(ctx):
	embed = discord.Embed(
	title = "Команды бота",
	description = "***кот *собака *лиса *хелп**",
	color = discord.Colour(random.randint(111111, 999999)))
	embed.set_footer(text = f"Команду использовал {ctx.author.name}")
	await ctx.reply(embed = embed)
	
@client.command()
async def лиса(ctx):
    response = requests.get('https://some-random-api.ml/img/fox')
    json_data = json.loads(response.text)
    embed = discord.Embed(color = discord.Colour(random.randint(111111, 999999)), title = 'Лиса')
    embed.set_image(url = json_data['link'])
    embed.set_footer(text = f"Команду использовал {ctx.author.name}")
    await ctx.send(embed = embed)

@client.command()
async def собака(ctx):
    response = requests.get('https://some-random-api.ml/img/dog')
    json_data = json.loads(response.text)

    embed = discord.Embed(color = discord.Colour(random.randint(111111, 999999)), title = 'Собачка')
    embed.set_image(url = json_data['link'])
    embed.set_footer(text = f"Команду использовал {ctx.author.name}")
    await ctx.send(embed = embed)

@client.command()
async def кот(ctx):
    response = requests.get('https://some-random-api.ml/img/cat')
    json_data = json.loads(response.text)

    embed = discord.Embed(color = discord.Colour(random.randint(111111, 999999)), title = 'Кот')
    embed.set_image(url = json_data['link'])
    embed.set_footer(text = f"Команду использовал {ctx.author.name}") 
    await ctx.send(embed = embed)
client.run('OTYyNzAwMjc4ODUzOTU5Nzcw.GwtaS4.7zlzwkJzf4M8cP4x0UjH8X3IEnaXSDKF7sk8zw')