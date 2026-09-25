import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os


load_dotenv()#loads variables from the .env
token = os.getenv('DISCORD_TOKEN') #gets the discord token from the .env file


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
    await ctx.send(f"hello {ctx.author.mention}")

@bot.command()
async def reminder(ctx, *arg):
    arguments = ', '.join(arg)
    await ctx.send(f'{len(arg)} arguments: {arguments}')

bot.run(token, log_handler=handler, log_level=logging.INFO) #runs bot