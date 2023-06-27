import os

from dotenv import load_dotenv

from cogs.src._botDiscord import BotDiscord

from cogs.openai import openai
from cogs.textToSpeech import textToSpeech

load_dotenv()

async def load_env():
    for cog in cogs:
        try:
            await bot.add_cog(cog)
        except:
            f"Couldn't load {cog} module"


if __name__ == "__main__":

    bot = BotDiscord()
    cogs = [openai(bot, os.getenv("openai_api_key")), textToSpeech(bot)]

    @bot.event
    async def on_ready():
        print(f"Connecté en tant que {bot.user.name} ({bot.user.id})")
        print("------")

        await load_env()

    bot.run(os.getenv("discord_token"))
