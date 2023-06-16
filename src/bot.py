import discord
from discord.ext import commands
from _discord import send_message
import os
from dotenv import load_dotenv

load_dotenv()

#def run_discord_bot():
intents = discord.Intents.default()
intents.typing = False
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)


@bot.command()
async def chat_gpt(ctx, *args):
    texte = ' '.join(args)
    await send_message(ctx, texte ,False)

bot.run(os.getenv("discord_token"))




