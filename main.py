import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os

load_dotenv()#loads variables from the .env
token = os.getenv('DISCORD_TOKEN') #gets the discord token from the .env file

handler = logging.FileHandler(filename='discordbot.log', encoding='utf-8', mode='w') #creates a log file