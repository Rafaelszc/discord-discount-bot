import os
from dotenv import load_dotenv
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='$', intents=intents)
bot.remove_command('help')

async def load_cogs():
    for file in os.listdir(os.path.join('src', 'cogs')):
        if file.endswith('.py'):
            await bot.load_extension(f"cogs.{file.replace('.py', '')}")

@bot.event 
async def on_ready():
    await load_cogs()
    print('bot on')

@bot.command()
async def hello_world(ctx: commands.Context):
    await ctx.reply("Hello World!")

load_dotenv(os.path.join('resources', 'env', 'token.env'))
TOKEN = os.getenv('TOKEN')

bot.run(TOKEN)