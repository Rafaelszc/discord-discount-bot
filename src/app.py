import os
from dotenv import load_dotenv
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='$', intents=intents)
bot.remove_command('help')

load_dotenv(os.path.join('resources', 'env', 'token.env'))
TOKEN = os.getenv('TOKEN')
AUTHOR_ID = os.getenv('AUTHOR_ID')

async def load_cogs():
    for file in os.listdir(os.path.join('src', 'cogs')):
        if file.endswith('.py'):
            await bot.load_extension(f"cogs.{file.replace('.py', '')}")

@bot.event 
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="Extract data..."))
    print('bot on')
    await load_cogs()


@bot.command()
async def hello_world(ctx: commands.Context):
    if ctx.author.id == int(AUTHOR_ID):
        await ctx.reply("Hello World! End point ok!!!")
    else:
        await ctx.reply("no")

bot.run(TOKEN)