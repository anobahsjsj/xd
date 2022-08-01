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

bot = commands.Bot(command_prefix = "бен!", intents = intents)
bot.activity = discord.Streaming(name = "Мои команды — бен!хелп", url = "https://google.com/")
@bot.event
async def on_ready():
	print('Подключено к {0.user}'.format(bot))

@bot.event
async def on_message(message):
	if message.author == bot.user:
		return
	if message.content.startswith('<@962700278853959770>'):
		await message.channel.send('***Мои команды - бен!хелп***')

	await bot.process_commands(message)

@bot.event
async def on_command_error(ctx, error):
	if isinstance(error, commands.CommandNotFound ):
		await ctx.send(embed = discord.				Embed(title ="Ошибка!", description = f'**Данная команда не найдена!**', color = discord.Color.red()))

@bot.command()
async def хелп(ctx):
	embed = discord.Embed(
	title = "Команды Бена",
	description = "**бен!кот — Показывает милого котика\nбен!собака — Показывает милую собачку\nбен!лиса — Показывает милую лисичку\nбен!хелп — Список комманд\nбен!инфо — Информация о боте\nбен!спросить — Спрашивает у бена вопрос\nбен!колба — Смешивает 2 элемента в лаборатории\nбен!кормить — Кормит бена бобами\nбен!напоить — Напоит бена яблочным соком**",
	color = discord.Colour(random.randint(111111, 999999)))
	embed.set_footer(text = f"Команду использовал {ctx.author.name}")
	await ctx.reply(embed = embed)
	
@bot.command()
async def лиса(ctx):
    response = requests.get('https://some-random-api.ml/img/fox')
    json_data = json.loads(response.text)
    embed = discord.Embed(color = discord.Colour(random.randint(111111, 999999)), title = '🦊Лисичка!🦊')
    embed.set_image(url = json_data['link'])
    embed.set_footer(text = f"Команду использовал {ctx.author.name}")
    await ctx.send(embed = embed)

@bot.command()
async def собака(ctx):
    response = requests.get('https://some-random-api.ml/img/dog')
    json_data = json.loads(response.text)

    embed = discord.Embed(color = discord.Colour(random.randint(111111, 999999)), title = '🐕Собачка!🐶')
    embed.set_image(url = json_data['link'])
    embed.set_footer(text = f"{ctx.author.name}")
    await ctx.send(embed = embed)

@bot.command()
async def кот(ctx):
    response = requests.get('https://some-random-api.ml/img/cat')
    json_data = json.loads(response.text)

    embed = discord.Embed(color = discord.Colour(random.randint(111111, 999999)), title = '🐱Котик!🐈')
    embed.set_image(url = json_data['link'])
    embed.set_footer(text = f"Команду использовал {ctx.author.name}") 
    await ctx.send(embed = embed)
    
bot.remove_command("help")

@bot.command()
async def спросить(ctx, message = None):
    if message == None:
    	embed = discord.Embed(
    	title = "Эй!",
    	description = "**Ты не написал вопрос! Пиши: бен!спросить (вопрос)**",
    	color = discord.Color.red())
    	await ctx.send(embed=embed)
    else:
    	answers = ["Yes!","No!","Ho-ho-ho!","Ho-ho-ho! No!", "Ho-ho-ho! Yes!"]
    	xd = random.choice(answers)
    	embed = discord.Embed(
    	title = 'Вопрос/Ответ',
    	description = f"**Бен ответил: {xd}**",
    	color = discord.Colour(random.randint(111111, 999999)))
    	embed.set_footer(text = f"Команду использовал {ctx.author.name}")
    	await ctx.send(embed=embed)
    	
    	
@bot.command()
async def инфо(ctx):
    embed = discord.Embed(
        title = "Информация о бене",
        description = f"> **Профиль бота:** ``{bot.user}``\n> **Версия бота:** ``2.0``\n> **2 имя бота:** ``{bot.user.name}``\n> **ID бота:** ``{bot.user.id}``\n> **Пинг бота:** ``{round(bot.latency)}ms``",
        color = discord.Colour(random.randint(111111, 999999)))
    embed.set_footer(text = f"Команду использовал {ctx.author.name}")
    await ctx.reply(embed = embed)
    
@bot.command()
async def колба(ctx, *, message = None):
	
	if len(message.split(" "))<2:
		embed = discord.Embed(title="Ошибка!",description="**Введите минимум 2 элемента которые надо смешать в колбу, пример: бен!колба спрайт кока-кола**",color=discord.Color.red())
		await ctx.send(embed=embed)
	else:
		d = ["колба взорвалась а бен почернел", "в колбе образовался вкуснейший напиток и бен его выпил", "в колбе образовалась очень странная и не вкусная житкость", "в колбе образовался слизняк! Бен ели его сжег!", "в колбе образовалась обычная пена", "колба взорвалась, но силу взрыва лишь хватило чтобы колба разлетелась на куски стекла и все", "в колбе получился странный на вкус напиток"]
		xd = random.choice(d)
		embed = discord.Embed(
		title = "Лаборатория!",
		description = f"**Бен смешал в колбу ваши 2 элемента, в этоге {xd}**",
		color = discord.Colour(random.randint(111111, 999999)))
		embed.set_footer(text = f"Команду использовал {ctx.author.name}")
		await ctx.reply(embed=embed)
		
@bot.command()
async def кормить(ctx):
	embed = discord.Embed(
	title = "Бобы",
	description = "**Вы наркомили бена бобами**",
	color = discord.Colour(random.randint(111111, 999999)))
	embed.set_footer(text = f"Команду использовал {ctx.author.name}")
	await ctx.send(embed=embed)
	
@bot.command()
async def напоить(ctx):
	embed = discord.Embed(
	title = "Яблочный сок",
	description = "**Вы напоили бена яблочным соком**",
	color = discord.Colour(random.randint(111111, 999999)))
	embed.set_footer(text = f"Команду использовал {ctx.author.name}")
	await ctx.send(embed=embed)
		
	
bot.run('MTAwMzIwMTIzNTAzOTU3MTk4OA.Gs62DL.3J8dRO0KdTY3WMC7ZcYjrqf7S1d07T2rwu7TqI')