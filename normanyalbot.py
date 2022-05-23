import json
import requests
import random
import aiohttp
import io
import discord
from discord.ext import commands
import os
import asyncio
intents = discord.Intents.all()
intents.members = True

bot = commands.Bot(command_prefix = "&", intents = intents)
bot.activity = discord.Game(name = "Мои команды — &хелп")


@bot.remove_command("help")

@bot.event
async def on_ready():
	print('Подключено к {0.user}'.format(bot))

	
@bot.event
async def on_command_error(ctx, error):
	if isinstance(error, commands.CommandNotFound ):
		await ctx.send(embed = discord.				Embed(title ="Ошибка", description = f'**Данная команда не найдена**', color = discord.Colour(random.randint(111111, 999999))))
		
		
@bot.command()
async def шар(ctx, message = None):
				
			if message == None:
				embed = discord.Embed(title = "Ошибка", description = "**Введите сообщение чтобы шар ответил!**", color = discord.Colour(random.randint(111111, 999999)))
				await ctx.send(embed=embed)
				
			else:
				ball = random.randint(1, 8)
			if ball == 1:
				embed = discord.Embed(title = "Шар🔮", description = "**Шар ответил на ваш вопрос: Не знаю🤷**", color = discord.Colour(random.randint(111111, 999999)))
				embed.set_footer(text = f"Команду использовал {ctx.author.nick}", icon_url = ctx.author.avatar_url)
				await ctx.send(embed=embed)
				
			if ball == 2:
				embed = discord.Embed(title = "Шар🔮", description = "**Шар ответил на ваш вопрос: Я не расслышал🔇, спроси ещё раз.**", color = discord.Colour(random.randint(111111, 999999)))
				embed.set_footer(text = f"Команду использовал {ctx.author.nick}", icon_url = ctx.author.avatar_url)
				await ctx.send(embed=embed)
				
			if ball == 3:
				embed = discord.Embed(title = "Шар🔮", description = "**Шар ответил на ваш вопрос: Нет конечно!❌**", color = discord.Colour(random.randint(111111, 999999)))
				embed.set_footer(text = f"Команду использовал {ctx.author.nick}", icon_url = ctx.author.avatar_url)
				await ctx.send(embed=embed)
				
			if ball == 4:
				embed = discord.Embed(title = "Шар🔮", description = "**Шар ответил на ваш вопрос: Конечно же да!✅**", color = discord.Colour(random.randint(111111, 999999)))
				embed.set_footer(text = f"Команду использовал {ctx.author.nick}", icon_url = ctx.author.avatar_url)
				await ctx.send(embed=embed)
				
			if ball == 5:
				embed = discord.Embed(title = "Шар🔮", description = "**Шар ответил на ваш вопрос: Неа❌**", color = discord.Colour(random.randint(111111, 999999)))
				embed.set_footer(text = f"Команду использовал {ctx.author.nick}", icon_url = ctx.author.avatar_url)
				await ctx.send(embed=embed)
				
			if ball == 6:
				embed = discord.Embed(title = "Шар🔮", description = "**Шар ответил на ваш вопрос: Да✅**", color = discord.Colour(random.randint(111111, 999999)))
				embed.set_footer(text = f"Команду использовал {ctx.author.nick}", icon_url = ctx.author.avatar_url)
				await ctx.send(embed=embed)
				
			if ball == 7:
				embed = discord.Embed(title = "Шар🔮", description = "**Шар ответил на ваш вопрос: 50 на 50**", color = discord.Colour(random.randint(111111, 999999)))
				embed.set_footer(text = f"Команду использовал {ctx.author.nick}", icon_url = ctx.author.avatar_url)
				await ctx.send(embed=embed)
				
			if ball == 8:
				embed = discord.Embed(title = "Шар🔮", description = "**Шар упал и треснул.....**", color = discord.Colour(random.randint(111111, 999999)))
				embed.set_footer(text = f"Команду использовал {ctx.author.nick}", icon_url = ctx.author.avatar_url)
				await ctx.send(embed=embed)
		
		
@bot.command()
async def лиса(ctx):
    response = requests.get('https://some-random-api.ml/img/fox')
    json_data = json.loads(response.text)

    embed = discord.Embed(color = discord.Colour(random.randint(111111, 999999)), title = 'Лиса')
    embed.set_image(url = json_data['link'])
    embed.set_footer(text = f"Команду использовал {ctx.author.nick}", icon_url = ctx.author.avatar_url)
    await ctx.send(embed = embed)

@bot.command()
async def собака(ctx):
    response = requests.get('https://some-random-api.ml/img/dog')
    json_data = json.loads(response.text)

    embed = discord.Embed(color = discord.Colour(random.randint(111111, 999999)), title = 'Собачка')
    embed.set_image(url = json_data['link'])
    embed.set_footer(text = f"Команду использовал {ctx.author.nick}", icon_url = ctx.author.avatar_url)
    await ctx.send(embed = embed)

@bot.command()
async def кот(ctx):
    response = requests.get('https://some-random-api.ml/img/cat')
    json_data = json.loads(response.text)

    embed = discord.Embed(color = discord.Colour(random.randint(111111, 999999)), title = 'Кот')
    embed.set_image(url = json_data['link'])
    embed.set_footer(text = f"Команду использовал {ctx.author.nick}", icon_url = ctx.author.avatar_url)
    await ctx.send(embed = embed)
    

@bot.command()
async def инфо(ctx):
    embed = discord.Embed(
        title = "Информация",
        description = f"> **Профиль бота:** ``{bot.user}``\n> **Версия бота:** ``92.31 — Stable``\n> **Имя бота:** ``{bot.user.name}``\n> **ID бота:** ``{bot.user.id}``\n> **Пинг бота:** ``{round(bot.latency)}ms``",
        color = discord.Colour(random.randint(111111, 999999)))
    embed.set_footer(text = f"Команду использовал {ctx.author.nick}", icon_url = ctx.author.avatar_url)
    await ctx.reply(embed = embed)
    
@bot.command()
async def съесть(ctx):
	import random
	what = random.randint(1, 6)
	embed = None
	if what > 2:
		embed = discord.Embed(
			title = "Негр",
			description = "**Вы увидели первого попавшего на глаза негра и съели его.**",
			color = discord.Colour(random.randint(111111, 999999)))
	else:
		embed = discord.Embed(
			title = "Негр",
			description = "**Вы захотели съесть негра, но у него оказалась реакция лучше и он съел вас первым.**",
			color = discord.Colour(random.randint(111111, 999999)))
	embed.set_footer(text = f"Команду использовал {ctx.author.nick}", icon_url = ctx.author.avatar_url)
	await ctx.reply(embed = embed)
	

@bot.command()
async def палка(ctx):
    loading = True
    text = ""
    message = await ctx.reply("-")
    while loading:
        text = "|"
        await message.edit(content = text)
        await asyncio.sleep(0.4)
        text = "/"
        await message.edit(content = text)
        await asyncio.sleep(0.4)
        text = "-"
        await message.edit(content = text)
        await asyncio.sleep(0.4)
        text2 = "\n"
        text2 = repr(text2)
        text2 = text2.replace("'", "")
        text2 = text2.replace("n", "")
        text = text2
        await message.edit(content = text)
    await asyncio.sleep(10)
    loading = False
    
    
@bot.command()
async def хелп(ctx):
	embed = discord.Embed(
	title = "Команды бота",
	description = "**&кот\n&собака\n&лиса\n&инфо\n&палка\n&съесть\n&шар\n&хелп**",
	color = discord.Colour(random.randint(111111, 999999)))
	embed.set_footer(text = f"Команду использовал {ctx.author.nick}", icon_url = ctx.author.avatar_url)
	await ctx.reply(embed = embed)





	
bot.run('OTYyNzAwMjc4ODUzOTU5Nzcw.G9zN1y.i0WV7098oF8_aoKBgZogHNFFrCA0ebJXOH4nc8')