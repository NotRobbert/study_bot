import re
import discord
import logging
import os
import asyncio
import studydb

from dotenv import load_dotenv
from discord.ext import commands, tasks
from discord import app_commands



load_dotenv()#loads variables from the .env
token = os.getenv('DISCORD_TOKEN') #gets the discord token from the .env file

UNITS = {"s": 1, "m": 60, "h": 3600, "d": 86400, "w": 604800}#dic for the units to seconds
MAX_SECONDS = 365*86400 #max seconds cant be more than a year
MAX_MESSAGE_LENGTH = 200

def parse_duration(text):#convert to seconds
    text = text.strip().lower().replace(" ","")#strips so its just number+unit (10m)
    if not re.fullmatch(r"(?:\d+[smhdw])+",text):#\d matches more than one digit and the + groups it one more time if needed so 1h5m and it must match so no h1, m30
        return None
    total = sum(int(n)*UNITS[u] for n, u in re.findall(r"(\d+)([smhdw])", text))#capture groups in parentheses e.g. [("1", "h"), ("5", "m")], calculates each pair then sums
    return total or None


handler = logging.FileHandler(filename='discordbot.log', encoding='utf-8', mode='w') #creates a log file
intents = discord.Intents.default() #uses the default intents
intents.message_content = True
intents.members = True


bot = commands.Bot(command_prefix='!', intents=intents) #prefix for bot commands in server

@bot.event
async def on_ready():
    print(f"BEEP BOOP {bot.user.name} IS ONLINE")#displays a message in terminal so i know if bot is running
    return

@bot.event
async def on_message(message):
    if message.author == bot.user:#makes sure the bot doesnt loop on its own messages
        return
    await bot.process_commands(message)

@bot.command()
async def hello(ctx):
    await ctx.send(f"hello {ctx.author.mention}")#says hello back to the user when propted

@bot.command()
async def reminder(ctx, when: str = None, *,message: str = None): #when takes the first word after the reminder command, = None makes both optional
    if when is None or message is None:
        await ctx.send("How to: '!reminder 30m start study session'")#if reminder command is empty, it sends a message describing how to use it
        return
    seconds = parse_duration(when)
    if seconds is None or seconds > MAX_SECONDS:
        await ctx.send("I couldn't read that time. Try something like '10m', '1h' or '1h30m' (NO LONGER THAN A YEAR!!)")#if seconds longer than a year or is none throw an error to the user and guide them
        return
    if len(message) > MAX_MESSAGE_LENGTH:
        await ctx.send("Message was longer than 200 characters, im sorry but i couldn't read it")#if message over max length constant variable then let the user know
        return
    await ctx.send(f"Okay{ctx.author.mention},Lets start the study session - {when}: {message}")#confirms the study session
    await asyncio.sleep(seconds)#waits for the reminder time, await lets the bot keep handling other messages in the meantime
    await  ctx.send(f"{ctx.author.mention} Study session complete")#alerts the user when time is up


bot.run(token, log_handler=handler, log_level=logging.INFO) #runs bot