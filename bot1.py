import discord
import time
from bot_logic import gen_pass
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi {bot.user}!')

@bot.command()
async def password(ctx):
    await ctx.send(gen_pass(10))

@bot.group()
async def cool(ctx):
    """Says if a user is cool.

    In reality this just checks if a subcommand is being invoked.
    """
    if ctx.invoked_subcommand is None:
        await ctx.send(f'No, {ctx.subcommand_passed} is not cool')


@cool.command(name='bot')
async def _bot(ctx):
    """Is the bot cool?"""
    await ctx.send('Yes, the bot is cool.')

bot.run("MTI5Njk3NjE5ODEyMzEyNjgwNA.G8SsQd.423gifEadb5g_qBjcFF4GQgjmfKvenaGJL5xGc")