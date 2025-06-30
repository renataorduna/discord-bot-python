import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_BOT_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'✅ Bot conectado como {bot.user}')

@bot.command()
async def hola(ctx):
    await ctx.send(f'¡Hola {ctx.author.name}!')

@bot.command()
async def paisaje(ctx):
    url = "https://images.unsplash.com/photo-1511884642898-4c92249e20b6?q=80&w=870&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
    await ctx.send(url)

bot.run(TOKEN)
