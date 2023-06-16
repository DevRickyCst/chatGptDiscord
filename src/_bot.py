import os
import discord
from discord.ext import commands

#Need it to start the bot
intents = discord.Intents.default()
intents.typing = False
intents.message_content = True

class BotDiscord(commands.Bot):

    def __init__(self, intents=intents, command_prefix='$') -> None:
        self.token = os.getenv("discord_token")
        commands.Bot.__init__(self, intents=intents,command_prefix='$')
