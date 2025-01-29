import discord
import os
from discord.ext import commands

# Set up the bot with a command prefix
intents = discord.Intents.default()
intents.message_content = True  # Enable access to message content
bot = commands.Bot(command_prefix="!", intents=intents)

# Event: When the bot is ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} (ID: {bot.user.id})')
    print('------')

# Command: Respond to !hello
@bot.command()
async def hello(ctx):
    await ctx.send(f'Hello, {ctx.author.name}!')

# Command: Respond to !classroom
@bot.command()
async def classroom(ctx):
    await ctx.send('Google Classroom integration coming soon!')

# Run the bot with your token
bot.run(os.getenv("DISCORD_TOKEN"))
