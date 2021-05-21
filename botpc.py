# HiManBot Copyright 2021 By Zan4eg#5557
# Импорты библиотек

import discord
import random
from discord.ext import commands
import asyncio
import socket
import smtplib
import datetime
import pyowm
import json
from datetime import timedelta
import os
from Cybernator import Paginator as pag
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import json, socket, threading, time, concurrent.futures
from six.moves import urllib
from random import choice
import string
import requests
import pyshorteners

PREFIX = '.' # Переменная префикса

Bot = commands.Bot( command_prefix = PREFIX ) # Установка префикса бота
@Bot.remove_command('help') #Удаление стандартной комманды help

def get_random_string(length):
	letters = string.ascii_letters + string.digits
	result_str = ''.join(random.choice(letters) for i in range(length))
	return result_str

# При загрузке бота
@Bot.event
async def on_ready():
    activity = discord.Game(name = "HiManBot | .help", url='https://twitch.com/zan4egpayne')
    await Bot.change_presence( status = discord.Status.online, activity = activity )
    print("Logged in as HiManBot!")
    print("HiManBot Copyright 2021 By Zan4eg#5557")
    print("Бот запущен и готов к работе!")
    while True:
        await asyncio.sleep(8)
        await Bot.change_presence( status = discord.Status.online, activity = discord.Game(name = ".help | HiManBot") )
        await asyncio.sleep(8)
        await Bot.change_presence( status = discord.Status.online, activity = discord.Game(name = "Бот создан специально для сервера HiMan'a") )
        await asyncio.sleep(8)
        await Bot.change_presence( status = discord.Status.online, activity = discord.Game(name = "Бот создан Zan4eg#5557") )

@Bot.event
async def on_command_error(ctx, error):
	if isinstance(error, commands.CommandNotFound):
		await ctx.send(embed = discord.Embed(description = f'{ctx.author.name}, команда не найдена!', colour = discord.Color.red()))

@Bot.command()
async def suggest(ctx, *, txt = None):
	if txt is None:
		await ctx.send(f"**{ctx.author}**, напишите ваше предложение \n Пример команды: ***`.suggest Добавить нового бота`***")
	else:
		channel = Bot.get_channel(844901883259781160)
		emb = discord.Embed(title=f"**{ctx.author}, отправил своё улучшение!**", colour=0x04ff00)
		emb.add_field( name='**Текст идеи:**', value=txt)
		emb.set_footer(text= "HiManBot 💚 | Идеи")
		sugg = await channel.send( embed = emb )
		await sugg.add_reaction('✅')
		await sugg.add_reaction('❌')
		await ctx.send(f'**{ctx.author}, Ваша идея была отправлена!**')

@Bot.command()
async def ticket(ctx, *, txt = None, ):
	if txt is None:
		await ctx.send(f"**{ctx.author}**, напишите ваш вопрос\n Пример команды: ***.tiket `Как был создан этот сервер?`***")
	else:
		channel = Bot.get_channel(844901971424706597)
		emb = discord.Embed(title=f"❓ Новый вопрос!", colour=0x04ff00)
		emb.add_field( name='**Вопрос:**', value=txt)
		emb.add_field( name='**Задал:**', value=ctx.message.author.mention, inline = False)
		emb.set_footer(text= "HiManBot 💚 | Поддержка")
		sugg = await channel.send( embed = emb )
		await ctx.send(f'**{ctx.author}, Ваш вопрос был отправлен!**')

@Bot.command()
@commands.has_any_role(813107950309736448, 844982428174647336, 806102838174154774, 844982917259198494, 844983277528809492, 844983550743019530, 843926339421863966, 805802707390169088)
async def answer(ctx, user: discord.Member = None, *, txt = None):
	if user is None:
		await ctx.send(f"**{ctx.author}**, напишите кому хотите дать ответ\n Пример команды: ***.answer `@Ник` `Ответ`***")
	else:
		if txt is None:
			await ctx.send(f"**{ctx.author}**, напишите ответ\n Пример команды: ***.answer `@Ник` `Ответ`***")
		else:
			channel = Bot.get_channel(844901971424706597)
			emb = discord.Embed(title=f"❓ Новый ответ!", colour=0x04ff00)
			emb.add_field( name='**Ответ:**', value=txt)
			emb.add_field( name='**Задал:**', value=user, inline = False)
			emb.add_field( name='**Ответил:**', value=ctx.message.author.mention, inline = False)
			emb.set_footer(text= "HiManBot 💚 | Поддержка")
			sugg = await channel.send( embed = emb )
			await ctx.send(f'**{ctx.author}, Ваш ответ был отправлен!**')

# Информация о пользователе
@Bot.command( pass_context=True )
async def info(ctx, user: discord.Member = None):
    if user is None:
        await ctx.send(f"**{ctx.author}**, укажите участника сервера \n Пример команды: ***.info `@Пользователь`***")
    else:
        emb = discord.Embed( title="Информация об {}".format(user.name), colour=0x04ff00 ) # Создаем ембед
        emb.add_field( name='Имя', value=user.name ) # Получаем имя пользователя
        emb.add_field( name='Присоединился', value=user.joined_at ) # Получаем присоедение пользователя
        emb.add_field( name='Айди', value=user.id ) # Получаем айди пользователя
        emb.set_thumbnail( url=user.avatar_url ) # Получаем аватар пользователя
        emb.set_footer(text= "Упомянули: {}".format(user.name), icon_url= user.avatar_url) # Получаем имя пользователя и его аву (опять же)
        await ctx.send( embed = emb )

# Информация о создателе
@Bot.command( pass_context=True )
async def botcreater(ctx):
    emb = discord.Embed( title="Дискорд **Zan4eg#5557**", colour=0x04ff00 )  # Создаем ембед
    emb.set_footer(text= "Бот создан: 15.05.2021") # Получаем имя пользователя и его аву (опять же)
    await ctx.send( embed = emb )

# Очистка сообщений
@Bot.command( pass_context = True )
@commands.has_permissions( administrator = True ) # Установка нужных прав для комманды
async def clear ( ctx, amount : int = None):  # Создание комманды/функции
    if amount is None:
        await ctx.send(f"**{ctx.author}**, укажите количество сообщений для удаления \n Пример команды: ***.clear `кол-во сообщений`***")
    else:
        await ctx.channel.purge( limit = amount ) # Сама очистка
        emb = discord.Embed( description=f'✅  Очищено {amount} сообщений!', colour=0x04ff00 ) # Создание отчета об очистке
        await ctx.send( embed = emb )

# Информация о сервере
@Bot.command()
async def serverinfo(ctx):
    # Задаем переменные
    channels = len(ctx.guild.channels)
    text_channels = len(ctx.guild.text_channels)
    voice_channels = len(ctx.guild.voice_channels)
    categories = len(ctx.guild.categories)
    members = len(ctx.guild.members)
    embed = discord.Embed(title = 'Информация о сервере:', description = f'Назва сервера: `{ctx.guild.name}`\nАйди сервера: `{ctx.guild.id}`\nВсего участников: `{members}`\nВсего каналов и категорий: `{channels}`\nТекстовые каналы: `{text_channels}`\nГолосовые каналы: `{voice_channels}`\nКатегорий: `{categories}`', colour= 0x04ff00)
    await ctx.send( embed=embed )

# Статистика каналов
@Bot.command() 
async def stat(ctx, channel: discord.TextChannel = None):
    if not channel: #проверяем ввели ли канал
        channel = ctx.channel
        text = 'в данном канале'
    else:
        text = f'в #{channel.name}'
    await ctx.send(f"{ctx.author.mention}, я начинаю вычисления, подождите немного...") #отправляем сообщение о начале отсчёта
    counter = 0
    yesterday = datetime.datetime.today() - timedelta(days = 1)
    #начинаем считать сообщения
    async for message in channel.history(limit=None, after=yesterday):
        counter += 1
    counter2 = 0
    weekago = datetime.datetime.today() - timedelta(weeks = 1)
    async for message in channel.history(limit=None, after=weekago):
        counter2 += 1
    counter3 = 0
    monthago = datetime.datetime.today() - timedelta(weeks = 4)
    async for message in channel.history(limit=None, after=monthago):
        counter3 += 1
    embed = discord.Embed(title = f'Статиститка сообщений {text}', colour= 0x04ff00) #создаём embed-сообщение о подсчётах 
    embed.add_field(name = 'За сегодня', value = f'{counter}', inline = False) #добавляем поле "За сегодня"
    embed.add_field(name = 'За неделю', value = f'{counter2}', inline = False) #добавляем поле "За неделю" 
    embed.add_field(name = 'За месяц', value = f'{counter3}', inline = False) #добавляем поле "За месяц" 
    await ctx.send( f'{ctx.author.mention}', embed = embed ) #вывод сообщения с информацией о подсчётах

# Генератор паролей
lenght = int( '20' )
chars = '+-/*$#?=@<>abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
@Bot.command()
async def passgen( ctx ):
    password = ''
    for i in range( lenght ):
        password += random.choice( chars )
    emb = discord.Embed( description=f'✅ Ваш пароль был сгенерирован и отправлен вам в лс!', colour=0x04ff00 )
    em = discord.Embed( description=f'✅ Ваш пароль: {password}\n⚠️ Никому не показывайте этот пароль!', colour=0x04ff00 )
    await ctx.send( embed = emb )
    await ctx.author.send( embed = em )
	
@Bot.command()
async def randcolor(ctx):
	await ctx.message.delete()
	random_number = random.randint(0,16777215)
	hex_number = str(hex(random_number))
	hex_number ='#'+ hex_number[2:]
	em = discord.Embed(title="Random Color Hex", description = f'Hex color: {hex_number}', color=random_number)
	await ctx.send(embed = em)

@commands.cooldown(1, 5, commands.BucketType.user)
@Bot.command()
async def ping(ctx):
    em = discord.Embed(title="".format(ctx.guild.name), description="", color=0x04ff00)
    em.set_author(name="")
    em.add_field(name="Ping", value='Понг! :ping_pong:', inline=True)
    em.add_field(name="MS", value=f'Пинг бота: **{ctx.bot.latency * 1000:,.2f}ms**', inline=True)
    await ctx.send(embed=em)

        
@Bot.command()
async def slot(ctx):
    emojis = "🍎🍊🍐🍋🍉🍇🍓🍒"
    a = random.choice(emojis)
    b = random.choice(emojis)
    c = random.choice(emojis)
    slotmachine = f"**[ {a} {b} {c} ]\n{ctx.author.name}**,"
    if (a == b == c):
        await ctx.send(embed=discord.Embed.from_dict({"title":"Казино", "description":f"{slotmachine} Все совпадения, вы выиграли!"}))
    elif (a == b) or (a == c) or (b == c):
        await ctx.send(embed=discord.Embed.from_dict({"title":"Казино", "description":f"{slotmachine} 2 подряд вы выиграли!"}))
    else:
        await ctx.send(embed=discord.Embed.from_dict({"title":"Казино", "description":f"{slotmachine} Нет совпадения, вы проиграли"}))

@Bot.command()
async def userpic(ctx, *, avamember: discord.Member):
    emb = discord.Embed(title = f"Аватар {avamember.name}", colour = 0x04ff00)
    emb.set_image(url = avamember.avatar_url)
    await ctx.send(embed = emb)

@Bot.command()
async def botinfo(ctx):
    guilds = await Bot.fetch_guilds(limit = None).flatten()  
    emb = discord.Embed(title = "Статистика", colour = 0x04ff00)
    emb.add_field(name = "Основная:", value = f"Серверов: **{len(guilds)}**\nУчастников: **{len(set(Bot.get_all_members()))}**")    # 1: Количество серверов, 2: количество уникальных участников на всех серверах
    emb.add_field(name = "Бот:", value = f"Задержка: **{int(Bot.latency * 1000)} мс**") # Скорость соединения бота с API дискорда
    await ctx.send(embed = emb)


@Bot.command()
async def tinyurl(ctx, url : str = None):
    if url is None:
        await ctx.send(embed = discord.Embed(
                title = "Укоротитель ссылок",
                description = "Ошибка | Укажите ссылку которую хотите укоротить",
                colour = 0x04ff00
            ))
    else:
        shortener = pyshorteners.Shortener()
        short_url = shortener.tinyurl.short(url)
        await ctx.send("Ваша ссылка готова : " + short_url)

# Навигация по командам
@Bot.command( pass_context = True )
async def help( ctx, amount = 1 ):
    
    emb1=discord.Embed( title = 'Навигация по командам :pushpin:', colour= 0x04ff00 )
    emb1.set_thumbnail( url='https://cdn.discordapp.com/attachments/724886353065803778/766295278927216670/e52a182a29690cf9.png' )
    emb1.add_field( name = '``{}info``'.format( PREFIX ), value = 'Информация об пользователе.' )
    emb1.add_field( name = '``{}botcreater``'.format( PREFIX ), value = 'Создатель бота.' )
    emb1.add_field( name = '``{}stat``'.format( PREFIX ), value = 'Стистика каналов.' )
    emb1.add_field( name = '``{}serverinfo``'.format( PREFIX ), value = 'Информация о сервере.' )
    emb1.add_field( name = '``{}ping``'.format( PREFIX ), value= 'Узнать задержку бота.' )
    emb1.add_field( name = '``{}userpic``'.format( PREFIX ), value= 'Узнать аватар пользователя.' )
    emb1.add_field( name = '``{}botinfo``'.format( PREFIX ), value= 'Узнать статистику бота.' )
    emb1.add_field( name = '``{}tinyurl``'.format( PREFIX ), value= 'Укоротить ссылку.' )
    emb2=discord.Embed( title = 'Навигация по командам :pushpin:', colour= 0x04ff00 )
    emb2.set_thumbnail( url='https://cdn.discordapp.com/attachments/724886353065803778/766295281406181437/1abb1364301a30c7.png' )
    emb2.add_field( name = '``{}clear``'.format( PREFIX ), value = 'Очистка чата.' )
    emb2.add_field( name = '``{}suggest``'.format( PREFIX ), value = 'Предложить идею серверу.' )
    emb2.add_field( name = '``{}ticket``'.format( PREFIX ), value = 'Задать свой вопрос в поддержку.' )
    emb3=discord.Embed( title = 'Навигация по командам :pushpin:', colour= 0x04ff00 )
    emb3.set_thumbnail( url='https://cdn.discordapp.com/attachments/724886353065803778/766295277001768990/e2104f40da530197.png' )
    emb3.add_field( name = '``{}passgen``'.format( PREFIX ), value= 'Сгенерировать сложный пароль.' )
    emb3.add_field( name = '``{}slot``'.format( PREFIX ), value= 'Казино.' )
    emb3.add_field( name = '``{}randcolor``'.format( PREFIX ), value= 'Рандомный цвет.' )


    embeds = [emb1, emb2, emb3]

    message = await ctx.send(embed=emb1)
    page = pag(Bot, message, only=ctx.author, use_more=False, embeds=embeds)
    await page.start()

Bot.run('ODQ0OTY1MTE3NjAzMDg2Mzc2.YKaFFg.Y99CsnWwmASlUQP_lBncRCGioSA')
